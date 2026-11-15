from pathlib import Path


repository_root = Path(__file__).resolve().parents[1]
monorepo_package_root = repository_root / "apps" / "navigator" / "api" / "python-sdk" / "src" / "darwin_sdk"
package_root = monorepo_package_root if monorepo_package_root.is_dir() else repository_root / "src" / "darwin_sdk"
required_files = (
    package_root / "__init__.py",
    package_root / "client.py",
    package_root / "environment.py",
    package_root / "act_openai.py",
    package_root / "act_openai_contract.json",
    package_root / "py.typed",
    package_root / "types" / "search_response.py",
    package_root / "types" / "start_thread_response.py",
    package_root / "types" / "get_thread_response.py",
    package_root / "types" / "send_message_body.py",
    package_root / "types" / "authenticate_response.py",
    package_root / "types" / "pay_response.py",
)

missing = [str(path) for path in required_files if not path.is_file()]
if missing:
    raise SystemExit(f"Python SDK is incomplete: {', '.join(missing)}")

project_root = package_root.parents[1] if monorepo_package_root.is_dir() else repository_root
project = (project_root / "pyproject.toml").read_text()
if '"jsonschema[format]>=4.18,<5"' not in project:
    raise SystemExit("Python SDK must declare jsonschema as a normal runtime dependency.")
if 'darwin_sdk = ["py.typed", "act_openai_contract.json"]' not in project:
    raise SystemExit("Python SDK must include the OpenAI contract as package data.")

for source_path in package_root.rglob("*.py"):
    compile(source_path.read_bytes(), str(source_path), "exec")

client_source = (package_root / "client.py").read_text()
for method in (
    "navigate",
    "get_navigate_request",
    "search",
    "start_thread",
    "get_thread",
    "list_threads",
    "send_message",
    "authenticate",
    "pay",
    "get_account",
    "list_search_history",
    "list_auth_credentials",
    "revoke_auth_credential",
    "list_target_accounts",
    "set_target_account_default",
    "revoke_target_account",
    "list_payment_methods",
    "set_payment_method_default",
    "revoke_payment_method",
):
    if f"    def {method}(" not in client_source:
        raise SystemExit(f"Python SDK is missing top-level {method}().")
    if f"    async def {method}(" not in client_source:
        raise SystemExit(f"Python SDK is missing asynchronous {method}().")
for removed in ("host", "account", "connect", "supply", "start_action", "get_action", "list_actions", "continue_action", "authenticate_session", "pay_action", "approve_action", "end_action", "get_authentication_status"):
    if f"    def {removed}(" in client_source:
        raise SystemExit(f"Python SDK still exposes {removed} on the primary client.")
environment_source = (package_root / "environment.py").read_text()
raw_client_source = (package_root / "raw_client.py").read_text()
if "https://api.darwin.so/api" not in environment_source:
    raise SystemExit("Generated Python SDK must default to the Darwin API root.")
if '"v2/search"' not in raw_client_source or '"v3/search"' not in raw_client_source:
    raise SystemExit("Generated Python SDK must expose both legacy v2 Search and adaptive v3 Search.")

search_signature = client_source.split("    def search(", 1)[1].split(") ->", 1)[0]
if "query: str" not in search_signature:
    raise SystemExit("Generated Python SDK must require one natural-language Search query.")
for field_name in ("category", "objective", "num_results"):
    if field_name not in search_signature:
        raise SystemExit(f"Generated Python Search request is missing {field_name}.")
for retired_field in (
    "filters",
    "limit",
    "include_ai_ids",
    "exclude_ai_ids",
    "include_domains",
    "exclude_domains",
    "context",
    "cursor",
):
    if f"\n        {retired_field}:" in search_signature:
        raise SystemExit(f"Generated Python Search request still exposes {retired_field}.")
for retired_selector in ("ai_id", "operation_id"):
    if f"\n        {retired_selector}:" in search_signature:
        raise SystemExit(f"Generated Python Search request still exposes {retired_selector}.")

print("Python SDK exposes the next-release thread contract plus Search and Account; no publication implied.")
