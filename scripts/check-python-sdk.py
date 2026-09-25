from pathlib import Path


package_root = Path(__file__).resolve().parents[1] / "src" / "darwin_sdk"
required_files = (
    package_root / "__init__.py",
    package_root / "client.py",
    package_root / "environment.py",
    package_root / "py.typed",
    package_root / "types" / "search_response.py",
    package_root / "types" / "act_action_response.py",
    package_root / "types" / "act_list_response.py",
    package_root / "types" / "act_pay_action_response.py",
    package_root / "types" / "authenticate_session_response.py",
    package_root / "types" / "act_end_action_response.py",
)

missing = [str(path) for path in required_files if not path.is_file()]
if missing:
    raise SystemExit(f"Python SDK is incomplete: {', '.join(missing)}")

for source_path in package_root.rglob("*.py"):
    compile(source_path.read_bytes(), str(source_path), "exec")

client_source = (package_root / "client.py").read_text()
for method in (
    "search",
    "get_account",
    "list_search_history",
    "start_action",
    "get_action",
    "list_actions",
    "continue_action",
    "authenticate_session",
    "pay_action",
    "approve_action",
    "end_action",
):
    if f"    def {method}(" not in client_source:
        raise SystemExit(f"Python SDK is missing top-level {method}().")

for removed in ("host", "account", "connect", "supply"):
    if f"    def {removed}(" in client_source:
        raise SystemExit(f"Python SDK still exposes {removed} on the primary client.")

if "https://api.darwin.so/api/v2" not in (package_root / "environment.py").read_text():
    raise SystemExit("Generated Python SDK must default to the v2 API.")

print("Python SDK exposes the live eleven-operation Search, account, and Act surface.")
