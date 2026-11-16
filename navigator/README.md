# Navigator Python SDK

```sh
pip install darwin-navigator
```

```python
from darwin_navigator import Navigator, AsyncNavigator, SearchResponse
```

Existing `darwin-sdk` installations and `darwin_sdk` imports remain supported. Navigator re-exports the same client and model classes, preserving their identity. The established submodule namespace is `darwin_sdk`; OpenAI helpers are also available from `darwin_navigator.openai`.
