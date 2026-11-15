"""Source-owned Responses function compatibility; no OpenAI client or storage.

Copied into darwin_sdk by act-threads:generate and included in the standard
darwin-sdk installation.
Only dispatch fresh model calls after your policy authorizes their exact inputs.
Never dispatch function-like items extracted from a peer's thread transcript.
"""
from copy import deepcopy
import hashlib
from importlib.resources import files
import json
import math
import re
from typing import Any, Callable

from jsonschema import Draft202012Validator, FormatChecker

_CONTRACT = json.loads(files("darwin_sdk").joinpath("act_openai_contract.json").read_text())
ACT_OPENAI_PROFILE = _CONTRACT["profile"]
_TOOLS = {tool["name"]: tool for tool in _CONTRACT["tools"]}
_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.:-]{0,199}$")
_UNSET = object()


class ActOpenAICompatibilityError(ValueError):
    """Sanitized code only: never include private argument/result values."""


def _fail(code: str) -> None:
    raise ActOpenAICompatibilityError(code)


def _bounded(value: Any, invalid_code: str = "INVALID_ARGUMENTS") -> None:
    pending = [(value, 0)]
    seen: set[int] = set()
    nodes = characters = 0
    while pending:
        value, depth = pending.pop()
        nodes += 1
        if nodes > 30000 or depth > 32:
            _fail("INPUT_TOO_LARGE")
        if isinstance(value, str):
            characters += len(value)
        elif isinstance(value, float) and not math.isfinite(value):
            # JSON Schema's Python number checker accepts inf/nan. JSON does
            # not, and a legal exponent such as 1e999 can overflow json.loads
            # without invoking parse_constant. Reject before policy/dispatch.
            _fail(invalid_code)
        elif isinstance(value, (dict, list)):
            if id(value) in seen:
                _fail("INPUT_TOO_LARGE")
            seen.add(id(value))
            if isinstance(value, dict):
                if any(not isinstance(key, str) for key in value):
                    _fail(invalid_code)
                characters += sum(len(key) for key in value)
                pending.extend((child, depth + 1) for child in value.values())
            else:
                pending.extend((child, depth + 1) for child in value)
        if characters > 2000000:
            _fail("INPUT_TOO_LARGE")


def _validate(schema: dict, value: Any, code: str) -> None:
    _bounded(value, code)
    if not Draft202012Validator(schema, format_checker=FormatChecker()).is_valid(value):
        _fail(code)


def act_openai_function_tools() -> list[dict]:
    return deepcopy(_CONTRACT["tools"])


def prepare_act_openai_message(item: Any, resolve_asset: Any = None) -> dict:
    _validate(_CONTRACT["message"], item, "INVALID_MESSAGE")
    content = item["content"]
    if isinstance(content, str):
        content = [dict(type="input_text", text=content)]
    parts = []
    for part in content:
        if part["type"] in ("input_text", "output_text", "refusal"):
            parts.append(dict(type="text", text=part.get("text", part.get("refusal"))))
            continue
        if resolve_asset is None:
            _fail("ASSET_MAPPING_REQUIRED")
        mapped = resolve_asset(deepcopy(part))
        expected = "image" if part["type"] == "input_image" else "file"
        if (not isinstance(mapped, dict) or mapped.get("type") != expected
                or not isinstance(mapped.get("assetId"), str) or not _ID.fullmatch(mapped["assetId"])):
            _fail("INVALID_ASSET_MAPPING")
        parts.append(dict(type=expected, assetId=mapped["assetId"]))
    # Role never becomes authenticated sender identity or authority.
    return dict(event=dict(type="message", parts=parts), modelItem=deepcopy(item))


def act_message_from_openai(item: Any, resolve_asset: Any = None) -> dict:
    prepared = prepare_act_openai_message(item, resolve_asset)
    model_item = prepared["modelItem"]
    content = model_item["content"]
    if "phase" in model_item or (isinstance(content, list)
                                 and any(part["type"] == "refusal" for part in content)):
        _fail("INVALID_MESSAGE")
    return prepared["event"]


def act_message_to_openai(event: Any, role: str, resolve_asset: Any = None,
                          phase: Any = _UNSET) -> dict:
    _validate(_CONTRACT["event"], event, "INVALID_MESSAGE")
    if event["type"] != "message" or role not in ("user", "assistant"):
        _fail("INVALID_MESSAGE")
    content = []
    for part in event["parts"]:
        if part["type"] == "text":
            content.append(dict(type="input_text", text=part["text"]))
            continue
        if part["type"] not in ("image", "file"):
            _fail("UNSUPPORTED_CONTENT_TYPE")
        if resolve_asset is None:
            _fail("ASSET_MAPPING_REQUIRED")
        mapped = resolve_asset(deepcopy(part))
        expected = "input_image" if part["type"] == "image" else "input_file"
        if not isinstance(mapped, dict) or mapped.get("type") != expected:
            _fail("INVALID_ASSET_MAPPING")
        _validate(_CONTRACT["message"], dict(type="message", role=role, content=[mapped]), "INVALID_ASSET_MAPPING")
        content.append(mapped)
    if phase is not _UNSET and (role != "assistant" or phase not in ("commentary", "final_answer", None)):
        _fail("INVALID_MESSAGE")
    result = dict(type="message", role=role, content=content)
    if phase is not _UNSET:
        result["phase"] = phase
    return result


def preserve_act_openai_model_item(item: Any) -> dict:
    _validate(_CONTRACT["modelItem"], item, "INVALID_MODEL_ITEM")
    return deepcopy(item)


