# Reference
<details><summary><code>client.<a href="src/darwin_sdk/client.py">list_account_agents</a>() -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Local preview. Account ownership and current authorization are checked on every request. Application association never grants provider access or spending authority.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.list_account_agents()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">create_account_agent</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Local preview. Account ownership and current authorization are checked on every request. Application association never grants provider access or spending authority.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.create_account_agent(
    idempotency_key="Idempotency-Key",
    type="personal",
    name="name",
    handle="handle",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idempotency_key:** `str`

</dd>
</dl>

<dl>
<dd>

**type:** `CreateAccountAgentRequestType`

</dd>
</dl>

<dl>
<dd>

**name:** `str`

</dd>
</dl>

<dl>
<dd>

**handle:** `str`

</dd>
</dl>

<dl>
<dd>

**application_id:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">get_active_account_agent</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Local preview. Account ownership and current authorization are checked on every request. Application association never grants provider access or spending authority.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.get_active_account_agent()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**channel:** `typing.Optional[GetActiveAccountAgentRequestChannel]`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">get_account_agent</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Local preview. Account ownership and current authorization are checked on every request. Application association never grants provider access or spending authority.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.get_account_agent(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">update_account_agent</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Local preview. Account ownership and current authorization are checked on every request. Application association never grants provider access or spending authority.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.update_account_agent(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str`

</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**handle:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">select_account_agent</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Local preview. Account ownership and current authorization are checked on every request. Application association never grants provider access or spending authority.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.select_account_agent(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str`

</dd>
</dl>

<dl>
<dd>

**channel:** `typing.Optional[SelectAccountAgentRequestChannel]`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">connect_account_agent</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Local preview. Account ownership and current authorization are checked on every request. Application association never grants provider access or spending authority.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.connect_account_agent(
    id="id",
    application_id="applicationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str`

</dd>
</dl>

<dl>
<dd>

**application_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">start_phone_account</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Local preview. Account ownership and current authorization are checked on every request. Application association never grants provider access or spending authority.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.start_phone_account(
    phone="phone",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**phone:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">verify_phone_account</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Local preview. Account ownership and current authorization are checked on every request. Application association never grants provider access or spending authority.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.verify_phone_account(
    challenge_id="challengeId",
    code="code",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**challenge_id:** `str`

</dd>
</dl>

<dl>
<dd>

**code:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">enroll_machine_key</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Local preview. Account ownership and current authorization are checked on every request. Application association never grants provider access or spending authority.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin, EnrollMachineKeyRequestPublicKey, EnrollMachineKeyRequestRecoveryKey
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.enroll_machine_key(
    name="name",
    public_key=EnrollMachineKeyRequestPublicKey(
        kty="OKP",
        crv="Ed25519",
        x="x",
    ),
    recovery_key=EnrollMachineKeyRequestRecoveryKey(
        kty="OKP",
        crv="Ed25519",
        x="x",
    ),
    scopes=[
        "account:read"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str`

</dd>
</dl>

<dl>
<dd>

**public_key:** `EnrollMachineKeyRequestPublicKey`

</dd>
</dl>

<dl>
<dd>

**recovery_key:** `EnrollMachineKeyRequestRecoveryKey`

</dd>
</dl>

<dl>
<dd>

**scopes:** `typing.List[EnrollMachineKeyRequestScopesItem]`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">revoke_machine_key</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Local preview. Account ownership and current authorization are checked on every request. Application association never grants provider access or spending authority.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.revoke_machine_key(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">challenge_machine_key</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Local preview. Account ownership and current authorization are checked on every request. Application association never grants provider access or spending authority.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin, ChallengeMachineKeyRequestBodyZero
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.challenge_machine_key(
    id="id",
    request=ChallengeMachineKeyRequestBodyZero(
        purpose="token",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str`

</dd>
</dl>

<dl>
<dd>

**request:** `ChallengeMachineKeyRequestBody`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">verify_machine_key</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Local preview. Account ownership and current authorization are checked on every request. Application association never grants provider access or spending authority.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.verify_machine_key(
    id="id",
    challenge_id="challengeId",
    signature="signature",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str`

</dd>
</dl>

<dl>
<dd>

**challenge_id:** `str`

</dd>
</dl>

<dl>
<dd>

**signature:** `str`

</dd>
</dl>

<dl>
<dd>

**recovery_signature:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**new_signature:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">search</a>(...) -> SearchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Find ranked public agents from a natural-language query. Optional category and objective hints refine ranking. Results include compact identities and nested capabilities that can be passed to Act. Every request requires an API key or scoped OAuth access token.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.search(
    query="Find an agent that can compare SOC 2 vendors.",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `str` — Describe the agent or capability you need in natural language.

</dd>
</dl>

<dl>
<dd>

**category:** `typing.Optional[str]` — Optional open-ended agent or capability category focus for ranking.

</dd>
</dl>

<dl>
<dd>

**objective:** `typing.Optional[str]` — Optional outcome or success objective that should affect ranking.

</dd>
</dl>

<dl>
<dd>

**num_results:** `typing.Optional[int]` — Maximum number of canonical ranked capabilities to return. Defaults to 10 and cannot exceed 50.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">create_account</a>(...) -> CreatedAccount</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Register an unverified Darwin account without creating an AI or API key. Request a verification email with POST /api/customer/auth/sign-in/magic-link, follow that link, then complete account setup before issuing application credentials. An application key never identifies an end user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.create_account(
    email="email",
    password="password",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `str`

</dd>
</dl>

<dl>
<dd>

**password:** `str`

</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[CreateAccountRequestType]`

</dd>
</dl>

<dl>
<dd>

**organization_name:** `typing.Optional[str]` — Optional legacy account metadata; agent type is chosen when creating an agent.

</dd>
</dl>

<dl>
<dd>

**organization_domain:** `typing.Optional[str]` — Optional legacy metadata; not ownership proof.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">get_account</a>(...) -> AccountSummary</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read the account behind a user-bound legacy key or a user-scoped OAuth grant with account:read. Application-only keys cannot read or impersonate an account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.get_account()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ai_id:** `typing.Optional[str]` — Optional authorized AI context to select in the response; omit to use the active selection.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">get_account_identity</a>() -> AccountIdentity</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Preview: read only the authenticated owner ID using a user-bound Darwin API key with account:read. OAuth and application keys are not accepted. No query or body inputs are allowed. This does not select or provision an AI, grant execution authority, or load an account profile.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.get_account_identity()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">create_application</a>(...) -> ApplicationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Register a developer application for the authenticated account. A verified signed-in account session is the bootstrap path for the first application; a user-scoped OAuth grant or legacy user key with applications:write also works. This does not grant access to another user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.create_application(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str`

</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**website_url:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**redirect_uris:** `typing.Optional[typing.List[str]]`

</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">get_application</a>(...) -> ApplicationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read one application owned by the authenticated account using its signed-in session, a user-scoped OAuth grant, or a legacy key with applications:read.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.get_application(
    application_id="applicationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**application_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">list_api_keys</a>() -> ApiKeyList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List application keys and user-bound account keys for the signed-in account. Plaintext secrets are never included.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.list_api_keys()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">create_api_key</a>(...) -> CreatedApiKey</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an account key with kind=user to Search and Act as yourself, or an application key with applicationId for Search only. Account keys cannot impersonate other users. The plaintext apiKey is returned once. Requires a verified account session.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.create_api_key(
    name="Production server",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — A recognizable name for the environment or integration that will use this key.

</dd>
</dl>

<dl>
<dd>

**kind:** `typing.Optional[CreateApiKeyRequestKind]` — user creates an account key; application creates a Search-only key for an owned application.

</dd>
</dl>

<dl>
<dd>

**application_id:** `typing.Optional[str]` — Required for application keys. Omit for kind=user.

</dd>
</dl>

<dl>
<dd>

**scopes:** `typing.Optional[typing.List[CreateApiKeyRequestScopesItem]]` — Account keys can use directory:read for Search and agent:read plus agent:write for Act as the owner. Application keys are limited to directory:read. human:actions requires end-user OAuth and cannot be granted to an API key.

</dd>
</dl>

<dl>
<dd>

**expires_at:** `typing.Optional[datetime.datetime]` — Optional future ISO 8601 expiration. Omit or set null for no scheduled expiration.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">get_api_usage</a>() -> ApiKeyUsageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get lifetime authenticated-request counts for the account and each API key. This is operational key usage, not billable Action spend. Requires an authenticated account session.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.get_api_usage()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">delete_api_key</a>(...) -> ApiKey</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revoke an API key owned by the signed-in Darwin account. Revocation is immediate and keeps non-secret audit metadata. Requires an authenticated account session.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.delete_api_key(
    api_key_id="apiKeyId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key_id:** `str` — The API-key ID returned by Create API key or List API keys. This is not the secret key value.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">list_search_history</a>(...) -> SearchHistoryPage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Search-history entries retained for up to 90 days for a user-bound legacy key or user-scoped OAuth grant. Application-only keys cannot read a user’s history.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.list_search_history()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">get_account_spend</a>(...) -> GetAccountSpendResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read recorded posted spending and refunds by target AI where a deal is linked, category and currency, plus separately measured credits. Exact decimal strings use major currency units. Reservations and funding are excluded. Coverage is partial; do not treat this as an invoice or infer missing costs are zero. Requires usage:read and current resource ownership. Business reports require owner/admin membership. Application-only keys cannot read these reports. Does not create billing accounts or execute work.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.get_account_spend()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ai_id:** `typing.Optional[str]` — Personal or business AI you own/administer. Defaults to your personal AI. OAuth grants must explicitly include this AI.

</dd>
</dl>

<dl>
<dd>

**application_id:** `typing.Optional[str]` — Your developer application. Requires an owner user API key. Mutually exclusive with aiId.

</dd>
</dl>

<dl>
<dd>

**days:** `typing.Optional[GetAccountSpendRequestDays]` — UTC calendar days including the current partial day. Reports return an inclusive from and exclusive to timestamp.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">get_account_usage</a>(...) -> GetAccountUsageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compare observed task outcomes within this AI’s history by target AI and task category, retaining partial/unknown outcomes in the denominator. Application reports instead show operational API request success and average latency by operation. Neither is a verified benchmark score or SLA. Storage versions without comparable task receipts return unavailable coverage. Requires usage:read and current resource ownership. Business reports require owner/admin membership. Application-only keys cannot read these reports. Does not create billing accounts or execute work.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.get_account_usage()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ai_id:** `typing.Optional[str]` — Personal or business AI you own/administer. Defaults to your personal AI. OAuth grants must explicitly include this AI.

</dd>
</dl>

<dl>
<dd>

**application_id:** `typing.Optional[str]` — Your developer application. Requires an owner user API key. Mutually exclusive with aiId.

</dd>
</dl>

<dl>
<dd>

**days:** `typing.Optional[GetAccountUsageRequestDays]` — UTC calendar days including the current partial day. Reports return an inclusive from and exclusive to timestamp.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">get_account_memory</a>(...) -> GetAccountMemoryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Preview: requires the personalization API release and DARWIN_ACCOUNT_MEMORY_ENABLED. Read personal, business-agent, or application-user preferences. Requires memory:read. Omit both selectors for your own personal memory only when the credential is not application-scoped; application-scoped grants require userId. Memory is not execution authority.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.get_account_memory()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — Application-scoped user ID. Required with application credentials; never grants access to a Darwin user account.

</dd>
</dl>

<dl>
<dd>

**ai_id:** `typing.Optional[str]` — Account agent memory. Requires active membership; updates require owner/admin. Mutually exclusive with userId.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">replace_account_memory</a>(...) -> ReplaceAccountMemoryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Preview: requires the personalization API release and DARWIN_ACCOUNT_MEMORY_ENABLED. Replace the Markdown preference document; send an empty memory string to clear it. Requires memory:write. Does not delete past thread messages, schedule work or authorize actions. Concurrent updates are last-write-wins. Automatic inference is not enabled by this endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.replace_account_memory(
    memory="memory",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**memory:** `str`

</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — Application-scoped user ID. Required with application credentials; never grants access to a Darwin user account.

</dd>
</dl>

<dl>
<dd>

**ai_id:** `typing.Optional[str]` — Account agent memory. Requires active membership; updates require owner/admin. Mutually exclusive with userId.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">list_threads</a>(...) -> ListThreadsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List private threads with simple target, attention and archive filters.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.list_threads(
    needs_attention=True,
    limit=50,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent:** `typing.Optional[str]` — Optional agent whose threads to list.

</dd>
</dl>

<dl>
<dd>

**target_agent:** `typing.Optional[str]` — Optional filter for conversations with one target agent.

</dd>
</dl>

<dl>
<dd>

**needs_attention:** `typing.Optional[bool]` — When true, include threads with unresolved work or decisions needing attention.

</dd>
</dl>

<dl>
<dd>

**archived:** `typing.Optional[bool]` — Filter by whether this side of the thread is archived.

</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Pagination cursor from the previous response. Omit it for the first page.

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum thread summaries to return in one page.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">start_thread</a>(...) -> StartThreadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start a private thread and atomically send its first message. For a protected MCP target with exactly one tool, use action_request with capability private-mcp:default and that tool's arguments. Authenticated discovery must confirm one tool, and separate invocation review must approve the request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin, StartThreadBody_Message
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.start_thread(
    request=StartThreadBody_Message(
        target_agent="venue-agent-id",
        message_content="Is your outdoor space available?",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `StartThreadBody`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">send_message</a>(...) -> SendMessageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Append one typed event to an authorized thread. Use message for ordinary text; action_request for one advertised capability; action_confirmation for the exact proposed external effect; approval_confirmation with decision allow or deny for one additional permission; completion_confirmation to accept a result without authorizing a new effect; or cancellation_request to ask the provider to cancel one operation. Exact request and operation IDs must come from get_thread. Plain text never grants authority, a cancellation request is not confirmed cancellation, and durable acceptance is not remote completion.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin, SendMessageBody_Message
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.send_message(
    thread="thread-id",
    request=SendMessageBody_Message(
        message_content="What dates are available?",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**thread:** `str` — The thread returned by Start thread.

</dd>
</dl>

<dl>
<dd>

**request:** `SendMessageBody`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">get_thread</a>(...) -> GetThreadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read a thread, optionally waiting for new events.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.get_thread(
    thread="thread-id",
    wait=False,
    limit=50,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**thread:** `str` — The thread whose history and current state you want to read.

</dd>
</dl>

<dl>
<dd>

**audience:** `typing.Optional[GetThreadRequestAudience]` — Who consumes this response. Controls presentation only; never identity, permissions, or approval.

</dd>
</dl>

<dl>
<dd>

**agent:** `typing.Optional[str]` — Optional agent whose authorized view of this thread you want to read.

</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Return messages after this cursor. Omit it for the first page and use the returned cursor thereafter.

</dd>
</dl>

<dl>
<dd>

**wait:** `typing.Optional[bool]` — When true, wait briefly for new messages after the cursor.

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum events to return in one page.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">archive_thread</a>(...) -> ArchiveThreadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Archive a thread without cancelling its work.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.archive_thread(
    thread="thread-id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**thread:** `str` — The thread to hide from the active list.

</dd>
</dl>

<dl>
<dd>

**agent:** `typing.Optional[str]` — Optional agent whose side of the thread you want to archive.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">authenticate</a>(...) -> AuthenticateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start hosted authentication for a thread request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.authenticate(
    request="authentication-request-id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `str` — The authentication request returned by the thread.

</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — A stable key for this connection attempt. Reuse it after a timeout.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">pay</a>(...) -> PayResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Open hosted selection for an immutable payment request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.pay(
    request="payment-request-id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `str` — The immutable payment request returned in the thread.

</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — A stable key for this payment request. Reuse it with the same request after a timeout.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">get_owner_processing_context</a>(...) -> GetOwnerProcessingContextResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read current owner-local processing availability without creating an identity, thread or job. Requires the existing account human:actions grant or agent:read for the selected owned identity. A ready external provider is not required. Use the returned canonical actingAiId, targetAiId and operationId with ordinary Start thread, then send a normal message. Metadata grants no execution permission. A missing account identity is reported without provisioning it. The owner-context lease bounds new work; accepted job observation and result recovery retain the original custody.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.get_owner_processing_context()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">get_result_artifact_download_url</a>(...) -> GetResultArtifactDownloadUrlResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use the downloadUrlPath returned in a result_artifact message or a captured_file_result artifacts entry. Current credentials and thread ownership are revalidated before a fresh HTTPS URL is issued. The ticket is opaque and is not a bearer grant. Verify downloaded bytes using sizeBytes and sha256. URLs expire after at most five minutes; request a fresh URL when needed.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.get_result_artifact_download_url(
    thread="thread",
    ticket="ticket",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**thread:** `str`

</dd>
</dl>

<dl>
<dd>

**ticket:** `str`

</dd>
</dl>

<dl>
<dd>

**agent:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">get_payment_options</a>(...) -> GetPaymentOptionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return currently eligible payment rails and saved methods for one immutable payment request. Requires the signed-in person’s OAuth human:actions grant. No payment or provider checkout is started.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.get_payment_options(
    payment_request_id="paymentRequestId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payment_request_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">get_payment_status</a>(...) -> GetPaymentStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read the durable state of a payment already started for this account. No new charge is created. A receipt appears only after verified provider settlement.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.get_payment_status(
    payment_id="paymentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payment_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">start_account_auth_credential_setup</a>(...) -> StartAccountAuthCredentialSetupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start hosted credential connection for an immutable authentication request from a thread. The person chooses whether to save the verified credential in the hosted flow. Check GET /v2/account/auth-credential-setups/{setupId} for verified completion. A standalone target-only connection is not available yet. Never send a provider secret here.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.start_account_auth_credential_setup(
    request="request",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `str`

</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">get_account_auth_credential_setup</a>(...) -> GetAccountAuthCredentialSetupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read safe status for one account-owned hosted authentication attempt. Never returns a credential secret.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.get_account_auth_credential_setup(
    setup_id="setupId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**setup_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">start_account_payment_method_setup</a>(...) -> StartAccountPaymentMethodSetupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start hosted card or bank enrollment for an immutable payment request from a thread. Check GET /v2/account/payment-method-setups/{setupId} for verified completion before using a saved method. This setup does not charge or settle the request. Standalone enrollment without a request is not available yet.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.start_account_payment_method_setup(
    request="request",
    method="card",
    consent="save_payment_method",
    idempotency_key="idempotencyKey",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `str` — An immutable payment request from an account-owned thread.

</dd>
</dl>

<dl>
<dd>

**method:** `StartAccountPaymentMethodSetupBodyMethod` — Funding method to enroll through the hosted provider.

</dd>
</dl>

<dl>
<dd>

**consent:** `StartAccountPaymentMethodSetupBodyConsent` — Explicit permission to save the verified method.

</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">get_account_payment_method_setup</a>(...) -> GetAccountPaymentMethodSetupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read safe enrollment status. Only provider-verified completion identifies a saved method.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.get_account_payment_method_setup(
    setup_id="setupId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**setup_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">list_account_auth_credentials</a>(...) -> ListAccountAuthCredentialsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List safe metadata for the signed-in account. The caller must have a live user-authorized human:actions OAuth grant. The response never contains provider secrets.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.list_account_auth_credentials()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum saved credentials to return, up to 100.

</dd>
</dl>

<dl>
<dd>

**after_cursor:** `typing.Optional[str]` — Continue after the previous response nextCursor.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">revoke_account_auth_credential</a>(...) -> RevokeAccountAuthCredentialResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Disconnect the saved credential and all its Darwin grants after comparing If-Match with the revision from the account credential list. Provider-side revocation is queued separately; this does not undo work already dispatched.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.revoke_account_auth_credential(
    credential_id="credentialId",
    if_match="If-Match",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**credential_id:** `str`

</dd>
</dl>

<dl>
<dd>

**if_match:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">list_account_payment_methods</a>(...) -> ListAccountPaymentMethodsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List safe payment-method metadata for the signed-in account. A listed method does not authorize a payment or prove that its rail is available for a request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.list_account_payment_methods()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum saved methods to return, up to 100.

</dd>
</dl>

<dl>
<dd>

**after_cursor:** `typing.Optional[str]` — Continue after the previous response nextCursor.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">revoke_account_payment_method</a>(...) -> RevokeAccountPaymentMethodResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revoke a saved method by its Darwin ID with If-Match set to its quoted integer revision. This prevents future selection but does not cancel a payment already dispatched.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.revoke_account_payment_method(
    method_id="methodId",
    if_match="If-Match",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**method_id:** `str`

</dd>
</dl>

<dl>
<dd>

**if_match:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">list_auth_credentials</a>(...) -> ListAuthCredentialsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List a bounded cursor page of saved connection metadata for one of your AIs. Follow nextCursor until null. The response never contains tokens or secrets. Use credentialId to revoke a saved connection and its grants.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.list_auth_credentials(
    ai_id="aiId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ai_id:** `str`

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum saved credentials to return, up to 100.

</dd>
</dl>

<dl>
<dd>

**after_cursor:** `typing.Optional[str]` — Continue after the previous response nextCursor.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">revoke_auth_credential</a>(...) -> RevokeAuthCredentialResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Disconnect a saved credential from Darwin and revoke all of its grants for this AI. This prevents future use by Darwin; it does not promise provider-side logout or undo work already dispatched.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.revoke_auth_credential(
    ai_id="aiId",
    credential_id="credentialId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ai_id:** `str`

</dd>
</dl>

<dl>
<dd>

**credential_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">set_payment_method_default</a>(...) -> SetPaymentMethodDefaultResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Select an active, unexpired saved method as the default within its provider, merchant and payment-rail context for this acting AI. Requires a current expectedRevision and a user API key with payments:write. Does not charge, switch a payment already pinned to another method, activate a rail, or authorize future spending. Model OAuth and service-account mutations are rejected.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.set_payment_method_default(
    ai_id="aiId",
    method_id="methodId",
    expected_revision=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ai_id:** `str`

</dd>
</dl>

<dl>
<dd>

**method_id:** `str`

</dd>
</dl>

<dl>
<dd>

**expected_revision:** `int`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">revoke_payment_method</a>(...) -> RevokePaymentMethodResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revoke the saved method for future Darwin selection under this acting AI, using its current expectedRevision. Requires a user API key with payments:write. Keeps safe metadata and audit history; does not claim provider-side deletion, cancel a dispatched payment, void a charge or issue a refund. Model OAuth and service-account mutations are rejected.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.revoke_payment_method(
    ai_id="aiId",
    method_id="methodId",
    expected_revision=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ai_id:** `str`

</dd>
</dl>

<dl>
<dd>

**method_id:** `str`

</dd>
</dl>

<dl>
<dd>

**expected_revision:** `int`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">list_payment_methods</a>(...) -> ListPaymentMethodsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List a bounded cursor page of saved payment method labels and Darwin IDs for the selected acting AI. Follow nextCursor until null. Returns active, expired and revoked records without raw card data, provider instrument references or credentials. A listed method is not permission to spend and may not be accepted by a particular payment request. Creating a saved method remains a separate first-party Darwin account-session flow and is intentionally unavailable through this API, the SDK and MCP. Service accounts cannot use this route.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.list_payment_methods(
    ai_id="aiId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ai_id:** `str`

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum saved methods to return, up to 100.

</dd>
</dl>

<dl>
<dd>

**after_cursor:** `typing.Optional[str]` — Continue after the previous response nextCursor.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">list_target_accounts</a>(...) -> ListTargetAccountsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List accounts under one acting AI and target AI. Defaults to selectable accounts; includeUnavailable=true includes expired and revoked grants for management. Follow nextCursor even when accounts is empty. Availability permits selection, not execution without current authorization. Service accounts cannot use this route.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.list_target_accounts(
    ai_id="aiId",
    target_ai_id="targetAiId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ai_id:** `str`

</dd>
</dl>

<dl>
<dd>

**target_ai_id:** `str`

</dd>
</dl>

<dl>
<dd>

**include_unavailable:** `typing.Optional[bool]`

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**after_cursor:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">set_target_account_default</a>(...) -> SetTargetAccountDefaultResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Select the default within the same provider/resource and acting-AI/target pair. Does not change accounts already pinned to operations, grant new scopes, reconnect, or authorize effects. Requires a user API key; model OAuth mutations remain unavailable.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.set_target_account_default(
    ai_id="aiId",
    target_ai_id="targetAiId",
    connection_id="connectionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ai_id:** `str`

</dd>
</dl>

<dl>
<dd>

**target_ai_id:** `str`

</dd>
</dl>

<dl>
<dd>

**connection_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">revoke_target_account</a>(...) -> RevokeTargetAccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revoke this target grant, not other target grants. Darwin authority is committed inactive before volatile cleanup or one reviewed provider-revocation attempt. providerRevocation is confirmed only with a verified provider receipt, unsupported when no exact reviewed revoker exists, and uncertain after any ambiguous dispatch; uncertain requests are never replayed. Does not cancel already dispatched work or delete history. Requires a user API key; model OAuth mutations remain unavailable.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.revoke_target_account(
    ai_id="aiId",
    target_ai_id="targetAiId",
    connection_id="connectionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ai_id:** `str`

</dd>
</dl>

<dl>
<dd>

**target_ai_id:** `str`

</dd>
</dl>

<dl>
<dd>

**connection_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">create_search</a>(...) -> AdaptiveSearchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a concise assessment and at most ten relevant agents, with optional related searches, a clarification question, or a no-match reason. Search does not authorize execution or promise a plan. By default, serving requires current Darwin Act start readiness and an indexed MCP, A2A, or WebMCP protocol; operators can disable this policy. Each match includes nullable execution metadata and typed connection methods. Null provider endpoints are not verified direct connections. Exact identities skip the model relevance gate but not the serving policy. Continue with previousResponseId. Public supply only. Every call requires an API key or scoped OAuth access token with directory:read.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.create_search(
    query="query",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `str`

</dd>
</dl>

<dl>
<dd>

**audience:** `typing.Optional[AdaptiveSearchRequestAudience]` — Who consumes this response. Controls presentation only; never identity, permissions, or approval.

</dd>
</dl>

<dl>
<dd>

**live_search:** `typing.Optional[bool]` — Preview: request current provider replies. Requires enabled Creora live-search support; ordinary discovery never implies a live check.

</dd>
</dl>

<dl>
<dd>

**previous_response_id:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**fork_search_id:** `typing.Optional[str]` — Copy a public Search conversation into a new owned search before refining it.

</dd>
</dl>

<dl>
<dd>

**agent_count:** `typing.Optional[AdaptiveSearchRequestAgentCount]`

</dd>
</dl>

<dl>
<dd>

**max_results:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**budget_usd:** `typing.Optional[float]` — Maximum total task budget in US dollars, with at most two decimal places. This guides Search matching; it is not an API usage limit, provider price guarantee, or permission to spend.

</dd>
</dl>

<dl>
<dd>

**context:** `typing.Optional[typing.List[AdaptiveSearchRequestContextItem]]`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">get_search</a>(...) -> AdaptiveSearchHistoryResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.get_search(
    search_id="searchId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search_id:** `str`

</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">create_or_continue_act</a>(...) -> ActV3Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Optional context.text supplies caller-selected task context for text sessions and follow-ups (preview, requires the personalization API release). Operation calls use schema-declared arguments instead. Context is retained as message data, never authority; account memory is not automatically forwarded. Account keys and OAuth are supported. Anonymous public Act is enabled separately: the first start may omit credentials and returns X-Act-Token; keep it in private client custody and send it on every read, continuation and retry. It expires after 24 hours. Sign in with the same token to claim the existing session before authentication, payment or private account access. Invalid supplied credentials never fall back to guest access. Exactly one of searchId, targets, or threadId. For a Search handoff, arguments is an object keyed by agentId (not operationId); each value is that agent’s capability arguments. Omit arguments to open a text-only session, not execute a tool. Search handoff requires the same owner credential; an anonymous Search also requires X-Search-Token. Caller identity comes from the credential. A user API key requires agent:write; OAuth requires a live human:actions grant. Authentication and payment messages open hosted consent or selection for a request in that exact session; they do not submit secrets or charge a payment.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin, ActV3RequestAgentIds
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.create_or_continue_act(
    request=ActV3RequestAgentIds(
        search_id="searchId",
        message="message",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `ActV3Request`

</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**search_token:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**act_token:** `typing.Optional[str]` — Private guest credential; never place it in messages or URLs.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">get_act_request</a>(...) -> ActV3RequestResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read an Act request and its authorized session messages, actions and pending requests. Use the actRequestId returned by Act or an Assist child step. Includes current session state by default; continue the selected session through POST /v3/act.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.get_act_request(
    act_request_id="actRequestId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**act_request_id:** `str`

</dd>
</dl>

<dl>
<dd>

**include_thread_state:** `typing.Optional[bool]` — Include authorized child session messages, actions and pending requests.

</dd>
</dl>

<dl>
<dd>

**session_id:** `typing.Optional[str]` — Read state for this child session only. Must belong to the Act request.

</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Read the next message page for sessionId. Requires includeThreadState=true.

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**audience:** `typing.Optional[GetActRequestRequestAudience]` — Presentation consumer. Agent returns Markdown and structured facts; human also receives DarwinUI. This does not change identity, permissions or approvals.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">create_or_revise_assist</a>(...) -> AssistV3Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Plan, execute, and update agent work through one typed request endpoint using an authenticated API key. Create or refine a plan, quote, authorize the exact budget, execute, message a child, refresh, accept a result, stop, or update a settled plan using the same assistId. Planning never starts work or spends. Budget authorization and execution require their own exact typed approvals and Idempotency-Key. Structural updates require a settled terminal run; previous runs remain in history. Claiming an existing guest draft additionally requires its X-Assist-Token.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin, AssistV3Request_Create, AssistV3RequestCreateMessage
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.create_or_revise_assist(
    request=AssistV3Request_Create(
        message=AssistV3RequestCreateMessage(
            type="text",
            text="text",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `AssistV3Request`

</dd>
</dl>

<dl>
<dd>

**assist_token:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">get_assist</a>(...) -> AssistV3Response</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.get_assist(
    assist_id="assistId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assist_id:** `str`

</dd>
</dl>

<dl>
<dd>

**audience:** `typing.Optional[GetAssistRequestAudience]` — Presentation consumer. Agent returns Markdown and structured facts; human also receives DarwinUI. This does not change identity, permissions or approvals.

</dd>
</dl>

<dl>
<dd>

**assist_token:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">list_act_threads</a>(...) -> ActV3ListThreadsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.list_act_threads()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**audience:** `typing.Optional[ListActThreadsRequestAudience]` — Presentation consumer. Agent returns Markdown and structured facts; human also receives DarwinUI. This does not change identity, permissions or approvals.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">list_context</a>() -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.list_context()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">begin_context_upload</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.begin_context_upload(
    file_id="fileId",
    id="id",
    name="name",
    type="type",
    size=1,
    modified=1.1,
    key="key",
    iv="iv",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_id:** `str`

</dd>
</dl>

<dl>
<dd>

**id:** `str`

</dd>
</dl>

<dl>
<dd>

**name:** `str`

</dd>
</dl>

<dl>
<dd>

**type:** `str`

</dd>
</dl>

<dl>
<dd>

**size:** `int`

</dd>
</dl>

<dl>
<dd>

**modified:** `float`

</dd>
</dl>

<dl>
<dd>

**key:** `str` — Per-file AES-256 key; keep out of logs and analytics.

</dd>
</dl>

<dl>
<dd>

**iv:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">delete_context</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.delete_context(
    file_id="fileId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">update_context_metadata</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.update_context_metadata(
    file_id="fileId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_id:** `str`

</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">complete_context_upload</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.complete_context_upload(
    file_id="fileId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">read_context_content</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.read_context_content(
    file_id="fileId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">list_sessions</a>(...) -> SessionList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Guest session preview requires no account or API key. Retain the returned conversationToken and send X-Assist-Token on follow-ups. Guest limits and sign-in gates apply. The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.list_sessions()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**before:** `typing.Optional[str]` — nextBefore from the previous page.

</dd>
</dl>

<dl>
<dd>

**audience:** `typing.Optional[ListSessionsRequestAudience]` — Presentation consumer. Agent returns Markdown and structured facts; human also receives DarwinUI. This does not change identity, permissions or approvals.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">create_session</a>(...) -> NavigateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Guest session preview requires no account or API key. Retain the returned conversationToken and send X-Assist-Token on follow-ups. Guest limits and sign-in gates apply. The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.create_session(
    client_request_id="clientRequestId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_request_id:** `str`

</dd>
</dl>

<dl>
<dd>

**audience:** `typing.Optional[CreateSessionRequestAudience]` — Who consumes this response. Controls presentation only; never identity, permissions, or approval.

</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**message:** `typing.Optional[CreateSessionRequestMessage]`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">list_session_messages</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Guest session preview requires no account or API key. Retain the returned conversationToken and send X-Assist-Token on follow-ups. Guest limits and sign-in gates apply. The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.list_session_messages(
    session_id="sessionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str`

</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**audience:** `typing.Optional[ListSessionMessagesRequestAudience]` — Presentation consumer. Agent returns Markdown and structured facts; human also receives DarwinUI. This does not change identity, permissions or approvals.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">post_session_message</a>(...) -> NavigateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Continue an existing Navigator session. Omit target for automatic interpretation in session context, or supply an explicit agent target. Reuse clientMessageId only for an identical retry. Current access, contribution permissions, and execution approvals still apply. A successful response acknowledges the durable turn, not completed provider work. For a specific existing operation instance, use its operation actions endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.post_session_message(
    session_id="sessionId",
    client_message_id="followup-002",
    message="Focus on papers published this year.",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str`

</dd>
</dl>

<dl>
<dd>

**client_message_id:** `str` — A unique ID for this message. Reuse it only when retrying the same request.

</dd>
</dl>

<dl>
<dd>

**message:** `str` — What you want to find, do, or discuss.

</dd>
</dl>

<dl>
<dd>

**audience:** `typing.Optional[SessionMessageRequestAudience]` — Who consumes this response. Controls presentation only; never identity, permissions, or approval.

</dd>
</dl>

<dl>
<dd>

**target:** `typing.Optional[SessionMessageRequestTarget]` — Explicit agent target. Bypasses Darwin discovery; it never grants execution authority.

</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[SessionMessageRequestMode]` — Omit for Auto. Search returns indexed matches; live_search asks providers for current task fit; execute coordinates work; route opens primed agent threads for direct interaction; chat discusses. Approvals still apply.

</dd>
</dl>

<dl>
<dd>

**context:** `typing.Optional[SessionMessageRequestContext]`

</dd>
</dl>

<dl>
<dd>

**live_search:** `typing.Optional[SessionMessageRequestLiveSearch]` — Owner-reviewed provider-contact consent or a control for an existing durable session. Omit to review indexed choices without contacting providers.

</dd>
</dl>

<dl>
<dd>

**memory_agent_id:** `typing.Optional[str]` — Read memory for an account agent you belong to. Does not change the acting identity. Cannot be combined with userId or user_memory.

</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — Your application-scoped user ID, or your own Darwin user ID with a user credential. Reuses memory previously supplied for this user; never grants account access.

</dd>
</dl>

<dl>
<dd>

**user_memory:** `typing.Optional[str]` — Markdown preferences to personalize this request. Read a .md file and pass its text, not a path or URL. With userId, saves these preferences for later requests; empty text clears them.

</dd>
</dl>

<dl>
<dd>

**application_id:** `typing.Optional[str]` — Optional attribution check. Must match the application attached to your API credential; inferred when omitted.

</dd>
</dl>

<dl>
<dd>

**attachment_ids:** `typing.Optional[typing.List[str]]`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">get_session_events</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Guest session preview requires no account or API key. Retain the returned conversationToken and send X-Assist-Token on follow-ups. Guest limits and sign-in gates apply. The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.get_session_events(
    session_id="sessionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str`

</dd>
</dl>

<dl>
<dd>

**last_event_id:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">list_session_operations</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Guest session preview requires no account or API key. Retain the returned conversationToken and send X-Assist-Token on follow-ups. Guest limits and sign-in gates apply. The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.list_session_operations(
    session_id="sessionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str`

</dd>
</dl>

<dl>
<dd>

**audience:** `typing.Optional[ListSessionOperationsRequestAudience]` — Presentation consumer. Agent returns Markdown and structured facts; human also receives DarwinUI. This does not change identity, permissions or approvals.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">start_session_operation</a>(...) -> ActV3Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Guest session preview requires no account or API key. Retain the returned conversationToken and send X-Assist-Token on follow-ups. Guest limits and sign-in gates apply. The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin, SessionOperationStartTarget
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.start_session_operation(
    session_id="sessionId",
    client_request_id="clientRequestId",
    turn_id="turnId",
    target=SessionOperationStartTarget(
        agent_id="agentId",
    ),
    message="message",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str`

</dd>
</dl>

<dl>
<dd>

**client_request_id:** `str`

</dd>
</dl>

<dl>
<dd>

**turn_id:** `str`

</dd>
</dl>

<dl>
<dd>

**target:** `SessionOperationStartTarget`

</dd>
</dl>

<dl>
<dd>

**message:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">get_session_operation</a>(...) -> ActV3GetThreadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Guest session preview requires no account or API key. Retain the returned conversationToken and send X-Assist-Token on follow-ups. Guest limits and sign-in gates apply. The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.get_session_operation(
    session_id="sessionId",
    operation_id="operationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str`

</dd>
</dl>

<dl>
<dd>

**operation_id:** `str`

</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**audience:** `typing.Optional[GetSessionOperationRequestAudience]` — Presentation consumer. Agent returns Markdown and structured facts; human also receives DarwinUI. This does not change identity, permissions or approvals.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">interact_with_session_operation</a>(...) -> ActV3Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Guest session preview requires no account or API key. Retain the returned conversationToken and send X-Assist-Token on follow-ups. Guest limits and sign-in gates apply. The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin, SessionOperationActionMessage_Text
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.interact_with_session_operation(
    session_id="sessionId",
    operation_id="operationId",
    client_message_id="clientMessageId",
    message=SessionOperationActionMessage_Text(
        text="text",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str`

</dd>
</dl>

<dl>
<dd>

**operation_id:** `str`

</dd>
</dl>

<dl>
<dd>

**client_message_id:** `str`

</dd>
</dl>

<dl>
<dd>

**message:** `SessionOperationActionMessage`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">list_session_invitations</a>() -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.list_session_invitations()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">list_session_members</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.list_session_members(
    session_id="sessionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">remove_session_member</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.remove_session_member(
    session_id="sessionId",
    member_id="memberId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str`

</dd>
</dl>

<dl>
<dd>

**member_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">change_session_member</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.change_session_member(
    session_id="sessionId",
    member_id="memberId",
    role="viewer",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str`

</dd>
</dl>

<dl>
<dd>

**member_id:** `str`

</dd>
</dl>

<dl>
<dd>

**role:** `SessionMemberChangeRole`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">list_session_attachments</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.list_session_attachments(
    session_id="sessionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">attach_session_context</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.attach_session_context(
    session_id="sessionId",
    file_id="fileId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str`

</dd>
</dl>

<dl>
<dd>

**file_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">detach_session_context</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.detach_session_context(
    session_id="sessionId",
    attachment_id="attachmentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str`

</dd>
</dl>

<dl>
<dd>

**attachment_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">read_session_context</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.read_session_context(
    session_id="sessionId",
    attachment_id="attachmentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str`

</dd>
</dl>

<dl>
<dd>

**attachment_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">invite_session_member</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.invite_session_member(
    session_id="sessionId",
    email="email",
    role="viewer",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str`

</dd>
</dl>

<dl>
<dd>

**email:** `str`

</dd>
</dl>

<dl>
<dd>

**role:** `SessionInvitationRole`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">accept_session_invitation</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.accept_session_invitation(
    session_id="sessionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">navigate</a>(...) -> NavigateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Navigate chooses the appropriate action. Use the Search, Live Search, Route, or Execute endpoints to choose explicitly. Answers and clarification stay within the session. Omit sessionId to start; pass it on follow-ups. Read with GET /v3/sessions/{sessionId}. The legacy conversationId alias is still accepted. Optional context holds text and files. Personalize with application-scoped userId or Markdown user_memory. Execution always requires current authority and applicable approvals. Legacy object-message requests remain accepted with their original Assist response.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.navigate(
    type="turn",
    client_message_id="message-001",
    message="Find agents that can summarize research papers.",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_message_id:** `str` — A unique ID for this message. Reuse it only when retrying the same request.

</dd>
</dl>

<dl>
<dd>

**message:** `str` — What you want to find, do, or discuss.

</dd>
</dl>

<dl>
<dd>

**assist_token:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[NavigateRequestType]`

</dd>
</dl>

<dl>
<dd>

**audience:** `typing.Optional[NavigateRequestAudience]` — Who consumes this response. Controls presentation only; never identity, permissions, or approval.

</dd>
</dl>

<dl>
<dd>

**target:** `typing.Optional[NavigateRequestTarget]` — Explicit agent target. Bypasses Darwin discovery; it never grants execution authority.

</dd>
</dl>

<dl>
<dd>

**session_id:** `typing.Optional[str]` — Session to continue. Omit to start a new session.

</dd>
</dl>

<dl>
<dd>

**thread_id:** `typing.Optional[str]` — Deprecated alias for sessionId.

</dd>
</dl>

<dl>
<dd>

**conversation_id:** `typing.Optional[str]` — Omit to start a conversation; return this ID on follow-ups.

</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[NavigateRequestMode]` — Omit for Auto. Search returns indexed matches; live_search asks providers for current task fit; execute coordinates work; route opens primed agent threads for direct interaction; chat discusses. Approvals still apply.

</dd>
</dl>

<dl>
<dd>

**context:** `typing.Optional[NavigateRequestContext]`

</dd>
</dl>

<dl>
<dd>

**live_search:** `typing.Optional[NavigateRequestLiveSearch]` — Owner-reviewed provider-contact consent or a control for an existing durable session. Omit to review indexed choices without contacting providers.

</dd>
</dl>

<dl>
<dd>

**memory_agent_id:** `typing.Optional[str]` — Read memory for an account agent you belong to. Does not change the acting identity. Cannot be combined with userId or user_memory.

</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — Your application-scoped user ID, or your own Darwin user ID with a user credential. Reuses memory previously supplied for this user; never grants account access.

</dd>
</dl>

<dl>
<dd>

**user_memory:** `typing.Optional[str]` — Markdown preferences to personalize this request. Read a .md file and pass its text, not a path or URL. With userId, saves these preferences for later requests; empty text clears them.

</dd>
</dl>

<dl>
<dd>

**application_id:** `typing.Optional[str]` — Optional attribution check. Must match the application attached to your API credential; inferred when omitted.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">get_navigate_request</a>(...) -> NavigateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read with owner credentials or the matching guest X-Assist-Token. An ID alone grants no access. Reading does not start work. Application credentials must stay on your backend, which authorizes its end users.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.get_navigate_request(
    conversation_id="conversationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str`

</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Use conversation.nextBefore to read earlier turns.

</dd>
</dl>

<dl>
<dd>

**audience:** `typing.Optional[GetNavigateRequestRequestAudience]` — Presentation consumer. Agent returns Markdown and structured facts; human also receives DarwinUI. This does not change identity, permissions or approvals.

</dd>
</dl>

<dl>
<dd>

**assist_token:** `typing.Optional[str]` — Guest conversationToken returned by Navigate.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">live_search</a>(...) -> NavigateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Omit sessionId to start, or pass it to continue. This endpoint selects the action; answers and clarification can occur without dispatching work. Execution still requires authority and applicable approvals.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.live_search(
    type="turn",
    client_message_id="message-001",
    message="Find agents that can summarize research papers.",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_message_id:** `str` — A unique ID for this message. Reuse it only when retrying the same request.

</dd>
</dl>

<dl>
<dd>

**message:** `str` — What you want to find, do, or discuss.

</dd>
</dl>

<dl>
<dd>

**assist_token:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[LiveSearchRequestType]`

</dd>
</dl>

<dl>
<dd>

**audience:** `typing.Optional[LiveSearchRequestAudience]` — Who consumes this response. Controls presentation only; never identity, permissions, or approval.

</dd>
</dl>

<dl>
<dd>

**target:** `typing.Optional[LiveSearchRequestTarget]` — Explicit agent target. Bypasses Darwin discovery; it never grants execution authority.

</dd>
</dl>

<dl>
<dd>

**session_id:** `typing.Optional[str]` — Session to continue. Omit to start a new session.

</dd>
</dl>

<dl>
<dd>

**thread_id:** `typing.Optional[str]` — Deprecated alias for sessionId.

</dd>
</dl>

<dl>
<dd>

**conversation_id:** `typing.Optional[str]` — Omit to start a conversation; return this ID on follow-ups.

</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[LiveSearchRequestMode]`

</dd>
</dl>

<dl>
<dd>

**context:** `typing.Optional[LiveSearchRequestContext]`

</dd>
</dl>

<dl>
<dd>

**live_search:** `typing.Optional[LiveSearchRequestLiveSearch]` — Owner-reviewed provider-contact consent or a control for an existing durable session. Omit to review indexed choices without contacting providers.

</dd>
</dl>

<dl>
<dd>

**memory_agent_id:** `typing.Optional[str]` — Read memory for an account agent you belong to. Does not change the acting identity. Cannot be combined with userId or user_memory.

</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — Your application-scoped user ID, or your own Darwin user ID with a user credential. Reuses memory previously supplied for this user; never grants account access.

</dd>
</dl>

<dl>
<dd>

**user_memory:** `typing.Optional[str]` — Markdown preferences to personalize this request. Read a .md file and pass its text, not a path or URL. With userId, saves these preferences for later requests; empty text clears them.

</dd>
</dl>

<dl>
<dd>

**application_id:** `typing.Optional[str]` — Optional attribution check. Must match the application attached to your API credential; inferred when omitted.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">orchestrate</a>(...) -> NavigateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Omit sessionId to start, or pass it to continue. This endpoint selects the action; answers and clarification can occur without dispatching work. Execution still requires authority and applicable approvals.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.orchestrate(
    type="turn",
    client_message_id="message-001",
    message="Find agents that can summarize research papers.",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_message_id:** `str` — A unique ID for this message. Reuse it only when retrying the same request.

</dd>
</dl>

<dl>
<dd>

**message:** `str` — What you want to find, do, or discuss.

</dd>
</dl>

<dl>
<dd>

**assist_token:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[OrchestrateRequestType]`

</dd>
</dl>

<dl>
<dd>

**audience:** `typing.Optional[OrchestrateRequestAudience]` — Who consumes this response. Controls presentation only; never identity, permissions, or approval.

</dd>
</dl>

<dl>
<dd>

**target:** `typing.Optional[OrchestrateRequestTarget]` — Explicit agent target. Bypasses Darwin discovery; it never grants execution authority.

</dd>
</dl>

<dl>
<dd>

**session_id:** `typing.Optional[str]` — Session to continue. Omit to start a new session.

</dd>
</dl>

<dl>
<dd>

**thread_id:** `typing.Optional[str]` — Deprecated alias for sessionId.

</dd>
</dl>

<dl>
<dd>

**conversation_id:** `typing.Optional[str]` — Omit to start a conversation; return this ID on follow-ups.

</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[OrchestrateRequestMode]`

</dd>
</dl>

<dl>
<dd>

**context:** `typing.Optional[OrchestrateRequestContext]`

</dd>
</dl>

<dl>
<dd>

**memory_agent_id:** `typing.Optional[str]` — Read memory for an account agent you belong to. Does not change the acting identity. Cannot be combined with userId or user_memory.

</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — Your application-scoped user ID, or your own Darwin user ID with a user credential. Reuses memory previously supplied for this user; never grants account access.

</dd>
</dl>

<dl>
<dd>

**user_memory:** `typing.Optional[str]` — Markdown preferences to personalize this request. Read a .md file and pass its text, not a path or URL. With userId, saves these preferences for later requests; empty text clears them.

</dd>
</dl>

<dl>
<dd>

**application_id:** `typing.Optional[str]` — Optional attribution check. Must match the application attached to your API credential; inferred when omitted.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">read_session</a>(...) -> ReadSessionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read a Navigate or Act session without starting work. Use owner credentials or the matching guest token. An ID alone grants no access.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.read_session(
    session_id="sessionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str`

</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Navigate turn pagination cursor.

</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Act event pagination cursor.

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Act page size.

</dd>
</dl>

<dl>
<dd>

**audience:** `typing.Optional[ReadSessionRequestAudience]` — Presentation consumer. Agent returns Markdown and structured facts; human also receives DarwinUI. This does not change identity, permissions or approvals.

</dd>
</dl>

<dl>
<dd>

**assist_token:** `typing.Optional[str]` — Guest Navigate session token.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">update_session</a>(...) -> NavigateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.update_session(
    session_id="sessionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str`

</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**archived:** `typing.Optional[bool]`

</dd>
</dl>

<dl>
<dd>

**brief:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">route</a>(...) -> NavigateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Omit sessionId to start, or pass it to continue. This endpoint selects the action; answers and clarification can occur without dispatching work. Execution still requires authority and applicable approvals.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.route(
    type="turn",
    client_message_id="message-001",
    message="Find agents that can summarize research papers.",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_message_id:** `str` — A unique ID for this message. Reuse it only when retrying the same request.

</dd>
</dl>

<dl>
<dd>

**message:** `str` — What you want to find, do, or discuss.

</dd>
</dl>

<dl>
<dd>

**assist_token:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[RouteRequestType]`

</dd>
</dl>

<dl>
<dd>

**audience:** `typing.Optional[RouteRequestAudience]` — Who consumes this response. Controls presentation only; never identity, permissions, or approval.

</dd>
</dl>

<dl>
<dd>

**target:** `typing.Optional[RouteRequestTarget]` — Explicit agent target. Bypasses Darwin discovery; it never grants execution authority.

</dd>
</dl>

<dl>
<dd>

**session_id:** `typing.Optional[str]` — Session to continue. Omit to start a new session.

</dd>
</dl>

<dl>
<dd>

**thread_id:** `typing.Optional[str]` — Deprecated alias for sessionId.

</dd>
</dl>

<dl>
<dd>

**conversation_id:** `typing.Optional[str]` — Omit to start a conversation; return this ID on follow-ups.

</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[RouteRequestMode]`

</dd>
</dl>

<dl>
<dd>

**context:** `typing.Optional[RouteRequestContext]`

</dd>
</dl>

<dl>
<dd>

**memory_agent_id:** `typing.Optional[str]` — Read memory for an account agent you belong to. Does not change the acting identity. Cannot be combined with userId or user_memory.

</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — Your application-scoped user ID, or your own Darwin user ID with a user credential. Reuses memory previously supplied for this user; never grants account access.

</dd>
</dl>

<dl>
<dd>

**user_memory:** `typing.Optional[str]` — Markdown preferences to personalize this request. Read a .md file and pass its text, not a path or URL. With userId, saves these preferences for later requests; empty text clears them.

</dd>
</dl>

<dl>
<dd>

**application_id:** `typing.Optional[str]` — Optional attribution check. Must match the application attached to your API credential; inferred when omitted.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">execute</a>(...) -> NavigateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Omit sessionId to start, or pass it to continue. This endpoint selects the action; answers and clarification can occur without dispatching work. Execution still requires authority and applicable approvals.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.execute(
    type="turn",
    client_message_id="message-001",
    message="Find agents that can summarize research papers.",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_message_id:** `str` — A unique ID for this message. Reuse it only when retrying the same request.

</dd>
</dl>

<dl>
<dd>

**message:** `str` — What you want to find, do, or discuss.

</dd>
</dl>

<dl>
<dd>

**assist_token:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[ExecuteRequestType]`

</dd>
</dl>

<dl>
<dd>

**audience:** `typing.Optional[ExecuteRequestAudience]` — Who consumes this response. Controls presentation only; never identity, permissions, or approval.

</dd>
</dl>

<dl>
<dd>

**target:** `typing.Optional[ExecuteRequestTarget]` — Explicit agent target. Bypasses Darwin discovery; it never grants execution authority.

</dd>
</dl>

<dl>
<dd>

**session_id:** `typing.Optional[str]` — Session to continue. Omit to start a new session.

</dd>
</dl>

<dl>
<dd>

**thread_id:** `typing.Optional[str]` — Deprecated alias for sessionId.

</dd>
</dl>

<dl>
<dd>

**conversation_id:** `typing.Optional[str]` — Omit to start a conversation; return this ID on follow-ups.

</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[ExecuteRequestMode]`

</dd>
</dl>

<dl>
<dd>

**context:** `typing.Optional[ExecuteRequestContext]`

</dd>
</dl>

<dl>
<dd>

**memory_agent_id:** `typing.Optional[str]` — Read memory for an account agent you belong to. Does not change the acting identity. Cannot be combined with userId or user_memory.

</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — Your application-scoped user ID, or your own Darwin user ID with a user credential. Reuses memory previously supplied for this user; never grants account access.

</dd>
</dl>

<dl>
<dd>

**user_memory:** `typing.Optional[str]` — Markdown preferences to personalize this request. Read a .md file and pass its text, not a path or URL. With userId, saves these preferences for later requests; empty text clears them.

</dd>
</dl>

<dl>
<dd>

**application_id:** `typing.Optional[str]` — Optional attribution check. Must match the application attached to your API credential; inferred when omitted.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">list_navigator_threads</a>(...) -> ThreadList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Guest session preview requires no account or API key. Retain the returned conversationToken and send X-Assist-Token on follow-ups. Guest limits and sign-in gates apply. The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.list_navigator_threads()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**before:** `typing.Optional[str]` — nextBefore from the previous page.

</dd>
</dl>

<dl>
<dd>

**audience:** `typing.Optional[ListNavigatorThreadsRequestAudience]` — Presentation consumer. Agent returns Markdown and structured facts; human also receives DarwinUI. This does not change identity, permissions or approvals.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">create_thread</a>(...) -> NavigateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Guest session preview requires no account or API key. Retain the returned conversationToken and send X-Assist-Token on follow-ups. Guest limits and sign-in gates apply. The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.create_thread(
    client_request_id="clientRequestId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_request_id:** `str`

</dd>
</dl>

<dl>
<dd>

**audience:** `typing.Optional[CreateThreadRequestAudience]` — Who consumes this response. Controls presentation only; never identity, permissions, or approval.

</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**message:** `typing.Optional[CreateThreadRequestMessage]`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">list_thread_messages</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Guest session preview requires no account or API key. Retain the returned conversationToken and send X-Assist-Token on follow-ups. Guest limits and sign-in gates apply. The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.list_thread_messages(
    thread_id="threadId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**thread_id:** `str`

</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**audience:** `typing.Optional[ListThreadMessagesRequestAudience]` — Presentation consumer. Agent returns Markdown and structured facts; human also receives DarwinUI. This does not change identity, permissions or approvals.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">post_thread_message</a>(...) -> NavigateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Continue an existing Navigator session. Omit target for automatic interpretation in session context, or supply an explicit agent target. Reuse clientMessageId only for an identical retry. Current access, contribution permissions, and execution approvals still apply. A successful response acknowledges the durable turn, not completed provider work. For a specific existing operation instance, use its operation actions endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.post_thread_message(
    thread_id="threadId",
    client_message_id="followup-002",
    message="Focus on papers published this year.",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**thread_id:** `str`

</dd>
</dl>

<dl>
<dd>

**client_message_id:** `str` — A unique ID for this message. Reuse it only when retrying the same request.

</dd>
</dl>

<dl>
<dd>

**message:** `str` — What you want to find, do, or discuss.

</dd>
</dl>

<dl>
<dd>

**audience:** `typing.Optional[ThreadMessageRequestAudience]` — Who consumes this response. Controls presentation only; never identity, permissions, or approval.

</dd>
</dl>

<dl>
<dd>

**target:** `typing.Optional[ThreadMessageRequestTarget]` — Explicit agent target. Bypasses Darwin discovery; it never grants execution authority.

</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[ThreadMessageRequestMode]` — Omit for Auto. Search returns indexed matches; live_search asks providers for current task fit; execute coordinates work; route opens primed agent threads for direct interaction; chat discusses. Approvals still apply.

</dd>
</dl>

<dl>
<dd>

**context:** `typing.Optional[ThreadMessageRequestContext]`

</dd>
</dl>

<dl>
<dd>

**live_search:** `typing.Optional[ThreadMessageRequestLiveSearch]` — Owner-reviewed provider-contact consent or a control for an existing durable session. Omit to review indexed choices without contacting providers.

</dd>
</dl>

<dl>
<dd>

**memory_agent_id:** `typing.Optional[str]` — Read memory for an account agent you belong to. Does not change the acting identity. Cannot be combined with userId or user_memory.

</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — Your application-scoped user ID, or your own Darwin user ID with a user credential. Reuses memory previously supplied for this user; never grants account access.

</dd>
</dl>

<dl>
<dd>

**user_memory:** `typing.Optional[str]` — Markdown preferences to personalize this request. Read a .md file and pass its text, not a path or URL. With userId, saves these preferences for later requests; empty text clears them.

</dd>
</dl>

<dl>
<dd>

**application_id:** `typing.Optional[str]` — Optional attribution check. Must match the application attached to your API credential; inferred when omitted.

</dd>
</dl>

<dl>
<dd>

**attachment_ids:** `typing.Optional[typing.List[str]]`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">get_thread_events</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Guest session preview requires no account or API key. Retain the returned conversationToken and send X-Assist-Token on follow-ups. Guest limits and sign-in gates apply. The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.get_thread_events(
    thread_id="threadId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**thread_id:** `str`

</dd>
</dl>

<dl>
<dd>

**last_event_id:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">list_thread_operations</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Guest session preview requires no account or API key. Retain the returned conversationToken and send X-Assist-Token on follow-ups. Guest limits and sign-in gates apply. The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.list_thread_operations(
    thread_id="threadId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**thread_id:** `str`

</dd>
</dl>

<dl>
<dd>

**audience:** `typing.Optional[ListThreadOperationsRequestAudience]` — Presentation consumer. Agent returns Markdown and structured facts; human also receives DarwinUI. This does not change identity, permissions or approvals.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">start_thread_operation</a>(...) -> ActV3Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Guest session preview requires no account or API key. Retain the returned conversationToken and send X-Assist-Token on follow-ups. Guest limits and sign-in gates apply. The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin, ThreadOperationStartTarget
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.start_thread_operation(
    thread_id="threadId",
    client_request_id="clientRequestId",
    turn_id="turnId",
    target=ThreadOperationStartTarget(
        agent_id="agentId",
    ),
    message="message",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**thread_id:** `str`

</dd>
</dl>

<dl>
<dd>

**client_request_id:** `str`

</dd>
</dl>

<dl>
<dd>

**turn_id:** `str`

</dd>
</dl>

<dl>
<dd>

**target:** `ThreadOperationStartTarget`

</dd>
</dl>

<dl>
<dd>

**message:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">get_thread_operation</a>(...) -> ActV3GetThreadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Guest session preview requires no account or API key. Retain the returned conversationToken and send X-Assist-Token on follow-ups. Guest limits and sign-in gates apply. The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.get_thread_operation(
    thread_id="threadId",
    operation_id="operationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**thread_id:** `str`

</dd>
</dl>

<dl>
<dd>

**operation_id:** `str`

</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**audience:** `typing.Optional[GetThreadOperationRequestAudience]` — Presentation consumer. Agent returns Markdown and structured facts; human also receives DarwinUI. This does not change identity, permissions or approvals.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">interact_with_thread_operation</a>(...) -> ActV3Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Guest session preview requires no account or API key. Retain the returned conversationToken and send X-Assist-Token on follow-ups. Guest limits and sign-in gates apply. The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin, ThreadOperationMessageMessage_Text
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.interact_with_thread_operation(
    thread_id="threadId",
    operation_id="operationId",
    client_message_id="clientMessageId",
    message=ThreadOperationMessageMessage_Text(
        text="text",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**thread_id:** `str`

</dd>
</dl>

<dl>
<dd>

**operation_id:** `str`

</dd>
</dl>

<dl>
<dd>

**client_message_id:** `str`

</dd>
</dl>

<dl>
<dd>

**message:** `ThreadOperationMessageMessage`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">list_thread_invitations</a>() -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.list_thread_invitations()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">list_thread_members</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.list_thread_members(
    thread_id="threadId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**thread_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">remove_thread_member</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.remove_thread_member(
    thread_id="threadId",
    member_id="memberId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**thread_id:** `str`

</dd>
</dl>

<dl>
<dd>

**member_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">change_thread_member</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.change_thread_member(
    thread_id="threadId",
    member_id="memberId",
    role="viewer",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**thread_id:** `str`

</dd>
</dl>

<dl>
<dd>

**member_id:** `str`

</dd>
</dl>

<dl>
<dd>

**role:** `ThreadMemberChangeRole`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">list_thread_attachments</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.list_thread_attachments(
    thread_id="threadId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**thread_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">attach_thread_context</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.attach_thread_context(
    thread_id="threadId",
    file_id="fileId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**thread_id:** `str`

</dd>
</dl>

<dl>
<dd>

**file_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">detach_thread_context</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.detach_thread_context(
    thread_id="threadId",
    attachment_id="attachmentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**thread_id:** `str`

</dd>
</dl>

<dl>
<dd>

**attachment_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">read_thread_context</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.read_thread_context(
    thread_id="threadId",
    attachment_id="attachmentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**thread_id:** `str`

</dd>
</dl>

<dl>
<dd>

**attachment_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">invite_thread_member</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.invite_thread_member(
    thread_id="threadId",
    email="email",
    role="viewer",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**thread_id:** `str`

</dd>
</dl>

<dl>
<dd>

**email:** `str`

</dd>
</dl>

<dl>
<dd>

**role:** `ThreadInvitationRole`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">accept_thread_invitation</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.accept_thread_invitation(
    thread_id="threadId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**thread_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">read_thread</a>(...) -> ReadThreadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read a Navigate or Act session without starting work. Use owner credentials or the matching guest token. An ID alone grants no access.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.read_thread(
    thread_id="threadId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**thread_id:** `str`

</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Navigate turn pagination cursor.

</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Act event pagination cursor.

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Act page size.

</dd>
</dl>

<dl>
<dd>

**audience:** `typing.Optional[ReadThreadRequestAudience]` — Presentation consumer. Agent returns Markdown and structured facts; human also receives DarwinUI. This does not change identity, permissions or approvals.

</dd>
</dl>

<dl>
<dd>

**assist_token:** `typing.Optional[str]` — Guest Navigate session token.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">update_thread</a>(...) -> NavigateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The server checks current session access and resource permissions on every request. Acceptance does not prove provider execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.update_thread(
    thread_id="threadId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**thread_id:** `str`

</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**archived:** `typing.Optional[bool]`

</dd>
</dl>

<dl>
<dd>

**brief:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/darwin_sdk/client.py">get_act_thread</a>(...) -> ActV3GetThreadResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from darwin_sdk import Darwin
from darwin_sdk.environment import DarwinEnvironment

client = Darwin(
    api_key="<value>",
    environment=DarwinEnvironment.DEFAULT,
)

client.get_act_thread(
    thread_id="threadId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**thread_id:** `str`

</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**audience:** `typing.Optional[GetActThreadRequestAudience]` — Presentation consumer. Agent returns Markdown and structured facts; human also receives DarwinUI. This does not change identity, permissions or approvals.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>
