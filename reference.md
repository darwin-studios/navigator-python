# Reference
## Agent
<details><summary><code>client.agent.<a href="src/darwin_sdk/agent/client.py">get_conversation</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
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
    token="<token>",
    environment=DarwinEnvironment.PRODUCTION,
)

client.agent.get_conversation()

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

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
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

<details><summary><code>client.agent.<a href="src/darwin_sdk/agent/client.py">create_message</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
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
    token="<token>",
    environment=DarwinEnvironment.PRODUCTION,
)

client.agent.create_message(
    content="content",
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

**content:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_id:** `typing.Optional[str]` — An optional caller-generated idempotency and correlation identifier.
    
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

## Goals
<details><summary><code>client.goals.<a href="src/darwin_sdk/goals/client.py">list_goals</a>() -> ListGoalsResponse</code></summary>
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
    token="<token>",
    environment=DarwinEnvironment.PRODUCTION,
)

client.goals.list_goals()

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

<details><summary><code>client.goals.<a href="src/darwin_sdk/goals/client.py">create_goal</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
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
    token="<token>",
    environment=DarwinEnvironment.PRODUCTION,
)

client.goals.create_goal(
    intent="intent",
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

**intent:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**kind:** `typing.Optional[CreateGoalRequestKind]` 
    
</dd>
</dl>

<dl>
<dd>

**context:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
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

<details><summary><code>client.goals.<a href="src/darwin_sdk/goals/client.py">get_goal</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
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
    token="<token>",
    environment=DarwinEnvironment.PRODUCTION,
)

client.goals.get_goal(
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

## Approvals
<details><summary><code>client.approvals.<a href="src/darwin_sdk/approvals/client.py">list_approvals</a>(...) -> ListApprovalsResponse</code></summary>
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
    token="<token>",
    environment=DarwinEnvironment.PRODUCTION,
)

client.approvals.list_approvals()

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

**status:** `typing.Optional[str]` 
    
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

<details><summary><code>client.approvals.<a href="src/darwin_sdk/approvals/client.py">decide_approval</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
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
    token="<token>",
    environment=DarwinEnvironment.PRODUCTION,
)

client.approvals.decide_approval(
    id="id",
    decision="APPROVE",
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

**decision:** `ApprovalDecisionRequestDecision` 
    
</dd>
</dl>

<dl>
<dd>

**reason:** `typing.Optional[str]` 
    
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

## Integrations
<details><summary><code>client.integrations.<a href="src/darwin_sdk/integrations/client.py">get_integrations</a>() -> typing.Dict[str, typing.Any]</code></summary>
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
    token="<token>",
    environment=DarwinEnvironment.PRODUCTION,
)

client.integrations.get_integrations()

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

