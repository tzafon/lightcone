# Responses

Types:

```python
from tzafon.types import ContentBlock, ResponsesResponse, ResponseDeleteResponse
```

Methods:

- <code title="post /responses">client.responses.<a href="./src/tzafon/resources/responses.py">create</a>(\*\*<a href="src/tzafon/types/response_create_params.py">params</a>) -> <a href="./src/tzafon/types/responses_response.py">ResponsesResponse</a></code>
- <code title="get /responses/{id}">client.responses.<a href="./src/tzafon/resources/responses.py">retrieve</a>(id) -> <a href="./src/tzafon/types/responses_response.py">ResponsesResponse</a></code>
- <code title="delete /responses/{id}">client.responses.<a href="./src/tzafon/resources/responses.py">delete</a>(id) -> <a href="./src/tzafon/types/response_delete_response.py">ResponseDeleteResponse</a></code>
- <code title="post /responses/{id}/cancel">client.responses.<a href="./src/tzafon/resources/responses.py">cancel</a>(id) -> <a href="./src/tzafon/types/responses_response.py">ResponsesResponse</a></code>

# Computers

Types:

```python
from tzafon.types import (
    ActionResult,
    ComputerAction,
    ComputerResponse,
    ComputerListResponse,
    ComputerBatchResponse,
    ComputerKeepaliveResponse,
    ComputerRetrieveStatusResponse,
)
```

Methods:

