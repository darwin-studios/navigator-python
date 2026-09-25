# Darwin Python SDK

The primary client covers the same eleven live operations exposed through Darwin MCP: Search, account context, Search history, and the complete Start/Get/List/Continue/Authenticate/Pay/Approve/End Action flow. It also includes the bounded developer account, application, and API-key endpoints documented in the public OpenAPI contract.

```bash
pip install darwin-sdk
```

```python
import os

from darwin_sdk import Darwin

darwin = Darwin(api_key=os.environ["DARWIN_API_KEY"])
found = darwin.search(query="OCR that handles handwriting and tables")
outcome = darwin.start_action(
    capability_id=found.results[0].capability_id,
    capability_revision=found.results[0].capability_revision,
    inputs={"file": "https://example.com/invoice.pdf"},
    request_id="req_123",
)
```

The client is generated from Darwin's public `/api/v2` OpenAPI contract and defaults to `https://api.darwin.so/api/v2`. Treat each Action's `available_actions` and typed interaction as the mutation authority. See [the API guide](https://darwin.so/docs/surfaces/api) for authentication, payment, approval, continuation, and closure examples.
