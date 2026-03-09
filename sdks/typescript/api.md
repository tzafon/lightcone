# Agent

## Tasks

Types:

- <code><a href="./src/resources/agent/tasks.ts">TaskInjectMessageResponse</a></code>
- <code><a href="./src/resources/agent/tasks.ts">TaskPauseResponse</a></code>
- <code><a href="./src/resources/agent/tasks.ts">TaskResumeResponse</a></code>
- <code><a href="./src/resources/agent/tasks.ts">TaskRetrieveStatusResponse</a></code>
- <code><a href="./src/resources/agent/tasks.ts">TaskStartResponse</a></code>
- <code><a href="./src/resources/agent/tasks.ts">TaskStartStreamResponse</a></code>

Methods:

- <code title="post /agent/tasks/{id}/messages">client.agent.tasks.<a href="./src/resources/agent/tasks.ts">injectMessage</a>(id, { ...params }) -> TaskInjectMessageResponse</code>
- <code title="post /agent/tasks/{id}/pause">client.agent.tasks.<a href="./src/resources/agent/tasks.ts">pause</a>(id) -> TaskPauseResponse</code>
- <code title="post /agent/tasks/{id}/resume">client.agent.tasks.<a href="./src/resources/agent/tasks.ts">resume</a>(id) -> TaskResumeResponse</code>
- <code title="get /agent/tasks/{id}">client.agent.tasks.<a href="./src/resources/agent/tasks.ts">retrieveStatus</a>(id) -> TaskRetrieveStatusResponse</code>
- <code title="post /agent/tasks">client.agent.tasks.<a href="./src/resources/agent/tasks.ts">start</a>({ ...params }) -> TaskStartResponse</code>
- <code title="post /agent/tasks/stream">client.agent.tasks.<a href="./src/resources/agent/tasks.ts">startStream</a>({ ...params }) -> string</code>

# Computers

Types:

- <code><a href="./src/resources/computers/computers.ts">ActionResult</a></code>
- <code><a href="./src/resources/computers/computers.ts">ComputerAction</a></code>
- <code><a href="./src/resources/computers/computers.ts">ComputerResponse</a></code>
- <code><a href="./src/resources/computers/computers.ts">V2GoBackendInternalTypesPageContext</a></code>
- <code><a href="./src/resources/computers/computers.ts">ComputerListResponse</a></code>
- <code><a href="./src/resources/computers/computers.ts">ComputerBatchResponse</a></code>
- <code><a href="./src/resources/computers/computers.ts">ComputerKeepaliveResponse</a></code>
- <code><a href="./src/resources/computers/computers.ts">ComputerRetrieveStatusResponse</a></code>

Methods:

- <code title="post /computers">client.computers.<a href="./src/resources/computers/computers.ts">create</a>({ ...params }) -> ComputerResponse</code>
- <code title="get /computers/{id}">client.computers.<a href="./src/resources/computers/computers.ts">retrieve</a>(id) -> ComputerResponse</code>
- <code title="get /computers">client.computers.<a href="./src/resources/computers/computers.ts">list</a>({ ...params }) -> ComputerListResponse</code>
- <code title="delete /computers/{id}">client.computers.<a href="./src/resources/computers/computers.ts">delete</a>(id) -> void</code>
- <code title="post /computers/{id}/batch">client.computers.<a href="./src/resources/computers/computers.ts">batch</a>(id, { ...params }) -> ComputerBatchResponse</code>
- <code title="post /computers/{id}/change-proxy">client.computers.<a href="./src/resources/computers/computers.ts">changeProxy</a>(id, { ...params }) -> ActionResult</code>
- <code title="post /computers/{id}/click">client.computers.<a href="./src/resources/computers/computers.ts">click</a>(id, { ...params }) -> ActionResult</code>
- <code title="post /computers/{id}/debug">client.computers.<a href="./src/resources/computers/computers.ts">debug</a>(id, { ...params }) -> ActionResult</code>
- <code title="post /computers/{id}/double-click">client.computers.<a href="./src/resources/computers/computers.ts">doubleClick</a>(id, { ...params }) -> ActionResult</code>
- <code title="post /computers/{id}/drag">client.computers.<a href="./src/resources/computers/computers.ts">drag</a>(id, { ...params }) -> ActionResult</code>
- <code title="post /computers/{id}/execute">client.computers.<a href="./src/resources/computers/computers.ts">execute</a>(id, { ...params }) -> ActionResult</code>
- <code title="post /computers/{id}/hotkey">client.computers.<a href="./src/resources/computers/computers.ts">hotkey</a>(id, { ...params }) -> ActionResult</code>
- <code title="post /computers/{id}/html">client.computers.<a href="./src/resources/computers/computers.ts">html</a>(id, { ...params }) -> ActionResult</code>
- <code title="post /computers/{id}/keepalive">client.computers.<a href="./src/resources/computers/computers.ts">keepalive</a>(id) -> ComputerKeepaliveResponse</code>
- <code title="post /computers/{id}/key-down">client.computers.<a href="./src/resources/computers/computers.ts">keyDown</a>(id, { ...params }) -> ActionResult</code>
- <code title="post /computers/{id}/key-up">client.computers.<a href="./src/resources/computers/computers.ts">keyUp</a>(id, { ...params }) -> ActionResult</code>
- <code title="post /computers/{id}/mouse-down">client.computers.<a href="./src/resources/computers/computers.ts">mouseDown</a>(id, { ...params }) -> ActionResult</code>
- <code title="post /computers/{id}/mouse-up">client.computers.<a href="./src/resources/computers/computers.ts">mouseUp</a>(id, { ...params }) -> ActionResult</code>
- <code title="post /computers/{id}/navigate">client.computers.<a href="./src/resources/computers/computers.ts">navigate</a>(id, { ...params }) -> ActionResult</code>
- <code title="get /computers/{id}/events">client.computers.<a href="./src/resources/computers/computers.ts">retrieveEvents</a>(id) -> void</code>
- <code title="get /computers/{id}/screencast">client.computers.<a href="./src/resources/computers/computers.ts">retrieveScreencast</a>(id) -> void</code>
- <code title="get /computers/{id}/status">client.computers.<a href="./src/resources/computers/computers.ts">retrieveStatus</a>(id) -> ComputerRetrieveStatusResponse</code>
- <code title="get /computers/{id}/ws">client.computers.<a href="./src/resources/computers/computers.ts">retrieveWs</a>(id) -> void</code>
- <code title="post /computers/{id}/right-click">client.computers.<a href="./src/resources/computers/computers.ts">rightClick</a>(id, { ...params }) -> ActionResult</code>
- <code title="post /computers/{id}/screenshot">client.computers.<a href="./src/resources/computers/computers.ts">screenshot</a>(id, { ...params }) -> ActionResult</code>
- <code title="post /computers/{id}/scroll">client.computers.<a href="./src/resources/computers/computers.ts">scroll</a>(id, { ...params }) -> ActionResult</code>
- <code title="post /computers/{id}/type">client.computers.<a href="./src/resources/computers/computers.ts">type</a>(id, { ...params }) -> ActionResult</code>
- <code title="post /computers/{id}/viewport">client.computers.<a href="./src/resources/computers/computers.ts">viewport</a>(id, { ...params }) -> ActionResult</code>