- <code title="post /computers">client.computers.<a href="./src/tzafon/resources/computers/computers.py">create</a>(\*\*<a href="src/tzafon/types/computer_create_params.py">params</a>) -> <a href="./src/tzafon/types/computer_response.py">ComputerResponse</a></code>
- <code title="get /computers/{id}">client.computers.<a href="./src/tzafon/resources/computers/computers.py">retrieve</a>(id) -> <a href="./src/tzafon/types/computer_response.py">ComputerResponse</a></code>
- <code title="get /computers">client.computers.<a href="./src/tzafon/resources/computers/computers.py">list</a>(\*\*<a href="src/tzafon/types/computer_list_params.py">params</a>) -> <a href="./src/tzafon/types/computer_list_response.py">ComputerListResponse</a></code>
- <code title="delete /computers/{id}">client.computers.<a href="./src/tzafon/resources/computers/computers.py">delete</a>(id) -> None</code>
- <code title="post /computers/{id}/batch">client.computers.<a href="./src/tzafon/resources/computers/computers.py">batch</a>(id, \*\*<a href="src/tzafon/types/computer_batch_params.py">params</a>) -> <a href="./src/tzafon/types/computer_batch_response.py">ComputerBatchResponse</a></code>
- <code title="post /computers/{id}/change-proxy">client.computers.<a href="./src/tzafon/resources/computers/computers.py">change_proxy</a>(id, \*\*<a href="src/tzafon/types/computer_change_proxy_params.py">params</a>) -> <a href="./src/tzafon/types/action_result.py">ActionResult</a></code>
- <code title="post /computers/{id}/click">client.computers.<a href="./src/tzafon/resources/computers/computers.py">click</a>(id, \*\*<a href="src/tzafon/types/computer_click_params.py">params</a>) -> <a href="./src/tzafon/types/action_result.py">ActionResult</a></code>
- <code title="post /computers/{id}/debug">client.computers.<a href="./src/tzafon/resources/computers/computers.py">debug</a>(id, \*\*<a href="src/tzafon/types/computer_debug_params.py">params</a>) -> <a href="./src/tzafon/types/action_result.py">ActionResult</a></code>
- <code title="post /computers/{id}/double-click">client.computers.<a href="./src/tzafon/resources/computers/computers.py">double_click</a>(id, \*\*<a href="src/tzafon/types/computer_double_click_params.py">params</a>) -> <a href="./src/tzafon/types/action_result.py">ActionResult</a></code>
- <code title="post /computers/{id}/drag">client.computers.<a href="./src/tzafon/resources/computers/computers.py">drag</a>(id, \*\*<a href="src/tzafon/types/computer_drag_params.py">params</a>) -> <a href="./src/tzafon/types/action_result.py">ActionResult</a></code>
- <code title="post /computers/{id}/execute">client.computers.<a href="./src/tzafon/resources/computers/computers.py">execute</a>(id, \*\*<a href="src/tzafon/types/computer_execute_params.py">params</a>) -> <a href="./src/tzafon/types/action_result.py">ActionResult</a></code>
- <code title="post /computers/{id}/hotkey">client.computers.<a href="./src/tzafon/resources/computers/computers.py">hotkey</a>(id, \*\*<a href="src/tzafon/types/computer_hotkey_params.py">params</a>) -> <a href="./src/tzafon/types/action_result.py">ActionResult</a></code>
- <code title="post /computers/{id}/html">client.computers.<a href="./src/tzafon/resources/computers/computers.py">html</a>(id, \*\*<a href="src/tzafon/types/computer_html_params.py">params</a>) -> <a href="./src/tzafon/types/action_result.py">ActionResult</a></code>
- <code title="post /computers/{id}/keepalive">client.computers.<a href="./src/tzafon/resources/computers/computers.py">keepalive</a>(id) -> <a href="./src/tzafon/types/computer_keepalive_response.py">ComputerKeepaliveResponse</a></code>
- <code title="post /computers/{id}/key-down">client.computers.<a href="./src/tzafon/resources/computers/computers.py">key_down</a>(id, \*\*<a href="src/tzafon/types/computer_key_down_params.py">params</a>) -> <a href="./src/tzafon/types/action_result.py">ActionResult</a></code>
- <code title="post /computers/{id}/key-up">client.computers.<a href="./src/tzafon/resources/computers/computers.py">key_up</a>(id, \*\*<a href="src/tzafon/types/computer_key_up_params.py">params</a>) -> <a href="./src/tzafon/types/action_result.py">ActionResult</a></code>
- <code title="post /computers/{id}/mouse-down">client.computers.<a href="./src/tzafon/resources/computers/computers.py">mouse_down</a>(id, \*\*<a href="src/tzafon/types/computer_mouse_down_params.py">params</a>) -> <a href="./src/tzafon/types/action_result.py">ActionResult</a></code>
- <code title="post /computers/{id}/mouse-up">client.computers.<a href="./src/tzafon/resources/computers/computers.py">mouse_up</a>(id, \*\*<a href="src/tzafon/types/computer_mouse_up_params.py">params</a>) -> <a href="./src/tzafon/types/action_result.py">ActionResult</a></code>
- <code title="post /computers/{id}/navigate">client.computers.<a href="./src/tzafon/resources/computers/computers.py">navigate</a>(id, \*\*<a href="src/tzafon/types/computer_navigate_params.py">params</a>) -> <a href="./src/tzafon/types/action_result.py">ActionResult</a></code>
- <code title="get /computers/{id}/events">client.computers.<a href="./src/tzafon/resources/computers/computers.py">retrieve_events</a>(id) -> None</code>
- <code title="get /computers/{id}/screencast">client.computers.<a href="./src/tzafon/resources/computers/computers.py">retrieve_screencast</a>(id) -> None</code>
- <code title="get /computers/{id}/status">client.computers.<a href="./src/tzafon/resources/computers/computers.py">retrieve_status</a>(id) -> <a href="./src/tzafon/types/computer_retrieve_status_response.py">ComputerRetrieveStatusResponse</a></code>
- <code title="get /computers/{id}/ws">client.computers.<a href="./src/tzafon/resources/computers/computers.py">retrieve_ws</a>(id) -> None</code>
- <code title="post /computers/{id}/right-click">client.computers.<a href="./src/tzafon/resources/computers/computers.py">right_click</a>(id, \*\*<a href="src/tzafon/types/computer_right_click_params.py">params</a>) -> <a href="./src/tzafon/types/action_result.py">ActionResult</a></code>
- <code title="post /computers/{id}/screenshot">client.computers.<a href="./src/tzafon/resources/computers/computers.py">screenshot</a>(id, \*\*<a href="src/tzafon/types/computer_screenshot_params.py">params</a>) -> <a href="./src/tzafon/types/action_result.py">ActionResult</a></code>
- <code title="post /computers/{id}/scroll">client.computers.<a href="./src/tzafon/resources/computers/computers.py">scroll</a>(id, \*\*<a href="src/tzafon/types/computer_scroll_params.py">params</a>) -> <a href="./src/tzafon/types/action_result.py">ActionResult</a></code>
- <code title="post /computers/{id}/type">client.computers.<a href="./src/tzafon/resources/computers/computers.py">type</a>(id, \*\*<a href="src/tzafon/types/computer_type_params.py">params</a>) -> <a href="./src/tzafon/types/action_result.py">ActionResult</a></code>
- <code title="post /computers/{id}/viewport">client.computers.<a href="./src/tzafon/resources/computers/computers.py">viewport</a>(id, \*\*<a href="src/tzafon/types/computer_viewport_params.py">params</a>) -> <a href="./src/tzafon/types/action_result.py">ActionResult</a></code>

