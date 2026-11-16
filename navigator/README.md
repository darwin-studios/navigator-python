# Navigator Python SDK

```sh
pip install darwin-navigator
```

```python
import os
from darwin_navigator import Navigator, AsyncNavigator
navigator = Navigator(api_key=os.environ['DARWIN_API_KEY'])
results = navigator.search(query='Find agents for research', num_results=5)
```

Navigator is a product by Darwin. This distribution uses its own
`darwin_navigator` namespace. Existing `darwin-sdk` installations and
`darwin_sdk` imports remain separately available and are not replaced.
`Darwin` and `AsyncDarwin` are also exported within this package.
OpenAI helpers are available from `darwin_navigator.openai`.
See https://darwin.so/docs/interfaces/darwin/python-sdk.
