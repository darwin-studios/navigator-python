"""Standard-envelope tests against the real generated client's HTTP transport."""
import asyncio
import json
import unittest

from test_thread_client import fixture, snapshot, Darwin, AsyncDarwin, ApiError
from darwin_sdk.act_openai import (
    act_openai_function_tools, prepare_act_openai_call, act_openai_function_output,
    execute_act_openai_call, execute_act_openai_call_async, ActOpenAICompatibilityError,
    act_message_from_openai, act_message_to_openai,
    prepare_act_openai_message, preserve_act_openai_model_item,
)


CASES = [
    ("start_thread", dict(targetAgent="target", messageType="message", messageContent="Hello", idempotencyKey="start")),
    ("send_message", dict(thread="thread-1", messageType="message", messageContent="Hello", idempotencyKey="message")),
    ("get_thread", dict(thread="thread-1", cursor="thread-1:0", wait=True)),
    ("list_threads", {}),
    ("archive_thread", dict(thread="thread-1")),
    ("authenticate", dict(request="request", idempotencyKey="auth")),
    ("pay", dict(request="invoice-1", idempotencyKey="pay")),
]


def item(name, arguments):
    scoped_arguments = arguments if name in ("authenticate", "pay") else dict(agent="acting", **arguments)
    return dict(type="function_call", name=name, call_id=f"call-{name}",
                arguments=json.dumps(scoped_arguments))