## Exec

Types:

```python
from tzafon.types.computers import ExecCreateResponse, ExecSyncResponse
```

Methods:

- <code title="post /computers/{id}/exec">client.computers.exec.<a href="./src/tzafon/resources/computers/exec.py">create</a>(id, \*\*<a href="src/tzafon/types/computers/exec_create_params.py">params</a>) -> <a href="./src/tzafon/types/computers/exec_create_response.py">JSONLDecoder[ExecCreateResponse]</a></code>
- <code title="post /computers/{id}/exec/sync">client.computers.exec.<a href="./src/tzafon/resources/computers/exec.py">sync</a>(id, \*\*<a href="src/tzafon/types/computers/exec_sync_params.py">params</a>) -> <a href="./src/tzafon/types/computers/exec_sync_response.py">ExecSyncResponse</a></code>

## Tabs

Methods:

- <code title="post /computers/{id}/tabs">client.computers.tabs.<a href="./src/tzafon/resources/computers/tabs.py">create</a>(id, \*\*<a href="src/tzafon/types/computers/tab_create_params.py">params</a>) -> <a href="./src/tzafon/types/action_result.py">ActionResult</a></code>
- <code title="get /computers/{id}/tabs">client.computers.tabs.<a href="./src/tzafon/resources/computers/tabs.py">list</a>(id) -> <a href="./src/tzafon/types/action_result.py">ActionResult</a></code>
- <code title="delete /computers/{id}/tabs/{tab_id}">client.computers.tabs.<a href="./src/tzafon/resources/computers/tabs.py">delete</a>(tab_id, \*, id) -> <a href="./src/tzafon/types/action_result.py">ActionResult</a></code>
- <code title="post /computers/{id}/tabs/{tab_id}/switch">client.computers.tabs.<a href="./src/tzafon/resources/computers/tabs.py">switch</a>(tab_id, \*, id) -> <a href="./src/tzafon/types/action_result.py">ActionResult</a></code>

# Agent

## Tasks

Types:

```python
from tzafon.types.agent import (
    TaskInjectMessageResponse,
    TaskPauseResponse,
    TaskResumeResponse,
    TaskRetrieveStatusResponse,
    TaskStartResponse,
    TaskStartStreamResponse,
)
```

Methods:

- <code title="post /agent/tasks/{id}/messages">client.agent.tasks.<a href="./src/tzafon/resources/agent/tasks.py">inject_message</a>(id, \*\*<a href="src/tzafon/types/agent/task_inject_message_params.py">params</a>) -> <a href="./src/tzafon/types/agent/task_inject_message_response.py">TaskInjectMessageResponse</a></code>
- <code title="post /agent/tasks/{id}/pause">client.agent.tasks.<a href="./src/tzafon/resources/agent/tasks.py">pause</a>(id) -> <a href="./src/tzafon/types/agent/task_pause_response.py">TaskPauseResponse</a></code>
- <code title="post /agent/tasks/{id}/resume">client.agent.tasks.<a href="./src/tzafon/resources/agent/tasks.py">resume</a>(id) -> <a href="./src/tzafon/types/agent/task_resume_response.py">TaskResumeResponse</a></code>
- <code title="get /agent/tasks/{id}">client.agent.tasks.<a href="./src/tzafon/resources/agent/tasks.py">retrieve_status</a>(id) -> <a href="./src/tzafon/types/agent/task_retrieve_status_response.py">TaskRetrieveStatusResponse</a></code>
- <code title="post /agent/tasks">client.agent.tasks.<a href="./src/tzafon/resources/agent/tasks.py">start</a>(\*\*<a href="src/tzafon/types/agent/task_start_params.py">params</a>) -> <a href="./src/tzafon/types/agent/task_start_response.py">TaskStartResponse</a></code>
- <code title="post /agent/tasks/stream">client.agent.tasks.<a href="./src/tzafon/resources/agent/tasks.py">start_stream</a>(\*\*<a href="src/tzafon/types/agent/task_start_stream_params.py">params</a>) -> str</code>