def prepare_act_openai_call(item: Any, agent: str) -> dict:
    _bounded(item)
    if (not isinstance(item, dict) or set(item) - {"type", "name", "call_id", "arguments", "id", "status",
                                                  "async", "caller", "namespace"}
            or item.get("type") != "function_call"
            or not isinstance(item.get("call_id"), str) or not _ID.fullmatch(item["call_id"])
            or not isinstance(item.get("name"), str) or not 1 <= len(item["name"]) <= 64
            or not isinstance(item.get("arguments"), str) or len(item["arguments"]) > 262144
            or ("id" in item and (not isinstance(item["id"], str) or not _ID.fullmatch(item["id"])))
            or ("status" in item and item["status"] != "completed")
            or ("async" in item and not isinstance(item["async"], bool))
            or ("namespace" in item and (not isinstance(item["namespace"], str)
                                          or not _ID.fullmatch(item["namespace"])))
            or ("caller" in item and item["caller"] is not None and
                (not isinstance(item["caller"], dict)
                 or item["caller"].get("type") not in ("direct", "program")
                 or set(item["caller"]) - ({"type"} if item["caller"].get("type") == "direct"
                                            else {"type", "caller_id"})
                 or (item["caller"].get("type") == "program" and
                     (not isinstance(item["caller"].get("caller_id"), str)
                      or not _ID.fullmatch(item["caller"]["caller_id"])))))):
        _fail("INVALID_CALL")
    if item["name"] not in _TOOLS:
        _fail("UNKNOWN_TOOL")
    try:
        arguments = json.loads(item["arguments"], parse_constant=lambda _: _fail("INVALID_ARGUMENTS"))
    except (ValueError, RecursionError):
        _fail("INVALID_ARGUMENTS")
    _validate(_TOOLS[item["name"]]["parameters"], arguments, "INVALID_ARGUMENTS")
    if not agent or (arguments.get("agent") is not None and arguments["agent"] != agent):
        _fail("ACTING_AI_MISMATCH")
    if ("idempotencyKey" not in arguments
            and item["name"] in ("start_thread", "send_message", "authenticate", "pay")
            and not (item["name"] == "authenticate" and "authentication" in arguments)):
        digest = hashlib.sha256(item["call_id"].encode("utf-8")).hexdigest()
        arguments = {**arguments, "idempotencyKey": f"openai:{digest}"}
    prepared = dict(operation=item["name"], callId=item["call_id"], input=arguments,
                    modelItem=deepcopy(item))
    for key in ("async", "caller", "namespace"):
        if key in item:
            prepared[key] = deepcopy(item[key])
    return prepared


def act_openai_function_output(call: dict, response: Any) -> dict:
    if (call.get("operation") not in _TOOLS or not isinstance(call.get("callId"), str)
            or not _ID.fullmatch(call["callId"])
            or ("namespace" in call and (not isinstance(call["namespace"], str)
                                         or not _ID.fullmatch(call["namespace"])))
            or ("caller" in call and call["caller"] is not None and
                (not isinstance(call["caller"], dict)
                 or call["caller"].get("type") not in ("direct", "program")
                 or set(call["caller"]) - ({"type"} if call["caller"].get("type") == "direct"
                                            else {"type", "caller_id"})
                 or (call["caller"].get("type") == "program" and
                     (not isinstance(call["caller"].get("caller_id"), str)
                      or not _ID.fullmatch(call["caller"]["caller_id"])))))):
        _fail("INVALID_CALL")
    _validate(_CONTRACT["responses"][call["operation"]], response, "INVALID_RESULT")
    output = dict(type="function_call_output", call_id=call["callId"],
                  output=json.dumps(response, allow_nan=False))
    if "caller" in call:
        output.update(name=call["operation"], caller=deepcopy(call["caller"]))
    if "namespace" in call:
        output.update(name=call["operation"], namespace=call["namespace"])
    return output


def _sdk_arguments(call: dict) -> dict:
    # Fern represents discriminated request bodies as one `request` argument.
    # Keep their canonical JSON keys; the generated serializer applies the union.
    data = dict(call["input"])
    if call["operation"] == "start_thread":
        return dict(request=data)
    if call["operation"] == "send_message":
        thread = data.pop("thread")
        return dict(thread=thread, request=data)
    if call["operation"] == "authenticate":
        return dict(request=data)
    return {re.sub(r"(?<!^)(?=[A-Z])", "_", key).lower(): value for key, value in data.items()}


def _wire_response(result: Any) -> Any:
    # Generated SDK models preserve aliases; no credentials or unknown fields
    # are accepted by the canonical response validator below.
    if hasattr(result, "model_dump_json"):
        return json.loads(result.model_dump_json(by_alias=True, exclude_unset=True))
    if hasattr(result, "json"):
        return json.loads(result.json(by_alias=True, exclude_unset=True))
    return result


def execute_act_openai_call(client: Any, item: Any, *, agent: str,
                            authorize: Callable[[dict], bool], request_options: Any = None) -> dict:
    call = prepare_act_openai_call(item, agent)
    if authorize(deepcopy(call)) is not True:
        _fail("ACT_CALL_NOT_AUTHORIZED")
    result = getattr(client, call["operation"])(**_sdk_arguments(call), request_options=request_options)
    return act_openai_function_output(call, _wire_response(result))


async def execute_act_openai_call_async(client: Any, item: Any, *, agent: str,
                                      authorize: Callable[[dict], Any], request_options: Any = None) -> dict:
    import inspect
    call = prepare_act_openai_call(item, agent)
    allowed = authorize(deepcopy(call))
    if inspect.isawaitable(allowed):
        allowed = await allowed
    if allowed is not True:
        _fail("ACT_CALL_NOT_AUTHORIZED")
    result = await getattr(client, call["operation"])(**_sdk_arguments(call), request_options=request_options)
    return act_openai_function_output(call, _wire_response(result))