## Exec

Types:

- <code><a href="./src/resources/computers/exec.ts">ExecCreateResponse</a></code>
- <code><a href="./src/resources/computers/exec.ts">ExecSyncResponse</a></code>

Methods:

- <code title="post /computers/{id}/exec">client.computers.exec.<a href="./src/resources/computers/exec.ts">create</a>(id, { ...params }) -> ExecCreateResponse</code>
- <code title="post /computers/{id}/exec/sync">client.computers.exec.<a href="./src/resources/computers/exec.ts">sync</a>(id, { ...params }) -> ExecSyncResponse</code>

## Tabs

Methods:

- <code title="post /computers/{id}/tabs">client.computers.tabs.<a href="./src/resources/computers/tabs.ts">create</a>(id, { ...params }) -> ActionResult</code>
- <code title="get /computers/{id}/tabs">client.computers.tabs.<a href="./src/resources/computers/tabs.ts">list</a>(id) -> ActionResult</code>
- <code title="delete /computers/{id}/tabs/{tab_id}">client.computers.tabs.<a href="./src/resources/computers/tabs.ts">delete</a>(tabID, { ...params }) -> ActionResult</code>
- <code title="post /computers/{id}/tabs/{tab_id}/switch">client.computers.tabs.<a href="./src/resources/computers/tabs.ts">switch</a>(tabID, { ...params }) -> ActionResult</code>

# Responses

Types:

- <code><a href="./src/resources/responses.ts">ContentBlock</a></code>
- <code><a href="./src/resources/responses.ts">ResponsesResponse</a></code>
- <code><a href="./src/resources/responses.ts">V2GoBackendInternalServiceAction</a></code>
- <code><a href="./src/resources/responses.ts">V2GoBackendInternalServiceOutputItem</a></code>
- <code><a href="./src/resources/responses.ts">V2GoBackendInternalServiceResponsesUsage</a></code>
- <code><a href="./src/resources/responses.ts">V2GoBackendInternalServiceViewport</a></code>
- <code><a href="./src/resources/responses.ts">ResponseDeleteResponse</a></code>

Methods:

- <code title="post /v1/responses">client.responses.<a href="./src/resources/responses.ts">create</a>({ ...params }) -> ResponsesResponse</code>
- <code title="get /v1/responses/{id}">client.responses.<a href="./src/resources/responses.ts">retrieve</a>(id) -> ResponsesResponse</code>
- <code title="delete /v1/responses/{id}">client.responses.<a href="./src/resources/responses.ts">delete</a>(id) -> ResponseDeleteResponse</code>
- <code title="post /v1/responses/{id}/cancel">client.responses.<a href="./src/resources/responses.ts">cancel</a>(id) -> ResponsesResponse</code>

# Chat

Types:

- <code><a href="./src/resources/chat.ts">ChatCreateCompletionResponse</a></code>

Methods:

- <code title="post /chat/completions">client.chat.<a href="./src/resources/chat.ts">createCompletion</a>({ ...params }) -> unknown</code>

# Models

Types:

- <code><a href="./src/resources/models.ts">ModelListResponse</a></code>

Methods:

- <code title="get /models">client.models.<a href="./src/resources/models.ts">list</a>() -> unknown</code>