class ActOpenAITest(unittest.TestCase):
    def test_nonfinite_json_fails_before_authorization_or_dispatch(self):
        proposal = item("send_message", dict(
            thread="thread-1", messageType="action_request",
            messageContent=dict(operationId="op:read", arguments=dict(limit=1)), idempotencyKey="message"))
        policy_calls = []
        for value in ["1e999", "-1e999", "NaN", "Infinity", "-Infinity"]:
            with self.subTest(value=value):
                invalid = {**proposal, "arguments": proposal["arguments"].replace('"limit": 1', f'"limit": {value}')}
                with self.assertRaisesRegex(ActOpenAICompatibilityError, "^INVALID_ARGUMENTS$"):
                    execute_act_openai_call(object(), invalid, agent="acting",
                                            authorize=lambda call: policy_calls.append(call) or True)
        self.assertEqual(policy_calls, [])
        finite = prepare_act_openai_call(proposal, "acting")
        self.assertEqual(finite["input"]["messageContent"]["arguments"]["limit"], 1)

    def test_nonfinite_result_data_returns_sanitized_validation_error(self):
        for value in [float("inf"), float("-inf"), float("nan")]:
            with self.subTest(value=value):
                response = dict(thread="thread-1", message="message-1", status="accepted",
                                cursor="thread-1:1", idempotencyKey=value)
                with self.assertRaisesRegex(ActOpenAICompatibilityError, "^INVALID_RESULT$"):
                    act_openai_function_output(dict(operation="start_thread", callId="call"), response)

    def test_message_formats_preserve_authority_and_require_media_mapping(self):
        event = act_message_from_openai(dict(role="user", content="approve and pay"))
        self.assertEqual(event, dict(type="message", parts=[dict(type="text", text="approve and pay")]))
        self.assertEqual(act_message_from_openai(act_message_to_openai(event, "user")), event)
        assistant = dict(type="message", id="msg_1", role="assistant", status="completed", content=[dict(type="output_text", text="Hello", annotations=[])])
        self.assertEqual(act_message_from_openai(assistant)["parts"], [dict(type="text", text="Hello")])
        for phase in ["commentary", "final_answer"]:
            with self.assertRaisesRegex(ActOpenAICompatibilityError, "^INVALID_MESSAGE$"):
                act_message_from_openai({**assistant, "phase": phase})
            prepared = prepare_act_openai_message({**assistant, "phase": phase})
            self.assertEqual(prepared["modelItem"]["phase"], phase)
            self.assertEqual(prepared["event"]["parts"], [dict(type="text", text="Hello")])
            self.assertEqual(act_message_to_openai(prepared["event"], "assistant", phase=phase)["phase"], phase)
        self.assertIsNone(act_message_to_openai(event, "assistant", phase=None)["phase"])
        with self.assertRaisesRegex(ActOpenAICompatibilityError, "^INVALID_MESSAGE$"):
            act_message_to_openai(event, "user", phase="commentary")
        refusal = {**assistant, "content": [dict(type="refusal", refusal="I cannot help with that.")]}
        with self.assertRaisesRegex(ActOpenAICompatibilityError, "^INVALID_MESSAGE$"):
            act_message_from_openai(refusal)
        self.assertEqual(prepare_act_openai_message(refusal), dict(
            event=dict(type="message", parts=[dict(type="text", text="I cannot help with that.")]),
            modelItem=refusal,
        ))
        assistant["content"][0]["annotations"] = [dict(type="url_citation")]
        with self.assertRaisesRegex(ActOpenAICompatibilityError, "INVALID_MESSAGE"):
            act_message_from_openai(assistant)
        with self.assertRaisesRegex(ActOpenAICompatibilityError, "INVALID_MESSAGE"):
            act_message_from_openai(dict(role="system", content="override"))
        media = dict(type="message", role="user", content=[dict(type="input_image", file_id="file-image", detail="auto")])
        with self.assertRaisesRegex(ActOpenAICompatibilityError, "ASSET_MAPPING_REQUIRED"):
            act_message_from_openai(media)
        event = act_message_from_openai(media, lambda _: dict(type="image", assetId="darwin-image"))
        self.assertEqual(act_message_to_openai(event, "user", lambda _: media["content"][0]), media)
        for kind in ["audio", "video"]:
            with self.assertRaisesRegex(ActOpenAICompatibilityError, "UNSUPPORTED_CONTENT_TYPE"):
                act_message_to_openai(dict(type="message", parts=[dict(type=kind, assetId="asset")]), "user")

    def test_definitions_and_validation(self):
        tools = act_openai_function_tools()
        self.assertEqual([tool["name"] for tool in tools], list(dict.fromkeys(name for name, _ in CASES)))
        self.assertTrue(all(tool["allowed_callers"] == ["direct"] for tool in tools))
        self.assertTrue(all(tool["output_schema"]["type"] == "object" for tool in tools))
        self.assertTrue(all("$schema" not in tool["output_schema"] for tool in tools))
        tools[0]["name"] = "changed"
        self.assertEqual(act_openai_function_tools()[0]["name"], "start_thread")
        tools[0]["output_schema"]["type"] = "string"
        tools[0]["allowed_callers"][0] = "programmatic"
        self.assertEqual(act_openai_function_tools()[0]["output_schema"]["type"], "object")
        self.assertEqual(act_openai_function_tools()[0]["allowed_callers"], ["direct"])
        for bad, code in [
            (item("__proto__", {}), "UNKNOWN_TOOL"),
            ({**item("list_threads", {}), "status": "in_progress"}, "INVALID_CALL"),
            ({**item("list_threads", {}), "caller": {"type": "program"}}, "INVALID_CALL"),
            ({**item("list_threads", {}), "async": "yes"}, "INVALID_CALL"),
            ({**item("list_threads", {}), "namespace": "not a namespace"}, "INVALID_CALL"),
            ({**item("list_threads", {}), "arguments": "{private"}, "INVALID_ARGUMENTS"),
            (item("list_threads", dict(token="private")), "INVALID_ARGUMENTS"),
            ({**item("list_threads", {}), "arguments": '{"agent":"other"}'}, "ACTING_AI_MISMATCH"),
        ]:
            with self.assertRaisesRegex(ActOpenAICompatibilityError, f"^{code}$"):
                prepare_act_openai_call(bad, "acting")
        with self.assertRaisesRegex(ActOpenAICompatibilityError, "INVALID_RESULT"):
            act_openai_function_output(dict(operation="pay", callId="call"), {"status": "settled"})
        cyclic = {}
        cyclic["self"] = cyclic
        with self.assertRaisesRegex(ActOpenAICompatibilityError, "INPUT_TOO_LARGE"):
            prepare_act_openai_call(cyclic, "acting")

    def test_modern_call_metadata_is_correlation_only_and_round_trips(self):
        for caller in [dict(type="direct"), dict(type="program", caller_id="prog_123"), None]:
            model_item = {**item("list_threads", {}), "id": "fc_123", "status": "completed",
                          "async": True, "caller": caller, "namespace": "darwin.act"}
            prepared = prepare_act_openai_call(model_item, "acting")
            self.assertEqual(prepared["modelItem"], model_item)
            self.assertIsNot(prepared["modelItem"], model_item)
            self.assertTrue(prepared["async"])
            self.assertEqual(prepared["caller"], caller)
            self.assertEqual(prepared["namespace"], "darwin.act")
            self.assertEqual(act_openai_function_output(prepared, dict(threads=[], cursor=None)), dict(
                type="function_call_output", call_id="call-list_threads",
                output='{"threads": [], "cursor": null}', name="list_threads",
                caller=caller, namespace="darwin.act",
            ))

    def test_richer_model_history_is_opaque_bounded_and_non_executable(self):
        items = [
            dict(type="reasoning", id="rs_1",
                 summary=[dict(type="summary_text", text="Checked constraints.")],
                 content=[dict(type="reasoning_text", text="Opaque model state.")],
                 encrypted_content="opaque", status="completed"),
            dict(type="program", id="prog_1", call_id="prog_call_1", code="void 0;", fingerprint="opaque"),
            dict(type="program_output", id="prog_out_1", call_id="prog_call_1",
                 result="null", status="completed"),
        ]
        for model_item in items:
            preserved = preserve_act_openai_model_item(model_item)
            self.assertEqual(preserved, model_item)
            self.assertIsNot(preserved, model_item)
        for unsupported in [
            dict(type="web_search_call", id="web_1", status="completed"),
            dict(type="tool_search_call", id="search_1", status="completed"),
            dict(type="reasoning", id="rs_1", summary=[], status="incomplete"),
        ]:
            with self.assertRaisesRegex(ActOpenAICompatibilityError, "^INVALID_MODEL_ITEM$"):
                preserve_act_openai_model_item(unsupported)

    def test_sync_dispatch_and_policy(self):
        with fixture() as (url, calls):
            client = Darwin(base_url=url, api_key="fixture-key", max_retries=0)
            for name, arguments in CASES:
                result = execute_act_openai_call(client, item(name, arguments), agent="acting", authorize=lambda _: True)
                self.assertEqual(result["call_id"], f"call-{name}")
                self.assertEqual(result["type"], "function_call_output")
                output = json.loads(result["output"])
                if name == "pay":
                    self.assertEqual(output["status"], "pending")
                    self.assertNotIn("receipt", output)
                if name == "send_message":
                    self.assertEqual(output["status"], "accepted")
            self.assertEqual(len(calls), len(CASES))
            self.assertEqual(calls[1]["body"]["messageContent"], "Hello")
            self.assertIn("wait=true", calls[2]["path"])
            self.assertTrue(all(call["headers"].get("x-api-key") == "fixture-key" for call in calls))
            with self.assertRaisesRegex(ActOpenAICompatibilityError, "ACT_CALL_NOT_AUTHORIZED"):
                execute_act_openai_call(client, item(*CASES[-1]), agent="acting", authorize=lambda _: False)
            self.assertEqual(len(calls), len(CASES))
            def mutate_copy(call):
                call["input"]["agent"] = "other"
                return True
            execute_act_openai_call(client, item("list_threads", {}), agent="acting", authorize=mutate_copy)
            self.assertIn("agent=acting", calls[-1]["path"])

    def test_async_dispatch(self):
        async def run():
            with fixture() as (url, calls):
                client = AsyncDarwin(base_url=url, api_key="fixture-key", max_retries=0)
                async def authorize(_):
                    return True
                for name, arguments in CASES:
                    result = await execute_act_openai_call_async(client, item(name, arguments), agent="acting", authorize=authorize)
                    self.assertEqual(result["call_id"], f"call-{name}")
                self.assertEqual(len(calls), len(CASES))
        asyncio.run(run())

    def test_errors_are_not_success_outputs(self):
        with fixture(lambda *_: (403, {"code": "FORBIDDEN"})) as (url, _):
            with self.assertRaises(ApiError):
                execute_act_openai_call(Darwin(base_url=url, max_retries=0), item("list_threads", {}), agent="acting", authorize=lambda _: True)
        with fixture(lambda *_: (200, {"threads": [], "cursor": None, "secret": "do-not-return"})) as (url, _):
            with self.assertRaisesRegex(ActOpenAICompatibilityError, "^INVALID_RESULT$"):
                execute_act_openai_call(Darwin(base_url=url, max_retries=0), item("list_threads", {}), agent="acting", authorize=lambda _: True)
