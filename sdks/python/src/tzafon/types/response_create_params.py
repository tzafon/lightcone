# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .logprob_param import LogprobParam
from .message_param import MessageParam
from .summary_param import SummaryParam
from .action_drag_param import ActionDragParam
from .action_find_param import ActionFindParam
from .action_move_param import ActionMoveParam
from .action_type_param import ActionTypeParam
from .action_wait_param import ActionWaitParam
from .output_logs_param import OutputLogsParam
from .action_click_param import ActionClickParam
from .output_image_param import OutputImageParam
from .action_scroll_param import ActionScrollParam
from .action_keypress_param import ActionKeypressParam
from .action_open_page_param import ActionOpenPageParam
from .action_screenshot_param import ActionScreenshotParam
from .comparison_filter_param import ComparisonFilterParam
from .action_double_click_param import ActionDoubleClickParam
from .response_input_file_param import ResponseInputFileParam
from .response_input_text_param import ResponseInputTextParam
from .action_search_source_param import ActionSearchSourceParam
from .annotation_file_path_param import AnnotationFilePathParam
from .mcp_approval_request_param import McpApprovalRequestParam
from .response_input_image_param import ResponseInputImageParam
from .annotation_url_citation_param import AnnotationURLCitationParam
from .annotation_file_citation_param import AnnotationFileCitationParam
from .annotation_container_file_citation_param import AnnotationContainerFileCitationParam

__all__ = [
    "ResponseCreateParams",
    "InputUnionMember1",
    "InputUnionMember1EasyInputMessageParam",
    "InputUnionMember1EasyInputMessageParamContentUnionMember1",
    "InputUnionMember1Message",
    "InputUnionMember1MessageContent",
    "InputUnionMember1ResponseOutputMessageParam",
    "InputUnionMember1ResponseOutputMessageParamContent",
    "InputUnionMember1ResponseOutputMessageParamContentResponseOutputTextParam",
    "InputUnionMember1ResponseOutputMessageParamContentResponseOutputTextParamAnnotation",
    "InputUnionMember1ResponseOutputMessageParamContentResponseOutputRefusalParam",
    "InputUnionMember1ResponseFileSearchToolCallParam",
    "InputUnionMember1ResponseFileSearchToolCallParamResult",
    "InputUnionMember1ResponseComputerToolCallParam",
    "InputUnionMember1ResponseComputerToolCallParamAction",
    "InputUnionMember1ResponseComputerToolCallParamActionActionPointAndType",
    "InputUnionMember1ResponseComputerToolCallParamActionActionMouseDown",
    "InputUnionMember1ResponseComputerToolCallParamActionActionMouseUp",
    "InputUnionMember1ResponseComputerToolCallParamActionActionKeyDown",
    "InputUnionMember1ResponseComputerToolCallParamActionActionKeyUp",
    "InputUnionMember1ResponseComputerToolCallParamPendingSafetyCheck",
    "InputUnionMember1ComputerCallOutput",
    "InputUnionMember1ComputerCallOutputOutput",
    "InputUnionMember1ComputerCallOutputAcknowledgedSafetyCheck",
    "InputUnionMember1ResponseFunctionWebSearchParam",
    "InputUnionMember1ResponseFunctionWebSearchParamAction",
    "InputUnionMember1ResponseFunctionWebSearchParamActionActionSearch",
    "InputUnionMember1ResponseFunctionToolCallParam",
    "InputUnionMember1FunctionCallOutput",
    "InputUnionMember1FunctionCallOutputOutputUnionMember1",
    "InputUnionMember1FunctionCallOutputOutputUnionMember1ResponseInputTextContentParam",
    "InputUnionMember1FunctionCallOutputOutputUnionMember1ResponseInputImageContentParam",
    "InputUnionMember1FunctionCallOutputOutputUnionMember1ResponseInputFileContentParam",
    "InputUnionMember1ResponseReasoningItemParam",
    "InputUnionMember1ResponseReasoningItemParamContent",
    "InputUnionMember1ResponseCompactionItemParamParam",
    "InputUnionMember1ImageGenerationCall",
    "InputUnionMember1ResponseCodeInterpreterToolCallParam",
    "InputUnionMember1ResponseCodeInterpreterToolCallParamOutput",
    "InputUnionMember1LocalShellCall",
    "InputUnionMember1LocalShellCallAction",
    "InputUnionMember1LocalShellCallOutput",
    "InputUnionMember1ShellCall",
    "InputUnionMember1ShellCallAction",
    "InputUnionMember1ShellCallOutput",
    "InputUnionMember1ShellCallOutputOutput",
    "InputUnionMember1ShellCallOutputOutputOutcome",
    "InputUnionMember1ShellCallOutputOutputOutcomeOutcomeTimeout",
    "InputUnionMember1ShellCallOutputOutputOutcomeOutcomeExit",
    "InputUnionMember1ApplyPatchCall",
    "InputUnionMember1ApplyPatchCallOperation",
    "InputUnionMember1ApplyPatchCallOperationApplyPatchCallOperationCreateFile",
    "InputUnionMember1ApplyPatchCallOperationApplyPatchCallOperationDeleteFile",
    "InputUnionMember1ApplyPatchCallOperationApplyPatchCallOperationUpdateFile",
    "InputUnionMember1ApplyPatchCallOutput",
    "InputUnionMember1McpListTools",
    "InputUnionMember1McpListToolsTool",
    "InputUnionMember1McpApprovalResponse",
    "InputUnionMember1McpCall",
    "InputUnionMember1ResponseCustomToolCallOutputParam",
    "InputUnionMember1ResponseCustomToolCallOutputParamOutputUnionMember1",
    "InputUnionMember1ResponseCustomToolCallParam",
    "InputUnionMember1ItemReference",
    "InputUnionMember1ResponseOutputMessage",
    "InputUnionMember1ResponseOutputMessageContent",
    "InputUnionMember1ResponseOutputMessageContentResponseOutputText",
    "InputUnionMember1ResponseOutputMessageContentResponseOutputTextAnnotation",
    "InputUnionMember1ResponseOutputMessageContentResponseOutputRefusal",
    "InputUnionMember1ResponseFileSearchToolCall",
    "InputUnionMember1ResponseFileSearchToolCallResult",
    "InputUnionMember1ResponseFunctionToolCall",
    "InputUnionMember1ResponseFunctionWebSearch",
    "InputUnionMember1ResponseFunctionWebSearchAction",
    "InputUnionMember1ResponseFunctionWebSearchActionActionSearch",
    "InputUnionMember1ResponseComputerToolCall",
    "InputUnionMember1ResponseComputerToolCallAction",
    "InputUnionMember1ResponseComputerToolCallActionActionPointAndType",
    "InputUnionMember1ResponseComputerToolCallActionActionMouseDown",
    "InputUnionMember1ResponseComputerToolCallActionActionMouseUp",
    "InputUnionMember1ResponseComputerToolCallActionActionKeyDown",
    "InputUnionMember1ResponseComputerToolCallActionActionKeyUp",
    "InputUnionMember1ResponseComputerToolCallPendingSafetyCheck",
    "InputUnionMember1ResponseReasoningItem",
    "InputUnionMember1ResponseReasoningItemContent",
    "InputUnionMember1ResponseCompactionItem",
    "InputUnionMember1ResponseCodeInterpreterToolCall",
    "InputUnionMember1ResponseCodeInterpreterToolCallOutput",
    "InputUnionMember1ResponseFunctionShellToolCall",
    "InputUnionMember1ResponseFunctionShellToolCallAction",
    "InputUnionMember1ResponseFunctionShellToolCallOutput",
    "InputUnionMember1ResponseFunctionShellToolCallOutputOutput",
    "InputUnionMember1ResponseFunctionShellToolCallOutputOutputOutcome",
    "InputUnionMember1ResponseFunctionShellToolCallOutputOutputOutcomeOutputOutcomeTimeout",
    "InputUnionMember1ResponseFunctionShellToolCallOutputOutputOutcomeOutputOutcomeExit",
    "InputUnionMember1ResponseApplyPatchToolCall",
    "InputUnionMember1ResponseApplyPatchToolCallOperation",
    "InputUnionMember1ResponseApplyPatchToolCallOperationOperationCreateFile",
    "InputUnionMember1ResponseApplyPatchToolCallOperationOperationDeleteFile",
    "InputUnionMember1ResponseApplyPatchToolCallOperationOperationUpdateFile",
    "InputUnionMember1ResponseApplyPatchToolCallOutput",
    "InputUnionMember1ResponseCustomToolCall",
    "PreviousInputMessage",
    "Prompt",
    "PromptVariables",
    "PromptVariablesResponseInputText",
    "PromptVariablesResponseInputImage",
    "PromptVariablesResponseInputFile",
    "Reasoning",
    "Text",
    "TextFormat",
    "TextFormatResponseFormatText",
    "TextFormatResponseFormatTextJsonSchemaConfig",
    "TextFormatResponseFormatJsonObject",
    "ToolChoice",
    "ToolChoiceToolChoiceAllowed",
    "ToolChoiceToolChoiceTypes",
    "ToolChoiceToolChoiceFunction",
    "ToolChoiceToolChoiceMcp",
    "ToolChoiceToolChoiceCustom",
    "ToolChoiceToolChoiceApplyPatch",
    "ToolChoiceToolChoiceShell",
    "Tool",
    "ToolFunctionTool",
    "ToolFileSearchTool",
    "ToolFileSearchToolFilters",
    "ToolFileSearchToolFiltersCompoundFilter",
    "ToolFileSearchToolFiltersCompoundFilterFilter",
    "ToolFileSearchToolRankingOptions",
    "ToolFileSearchToolRankingOptionsHybridSearch",
    "ToolComputerTool",
    "ToolWebSearchTool",
    "ToolWebSearchToolFilters",
    "ToolWebSearchToolUserLocation",
    "ToolMcp",
    "ToolMcpAllowedTools",
    "ToolMcpAllowedToolsMcpAllowedToolsMcpToolFilter",
    "ToolMcpRequireApproval",
    "ToolMcpRequireApprovalMcpRequireApprovalMcpToolApprovalFilter",
    "ToolMcpRequireApprovalMcpRequireApprovalMcpToolApprovalFilterAlways",
    "ToolMcpRequireApprovalMcpRequireApprovalMcpToolApprovalFilterNever",
    "ToolCodeInterpreter",
    "ToolCodeInterpreterContainer",
    "ToolCodeInterpreterContainerCodeInterpreterContainerCodeInterpreterToolAuto",
    "ToolImageGeneration",
    "ToolImageGenerationInputImageMask",
    "ToolLocalShell",
    "ToolFunctionShellTool",
    "ToolCustomTool",
    "ToolCustomToolFormat",
    "ToolCustomToolFormatText",
    "ToolCustomToolFormatGrammar",
    "ToolWebSearchPreviewTool",
    "ToolWebSearchPreviewToolUserLocation",
    "ToolApplyPatchTool",
]


class ResponseCreateParams(TypedDict, total=False):
    input: Required[Union[str, Iterable[InputUnionMember1]]]

    background: Optional[bool]

    cache_salt: Optional[str]
    """
    If specified, the prefix cache will be salted with the provided string to
    prevent an attacker to guess prompts in multi-user environments. The salt should
    be random, protected from access by 3rd parties, and long enough to be
    unpredictable (e.g., 43 characters base64-encoded, corresponding to 256 bit).
    """

    enable_response_messages: bool
    """Dictates whether or not to return messages as part of the response object.

    Currently only supported fornon-background and gpt-oss only.
    """

    include: Optional[
        List[
            Literal[
                "code_interpreter_call.outputs",
                "computer_call_output.output.image_url",
                "file_search_call.results",
                "message.input_image.image_url",
                "message.output_text.logprobs",
                "reasoning.encrypted_content",
            ]
        ]
    ]

    include_stop_str_in_output: bool

    instructions: Optional[str]

    logit_bias: Optional[Dict[str, float]]

    max_output_tokens: Optional[int]

    max_tool_calls: Optional[int]

    metadata: Optional[Dict[str, str]]

    mm_processor_kwargs: Optional[Dict[str, object]]
    """Additional kwargs to pass to the HF processor."""

    model: Optional[str]

    parallel_tool_calls: Optional[bool]

    previous_input_messages: Optional[Iterable[PreviousInputMessage]]

    previous_response_id: Optional[str]

    priority: int
    """The priority of the request (lower means earlier handling; default: 0).

    Any priority other than 0 will raise an error if the served model does not use
    priority scheduling.
    """

    prompt: Optional[Prompt]
    """
    Reference to a prompt template and its variables.
    [Learn more](https://platform.openai.com/docs/guides/text?api-mode=responses#reusable-prompts).
    """

    prompt_cache_key: Optional[str]
    """
    A key that was used to read from or write to the prompt cache.Note: This field
    has not been implemented yet and vLLM will ignore it.
    """

    reasoning: Optional[Reasoning]
    """**gpt-5 and o-series models only**

    Configuration options for
    [reasoning models](https://platform.openai.com/docs/guides/reasoning).
    """

    request_id: str
    """The request_id related to this request.

    If the caller does not set it, a random_uuid will be generated. This id is used
    through out the inference process and return in response.
    """

    service_tier: Literal["auto", "default", "flex", "scale", "priority"]

    skip_special_tokens: bool

    store: Optional[bool]

    stream: Optional[bool]

    temperature: Optional[float]

    text: Optional[Text]
    """Configuration options for a text response from the model.

    Can be plain text or structured JSON data. Learn more:

    - [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
    - [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)
    """

    tool_choice: ToolChoice
    """Constrains the tools available to the model to a pre-defined set."""

    tools: Iterable[Tool]

    top_k: Optional[int]

    top_logprobs: Optional[int]

    top_p: Optional[float]

    truncation: Optional[Literal["auto", "disabled"]]

    user: Optional[str]


InputUnionMember1EasyInputMessageParamContentUnionMember1: TypeAlias = Union[
    ResponseInputTextParam, ResponseInputImageParam, ResponseInputFileParam
]


class InputUnionMember1EasyInputMessageParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """
    A message input to the model with a role indicating instruction following
    hierarchy. Instructions given with the `developer` or `system` role take
    precedence over instructions given with the `user` role. Messages with the
    `assistant` role are presumed to have been generated by the model in previous
    interactions.
    """

    content: Required[Union[str, Iterable[InputUnionMember1EasyInputMessageParamContentUnionMember1]]]

    role: Required[Literal["user", "assistant", "system", "developer"]]

    type: Literal["message"]


InputUnionMember1MessageContent: TypeAlias = Union[
    ResponseInputTextParam, ResponseInputImageParam, ResponseInputFileParam
]


class InputUnionMember1Message(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """
    A message input to the model with a role indicating instruction following
    hierarchy. Instructions given with the `developer` or `system` role take
    precedence over instructions given with the `user` role.
    """

    content: Required[Iterable[InputUnionMember1MessageContent]]

    role: Required[Literal["user", "system", "developer"]]

    status: Literal["in_progress", "completed", "incomplete"]

    type: Literal["message"]


InputUnionMember1ResponseOutputMessageParamContentResponseOutputTextParamAnnotation: TypeAlias = Union[
    AnnotationFileCitationParam,
    AnnotationURLCitationParam,
    AnnotationContainerFileCitationParam,
    AnnotationFilePathParam,
]


class InputUnionMember1ResponseOutputMessageParamContentResponseOutputTextParam(  # type: ignore[call-arg]
    TypedDict, total=False, extra_items=object
):
    """A text output from the model."""

    annotations: Required[Iterable[InputUnionMember1ResponseOutputMessageParamContentResponseOutputTextParamAnnotation]]

    text: Required[str]

    type: Required[Literal["output_text"]]

    logprobs: Iterable[LogprobParam]


class InputUnionMember1ResponseOutputMessageParamContentResponseOutputRefusalParam(  # type: ignore[call-arg]
    TypedDict, total=False, extra_items=object
):
    """A refusal from the model."""

    refusal: Required[str]

    type: Required[Literal["refusal"]]


InputUnionMember1ResponseOutputMessageParamContent: TypeAlias = Union[
    InputUnionMember1ResponseOutputMessageParamContentResponseOutputTextParam,
    InputUnionMember1ResponseOutputMessageParamContentResponseOutputRefusalParam,
]


class InputUnionMember1ResponseOutputMessageParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """An output message from the model."""

    id: Required[str]

    content: Required[Iterable[InputUnionMember1ResponseOutputMessageParamContent]]

    role: Required[Literal["assistant"]]

    status: Required[Literal["in_progress", "completed", "incomplete"]]

    type: Required[Literal["message"]]


class InputUnionMember1ResponseFileSearchToolCallParamResult(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    attributes: Optional[Dict[str, Union[str, float, bool]]]

    file_id: str

    filename: str

    score: float

    text: str


class InputUnionMember1ResponseFileSearchToolCallParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """The results of a file search tool call.

    See the
    [file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.
    """

    id: Required[str]

    queries: Required[SequenceNotStr[str]]

    status: Required[Literal["in_progress", "searching", "completed", "incomplete", "failed"]]

    type: Required[Literal["file_search_call"]]

    results: Optional[Iterable[InputUnionMember1ResponseFileSearchToolCallParamResult]]


class InputUnionMember1ResponseComputerToolCallParamActionActionPointAndType(  # type: ignore[call-arg]
    TypedDict, total=False, extra_items=object
):
    """Click at a position then type text."""

    text: Required[str]

    type: Required[Literal["point_and_type"]]

    x: Required[int]

    y: Required[int]


class InputUnionMember1ResponseComputerToolCallParamActionActionMouseDown(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Press and hold the left mouse button at a position."""

    type: Required[Literal["mouse_down"]]

    x: Required[int]

    y: Required[int]


class InputUnionMember1ResponseComputerToolCallParamActionActionMouseUp(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Release the left mouse button at a position."""

    type: Required[Literal["mouse_up"]]

    x: Required[int]

    y: Required[int]


class InputUnionMember1ResponseComputerToolCallParamActionActionKeyDown(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Press and hold a key."""

    keys: Required[SequenceNotStr[str]]

    type: Required[Literal["key_down"]]


class InputUnionMember1ResponseComputerToolCallParamActionActionKeyUp(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Release a held key."""

    keys: Required[SequenceNotStr[str]]

    type: Required[Literal["key_up"]]


InputUnionMember1ResponseComputerToolCallParamAction: TypeAlias = Union[
    ActionClickParam,
    ActionDoubleClickParam,
    ActionDragParam,
    ActionKeypressParam,
    ActionMoveParam,
    ActionScreenshotParam,
    ActionScrollParam,
    ActionTypeParam,
    ActionWaitParam,
    InputUnionMember1ResponseComputerToolCallParamActionActionPointAndType,
    InputUnionMember1ResponseComputerToolCallParamActionActionMouseDown,
    InputUnionMember1ResponseComputerToolCallParamActionActionMouseUp,
    InputUnionMember1ResponseComputerToolCallParamActionActionKeyDown,
    InputUnionMember1ResponseComputerToolCallParamActionActionKeyUp,
]


class InputUnionMember1ResponseComputerToolCallParamPendingSafetyCheck(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A pending safety check for the computer call."""

    id: Required[str]

    code: Optional[str]

    message: Optional[str]


class InputUnionMember1ResponseComputerToolCallParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A tool call to a computer use tool.

    See the
    [computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.
    """

    id: Required[str]

    action: Required[InputUnionMember1ResponseComputerToolCallParamAction]
    """A click action."""

    call_id: Required[str]

    pending_safety_checks: Required[Iterable[InputUnionMember1ResponseComputerToolCallParamPendingSafetyCheck]]

    status: Required[Literal["in_progress", "completed", "incomplete"]]

    type: Required[Literal["computer_call"]]


class InputUnionMember1ComputerCallOutputOutput(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A computer screenshot image used with the computer use tool."""

    type: Required[Literal["computer_screenshot"]]

    file_id: str

    image_url: str


class InputUnionMember1ComputerCallOutputAcknowledgedSafetyCheck(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A pending safety check for the computer call."""

    id: Required[str]

    code: Optional[str]

    message: Optional[str]


class InputUnionMember1ComputerCallOutput(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """The output of a computer tool call."""

    call_id: Required[str]

    output: Required[InputUnionMember1ComputerCallOutputOutput]
    """A computer screenshot image used with the computer use tool."""

    type: Required[Literal["computer_call_output"]]

    id: Optional[str]

    acknowledged_safety_checks: Optional[Iterable[InputUnionMember1ComputerCallOutputAcknowledgedSafetyCheck]]

    status: Optional[Literal["in_progress", "completed", "incomplete"]]


class InputUnionMember1ResponseFunctionWebSearchParamActionActionSearch(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Action type "search" - Performs a web search query."""

    query: Required[str]

    type: Required[Literal["search"]]

    queries: SequenceNotStr[str]

    sources: Iterable[ActionSearchSourceParam]


InputUnionMember1ResponseFunctionWebSearchParamAction: TypeAlias = Union[
    InputUnionMember1ResponseFunctionWebSearchParamActionActionSearch, ActionOpenPageParam, ActionFindParam
]


class InputUnionMember1ResponseFunctionWebSearchParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """The results of a web search tool call.

    See the
    [web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.
    """

    id: Required[str]

    action: Required[InputUnionMember1ResponseFunctionWebSearchParamAction]
    """Action type "search" - Performs a web search query."""

    status: Required[Literal["in_progress", "searching", "completed", "failed"]]

    type: Required[Literal["web_search_call"]]


class InputUnionMember1ResponseFunctionToolCallParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A tool call to run a function.

    See the
    [function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.
    """

    arguments: Required[str]

    call_id: Required[str]

    name: Required[str]

    type: Required[Literal["function_call"]]

    id: str

    status: Literal["in_progress", "completed", "incomplete"]


class InputUnionMember1FunctionCallOutputOutputUnionMember1ResponseInputTextContentParam(  # type: ignore[call-arg]
    TypedDict, total=False, extra_items=object
):
    """A text input to the model."""

    text: Required[str]

    type: Required[Literal["input_text"]]


class InputUnionMember1FunctionCallOutputOutputUnionMember1ResponseInputImageContentParam(  # type: ignore[call-arg]
    TypedDict, total=False, extra_items=object
):
    """An image input to the model.

    Learn about [image inputs](https://platform.openai.com/docs/guides/vision)
    """

    type: Required[Literal["input_image"]]

    detail: Optional[Literal["low", "high", "auto"]]

    file_id: Optional[str]

    image_url: Optional[str]


class InputUnionMember1FunctionCallOutputOutputUnionMember1ResponseInputFileContentParam(  # type: ignore[call-arg]
    TypedDict, total=False, extra_items=object
):
    """A file input to the model."""

    type: Required[Literal["input_file"]]

    file_data: Optional[str]

    file_id: Optional[str]

    file_url: Optional[str]

    filename: Optional[str]


InputUnionMember1FunctionCallOutputOutputUnionMember1: TypeAlias = Union[
    InputUnionMember1FunctionCallOutputOutputUnionMember1ResponseInputTextContentParam,
    InputUnionMember1FunctionCallOutputOutputUnionMember1ResponseInputImageContentParam,
    InputUnionMember1FunctionCallOutputOutputUnionMember1ResponseInputFileContentParam,
]


class InputUnionMember1FunctionCallOutput(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """The output of a function tool call."""

    call_id: Required[str]

    output: Required[Union[str, Iterable[InputUnionMember1FunctionCallOutputOutputUnionMember1]]]

    type: Required[Literal["function_call_output"]]

    id: Optional[str]

    status: Optional[Literal["in_progress", "completed", "incomplete"]]


class InputUnionMember1ResponseReasoningItemParamContent(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Reasoning text from the model."""

    text: Required[str]

    type: Required[Literal["reasoning_text"]]


class InputUnionMember1ResponseReasoningItemParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """
    A description of the chain of thought used by a reasoning model while generating
    a response. Be sure to include these items in your `input` to the Responses API
    for subsequent turns of a conversation if you are manually
    [managing context](https://platform.openai.com/docs/guides/conversation-state).
    """

    id: Required[str]

    summary: Required[Iterable[SummaryParam]]

    type: Required[Literal["reasoning"]]

    content: Iterable[InputUnionMember1ResponseReasoningItemParamContent]

    encrypted_content: Optional[str]

    status: Literal["in_progress", "completed", "incomplete"]


class InputUnionMember1ResponseCompactionItemParamParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """
    A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).
    """

    encrypted_content: Required[str]

    type: Required[Literal["compaction"]]

    id: Optional[str]


class InputUnionMember1ImageGenerationCall(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """An image generation request made by the model."""

    id: Required[str]

    result: Required[Optional[str]]

    status: Required[Literal["in_progress", "completed", "generating", "failed"]]

    type: Required[Literal["image_generation_call"]]


InputUnionMember1ResponseCodeInterpreterToolCallParamOutput: TypeAlias = Union[OutputLogsParam, OutputImageParam]


class InputUnionMember1ResponseCodeInterpreterToolCallParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A tool call to run code."""

    id: Required[str]

    code: Required[Optional[str]]

    container_id: Required[str]

    outputs: Required[Optional[Iterable[InputUnionMember1ResponseCodeInterpreterToolCallParamOutput]]]

    status: Required[Literal["in_progress", "completed", "incomplete", "interpreting", "failed"]]

    type: Required[Literal["code_interpreter_call"]]


class InputUnionMember1LocalShellCallAction(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Execute a shell command on the server."""

    command: Required[SequenceNotStr[str]]

    env: Required[Dict[str, str]]

    type: Required[Literal["exec"]]

    timeout_ms: Optional[int]

    user: Optional[str]

    working_directory: Optional[str]


class InputUnionMember1LocalShellCall(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A tool call to run a command on the local shell."""

    id: Required[str]

    action: Required[InputUnionMember1LocalShellCallAction]
    """Execute a shell command on the server."""

    call_id: Required[str]

    status: Required[Literal["in_progress", "completed", "incomplete"]]

    type: Required[Literal["local_shell_call"]]


class InputUnionMember1LocalShellCallOutput(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """The output of a local shell tool call."""

    id: Required[str]

    output: Required[str]

    type: Required[Literal["local_shell_call_output"]]

    status: Optional[Literal["in_progress", "completed", "incomplete"]]


class InputUnionMember1ShellCallAction(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """The shell commands and limits that describe how to run the tool call."""

    commands: Required[SequenceNotStr[str]]

    max_output_length: Optional[int]

    timeout_ms: Optional[int]


class InputUnionMember1ShellCall(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A tool representing a request to execute one or more shell commands."""

    action: Required[InputUnionMember1ShellCallAction]
    """The shell commands and limits that describe how to run the tool call."""

    call_id: Required[str]

    type: Required[Literal["shell_call"]]

    id: Optional[str]

    status: Optional[Literal["in_progress", "completed", "incomplete"]]


class InputUnionMember1ShellCallOutputOutputOutcomeOutcomeTimeout(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Indicates that the shell call exceeded its configured time limit."""

    type: Required[Literal["timeout"]]


class InputUnionMember1ShellCallOutputOutputOutcomeOutcomeExit(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Indicates that the shell commands finished and returned an exit code."""

    exit_code: Required[int]

    type: Required[Literal["exit"]]


InputUnionMember1ShellCallOutputOutputOutcome: TypeAlias = Union[
    InputUnionMember1ShellCallOutputOutputOutcomeOutcomeTimeout,
    InputUnionMember1ShellCallOutputOutputOutcomeOutcomeExit,
]


class InputUnionMember1ShellCallOutputOutput(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Captured stdout and stderr for a portion of a shell tool call output."""

    outcome: Required[InputUnionMember1ShellCallOutputOutputOutcome]
    """Indicates that the shell call exceeded its configured time limit."""

    stderr: Required[str]

    stdout: Required[str]


class InputUnionMember1ShellCallOutput(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """The streamed output items emitted by a shell tool call."""

    call_id: Required[str]

    output: Required[Iterable[InputUnionMember1ShellCallOutputOutput]]

    type: Required[Literal["shell_call_output"]]

    id: Optional[str]

    max_output_length: Optional[int]


class InputUnionMember1ApplyPatchCallOperationApplyPatchCallOperationCreateFile(  # type: ignore[call-arg]
    TypedDict, total=False, extra_items=object
):
    """Instruction for creating a new file via the apply_patch tool."""

    diff: Required[str]

    path: Required[str]

    type: Required[Literal["create_file"]]


class InputUnionMember1ApplyPatchCallOperationApplyPatchCallOperationDeleteFile(  # type: ignore[call-arg]
    TypedDict, total=False, extra_items=object
):
    """Instruction for deleting an existing file via the apply_patch tool."""

    path: Required[str]

    type: Required[Literal["delete_file"]]


class InputUnionMember1ApplyPatchCallOperationApplyPatchCallOperationUpdateFile(  # type: ignore[call-arg]
    TypedDict, total=False, extra_items=object
):
    """Instruction for updating an existing file via the apply_patch tool."""

    diff: Required[str]

    path: Required[str]

    type: Required[Literal["update_file"]]


InputUnionMember1ApplyPatchCallOperation: TypeAlias = Union[
    InputUnionMember1ApplyPatchCallOperationApplyPatchCallOperationCreateFile,
    InputUnionMember1ApplyPatchCallOperationApplyPatchCallOperationDeleteFile,
    InputUnionMember1ApplyPatchCallOperationApplyPatchCallOperationUpdateFile,
]


class InputUnionMember1ApplyPatchCall(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """
    A tool call representing a request to create, delete, or update files using diff patches.
    """

    call_id: Required[str]

    operation: Required[InputUnionMember1ApplyPatchCallOperation]
    """Instruction for creating a new file via the apply_patch tool."""

    status: Required[Literal["in_progress", "completed"]]

    type: Required[Literal["apply_patch_call"]]

    id: Optional[str]


class InputUnionMember1ApplyPatchCallOutput(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """The streamed output emitted by an apply patch tool call."""

    call_id: Required[str]

    status: Required[Literal["completed", "failed"]]

    type: Required[Literal["apply_patch_call_output"]]

    id: Optional[str]

    output: Optional[str]


class InputUnionMember1McpListToolsTool(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A tool available on an MCP server."""

    input_schema: Required[object]

    name: Required[str]

    annotations: object

    description: Optional[str]


class InputUnionMember1McpListTools(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A list of tools available on an MCP server."""

    id: Required[str]

    server_label: Required[str]

    tools: Required[Iterable[InputUnionMember1McpListToolsTool]]

    type: Required[Literal["mcp_list_tools"]]

    error: Optional[str]


class InputUnionMember1McpApprovalResponse(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A response to an MCP approval request."""

    approval_request_id: Required[str]

    approve: Required[bool]

    type: Required[Literal["mcp_approval_response"]]

    id: Optional[str]

    reason: Optional[str]


class InputUnionMember1McpCall(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """An invocation of a tool on an MCP server."""

    id: Required[str]

    arguments: Required[str]

    name: Required[str]

    server_label: Required[str]

    type: Required[Literal["mcp_call"]]

    approval_request_id: Optional[str]

    error: Optional[str]

    output: Optional[str]

    status: Literal["in_progress", "completed", "incomplete", "calling", "failed"]


InputUnionMember1ResponseCustomToolCallOutputParamOutputUnionMember1: TypeAlias = Union[
    ResponseInputTextParam, ResponseInputImageParam, ResponseInputFileParam
]


class InputUnionMember1ResponseCustomToolCallOutputParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """The output of a custom tool call from your code, being sent back to the model."""

    call_id: Required[str]

    output: Required[Union[str, Iterable[InputUnionMember1ResponseCustomToolCallOutputParamOutputUnionMember1]]]

    type: Required[Literal["custom_tool_call_output"]]

    id: str


class InputUnionMember1ResponseCustomToolCallParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A call to a custom tool created by the model."""

    call_id: Required[str]

    input: Required[str]

    name: Required[str]

    type: Required[Literal["custom_tool_call"]]

    id: str


class InputUnionMember1ItemReference(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """An internal identifier for an item to reference."""

    id: Required[str]

    type: Optional[Literal["item_reference"]]


InputUnionMember1ResponseOutputMessageContentResponseOutputTextAnnotation: TypeAlias = Union[
    AnnotationFileCitationParam,
    AnnotationURLCitationParam,
    AnnotationContainerFileCitationParam,
    AnnotationFilePathParam,
]


class InputUnionMember1ResponseOutputMessageContentResponseOutputText(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A text output from the model."""

    annotations: Required[Iterable[InputUnionMember1ResponseOutputMessageContentResponseOutputTextAnnotation]]

    text: Required[str]

    type: Required[Literal["output_text"]]

    logprobs: Optional[Iterable[LogprobParam]]


class InputUnionMember1ResponseOutputMessageContentResponseOutputRefusal(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A refusal from the model."""

    refusal: Required[str]

    type: Required[Literal["refusal"]]


InputUnionMember1ResponseOutputMessageContent: TypeAlias = Union[
    InputUnionMember1ResponseOutputMessageContentResponseOutputText,
    InputUnionMember1ResponseOutputMessageContentResponseOutputRefusal,
]


class InputUnionMember1ResponseOutputMessage(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """An output message from the model."""

    id: Required[str]

    content: Required[Iterable[InputUnionMember1ResponseOutputMessageContent]]

    role: Required[Literal["assistant"]]

    status: Required[Literal["in_progress", "completed", "incomplete"]]

    type: Required[Literal["message"]]


class InputUnionMember1ResponseFileSearchToolCallResult(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    attributes: Optional[Dict[str, Union[str, float, bool]]]

    file_id: Optional[str]

    filename: Optional[str]

    score: Optional[float]

    text: Optional[str]


class InputUnionMember1ResponseFileSearchToolCall(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """The results of a file search tool call.

    See the
    [file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.
    """

    id: Required[str]

    queries: Required[SequenceNotStr[str]]

    status: Required[Literal["in_progress", "searching", "completed", "incomplete", "failed"]]

    type: Required[Literal["file_search_call"]]

    results: Optional[Iterable[InputUnionMember1ResponseFileSearchToolCallResult]]


class InputUnionMember1ResponseFunctionToolCall(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A tool call to run a function.

    See the
    [function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.
    """

    arguments: Required[str]

    call_id: Required[str]

    name: Required[str]

    type: Required[Literal["function_call"]]

    id: Optional[str]

    status: Optional[Literal["in_progress", "completed", "incomplete"]]


class InputUnionMember1ResponseFunctionWebSearchActionActionSearch(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Action type "search" - Performs a web search query."""

    query: Required[str]

    type: Required[Literal["search"]]

    queries: Optional[SequenceNotStr[str]]

    sources: Optional[Iterable[ActionSearchSourceParam]]


InputUnionMember1ResponseFunctionWebSearchAction: TypeAlias = Union[
    InputUnionMember1ResponseFunctionWebSearchActionActionSearch, ActionOpenPageParam, ActionFindParam
]


class InputUnionMember1ResponseFunctionWebSearch(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """The results of a web search tool call.

    See the
    [web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.
    """

    id: Required[str]

    action: Required[InputUnionMember1ResponseFunctionWebSearchAction]
    """Action type "search" - Performs a web search query."""

    status: Required[Literal["in_progress", "searching", "completed", "failed"]]

    type: Required[Literal["web_search_call"]]


class InputUnionMember1ResponseComputerToolCallActionActionPointAndType(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Click at a position then type text."""

    text: Required[str]

    type: Required[Literal["point_and_type"]]

    x: Required[int]

    y: Required[int]


class InputUnionMember1ResponseComputerToolCallActionActionMouseDown(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Press and hold the left mouse button at a position."""

    type: Required[Literal["mouse_down"]]

    x: Required[int]

    y: Required[int]


class InputUnionMember1ResponseComputerToolCallActionActionMouseUp(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Release the left mouse button at a position."""

    type: Required[Literal["mouse_up"]]

    x: Required[int]

    y: Required[int]


class InputUnionMember1ResponseComputerToolCallActionActionKeyDown(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Press and hold a key."""

    keys: Required[SequenceNotStr[str]]

    type: Required[Literal["key_down"]]


class InputUnionMember1ResponseComputerToolCallActionActionKeyUp(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Release a held key."""

    keys: Required[SequenceNotStr[str]]

    type: Required[Literal["key_up"]]


InputUnionMember1ResponseComputerToolCallAction: TypeAlias = Union[
    ActionClickParam,
    ActionDoubleClickParam,
    ActionDragParam,
    ActionKeypressParam,
    ActionMoveParam,
    ActionScreenshotParam,
    ActionScrollParam,
    ActionTypeParam,
    ActionWaitParam,
    InputUnionMember1ResponseComputerToolCallActionActionPointAndType,
    InputUnionMember1ResponseComputerToolCallActionActionMouseDown,
    InputUnionMember1ResponseComputerToolCallActionActionMouseUp,
    InputUnionMember1ResponseComputerToolCallActionActionKeyDown,
    InputUnionMember1ResponseComputerToolCallActionActionKeyUp,
]


class InputUnionMember1ResponseComputerToolCallPendingSafetyCheck(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A pending safety check for the computer call."""

    id: Required[str]

    code: Optional[str]

    message: Optional[str]


class InputUnionMember1ResponseComputerToolCall(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A tool call to a computer use tool.

    See the
    [computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.
    """

    id: Required[str]

    action: Required[InputUnionMember1ResponseComputerToolCallAction]
    """A click action."""

    call_id: Required[str]

    pending_safety_checks: Required[Iterable[InputUnionMember1ResponseComputerToolCallPendingSafetyCheck]]

    status: Required[Literal["in_progress", "completed", "incomplete"]]

    type: Required[Literal["computer_call"]]


class InputUnionMember1ResponseReasoningItemContent(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Reasoning text from the model."""

    text: Required[str]

    type: Required[Literal["reasoning_text"]]


class InputUnionMember1ResponseReasoningItem(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """
    A description of the chain of thought used by a reasoning model while generating
    a response. Be sure to include these items in your `input` to the Responses API
    for subsequent turns of a conversation if you are manually
    [managing context](https://platform.openai.com/docs/guides/conversation-state).
    """

    id: Required[str]

    summary: Required[Iterable[SummaryParam]]

    type: Required[Literal["reasoning"]]

    content: Optional[Iterable[InputUnionMember1ResponseReasoningItemContent]]

    encrypted_content: Optional[str]

    status: Optional[Literal["in_progress", "completed", "incomplete"]]


class InputUnionMember1ResponseCompactionItem(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """
    A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).
    """

    id: Required[str]

    encrypted_content: Required[str]

    type: Required[Literal["compaction"]]

    created_by: Optional[str]


InputUnionMember1ResponseCodeInterpreterToolCallOutput: TypeAlias = Union[OutputLogsParam, OutputImageParam]


class InputUnionMember1ResponseCodeInterpreterToolCall(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A tool call to run code."""

    id: Required[str]

    container_id: Required[str]

    status: Required[Literal["in_progress", "completed", "incomplete", "interpreting", "failed"]]

    type: Required[Literal["code_interpreter_call"]]

    code: Optional[str]

    outputs: Optional[Iterable[InputUnionMember1ResponseCodeInterpreterToolCallOutput]]


class InputUnionMember1ResponseFunctionShellToolCallAction(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """The shell commands and limits that describe how to run the tool call."""

    commands: Required[SequenceNotStr[str]]

    max_output_length: Optional[int]

    timeout_ms: Optional[int]


class InputUnionMember1ResponseFunctionShellToolCall(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A tool call that executes one or more shell commands in a managed environment."""

    id: Required[str]

    action: Required[InputUnionMember1ResponseFunctionShellToolCallAction]
    """The shell commands and limits that describe how to run the tool call."""

    call_id: Required[str]

    status: Required[Literal["in_progress", "completed", "incomplete"]]

    type: Required[Literal["shell_call"]]

    created_by: Optional[str]


class InputUnionMember1ResponseFunctionShellToolCallOutputOutputOutcomeOutputOutcomeTimeout(  # type: ignore[call-arg]
    TypedDict, total=False, extra_items=object
):
    """Indicates that the shell call exceeded its configured time limit."""

    type: Required[Literal["timeout"]]


class InputUnionMember1ResponseFunctionShellToolCallOutputOutputOutcomeOutputOutcomeExit(  # type: ignore[call-arg]
    TypedDict, total=False, extra_items=object
):
    """Indicates that the shell commands finished and returned an exit code."""

    exit_code: Required[int]

    type: Required[Literal["exit"]]


InputUnionMember1ResponseFunctionShellToolCallOutputOutputOutcome: TypeAlias = Union[
    InputUnionMember1ResponseFunctionShellToolCallOutputOutputOutcomeOutputOutcomeTimeout,
    InputUnionMember1ResponseFunctionShellToolCallOutputOutputOutcomeOutputOutcomeExit,
]


class InputUnionMember1ResponseFunctionShellToolCallOutputOutput(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """The content of a shell tool call output that was emitted."""

    outcome: Required[InputUnionMember1ResponseFunctionShellToolCallOutputOutputOutcome]
    """Indicates that the shell call exceeded its configured time limit."""

    stderr: Required[str]

    stdout: Required[str]

    created_by: Optional[str]


class InputUnionMember1ResponseFunctionShellToolCallOutput(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """The output of a shell tool call that was emitted."""

    id: Required[str]

    call_id: Required[str]

    output: Required[Iterable[InputUnionMember1ResponseFunctionShellToolCallOutputOutput]]

    status: Required[Literal["in_progress", "completed", "incomplete"]]

    type: Required[Literal["shell_call_output"]]

    created_by: Optional[str]

    max_output_length: Optional[int]


class InputUnionMember1ResponseApplyPatchToolCallOperationOperationCreateFile(  # type: ignore[call-arg]
    TypedDict, total=False, extra_items=object
):
    """Instruction describing how to create a file via the apply_patch tool."""

    diff: Required[str]

    path: Required[str]

    type: Required[Literal["create_file"]]


class InputUnionMember1ResponseApplyPatchToolCallOperationOperationDeleteFile(  # type: ignore[call-arg]
    TypedDict, total=False, extra_items=object
):
    """Instruction describing how to delete a file via the apply_patch tool."""

    path: Required[str]

    type: Required[Literal["delete_file"]]


class InputUnionMember1ResponseApplyPatchToolCallOperationOperationUpdateFile(  # type: ignore[call-arg]
    TypedDict, total=False, extra_items=object
):
    """Instruction describing how to update a file via the apply_patch tool."""

    diff: Required[str]

    path: Required[str]

    type: Required[Literal["update_file"]]


InputUnionMember1ResponseApplyPatchToolCallOperation: TypeAlias = Union[
    InputUnionMember1ResponseApplyPatchToolCallOperationOperationCreateFile,
    InputUnionMember1ResponseApplyPatchToolCallOperationOperationDeleteFile,
    InputUnionMember1ResponseApplyPatchToolCallOperationOperationUpdateFile,
]


class InputUnionMember1ResponseApplyPatchToolCall(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A tool call that applies file diffs by creating, deleting, or updating files."""

    id: Required[str]

    call_id: Required[str]

    operation: Required[InputUnionMember1ResponseApplyPatchToolCallOperation]
    """Instruction describing how to create a file via the apply_patch tool."""

    status: Required[Literal["in_progress", "completed"]]

    type: Required[Literal["apply_patch_call"]]

    created_by: Optional[str]


class InputUnionMember1ResponseApplyPatchToolCallOutput(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """The output emitted by an apply patch tool call."""

    id: Required[str]

    call_id: Required[str]

    status: Required[Literal["completed", "failed"]]

    type: Required[Literal["apply_patch_call_output"]]

    created_by: Optional[str]

    output: Optional[str]


class InputUnionMember1ResponseCustomToolCall(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A call to a custom tool created by the model."""

    call_id: Required[str]

    input: Required[str]

    name: Required[str]

    type: Required[Literal["custom_tool_call"]]

    id: Optional[str]


InputUnionMember1: TypeAlias = Union[
    InputUnionMember1EasyInputMessageParam,
    InputUnionMember1Message,
    InputUnionMember1ResponseOutputMessageParam,
    InputUnionMember1ResponseFileSearchToolCallParam,
    InputUnionMember1ResponseComputerToolCallParam,
    InputUnionMember1ComputerCallOutput,
    InputUnionMember1ResponseFunctionWebSearchParam,
    InputUnionMember1ResponseFunctionToolCallParam,
    InputUnionMember1FunctionCallOutput,
    InputUnionMember1ResponseReasoningItemParam,
    InputUnionMember1ResponseCompactionItemParamParam,
    InputUnionMember1ImageGenerationCall,
    InputUnionMember1ResponseCodeInterpreterToolCallParam,
    InputUnionMember1LocalShellCall,
    InputUnionMember1LocalShellCallOutput,
    InputUnionMember1ShellCall,
    InputUnionMember1ShellCallOutput,
    InputUnionMember1ApplyPatchCall,
    InputUnionMember1ApplyPatchCallOutput,
    InputUnionMember1McpListTools,
    McpApprovalRequestParam,
    InputUnionMember1McpApprovalResponse,
    InputUnionMember1McpCall,
    InputUnionMember1ResponseCustomToolCallOutputParam,
    InputUnionMember1ResponseCustomToolCallParam,
    InputUnionMember1ItemReference,
    InputUnionMember1ResponseOutputMessage,
    InputUnionMember1ResponseFileSearchToolCall,
    InputUnionMember1ResponseFunctionToolCall,
    InputUnionMember1ResponseFunctionWebSearch,
    InputUnionMember1ResponseComputerToolCall,
    InputUnionMember1ResponseReasoningItem,
    InputUnionMember1ResponseCompactionItem,
    InputUnionMember1ImageGenerationCall,
    InputUnionMember1ResponseCodeInterpreterToolCall,
    InputUnionMember1LocalShellCall,
    InputUnionMember1ResponseFunctionShellToolCall,
    InputUnionMember1ResponseFunctionShellToolCallOutput,
    InputUnionMember1ResponseApplyPatchToolCall,
    InputUnionMember1ResponseApplyPatchToolCallOutput,
    InputUnionMember1McpCall,
    InputUnionMember1McpListTools,
    McpApprovalRequestParam,
    InputUnionMember1ResponseCustomToolCall,
]

PreviousInputMessage: TypeAlias = Union[MessageParam, Dict[str, object]]


class PromptVariablesResponseInputText(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A text input to the model."""

    text: Required[str]

    type: Required[Literal["input_text"]]


class PromptVariablesResponseInputImage(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """An image input to the model.

    Learn about [image inputs](https://platform.openai.com/docs/guides/vision).
    """

    detail: Required[Literal["low", "high", "auto"]]

    type: Required[Literal["input_image"]]

    file_id: Optional[str]

    image_url: Optional[str]


class PromptVariablesResponseInputFile(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A file input to the model."""

    type: Required[Literal["input_file"]]

    file_data: Optional[str]

    file_id: Optional[str]

    file_url: Optional[str]

    filename: Optional[str]


PromptVariables: TypeAlias = Union[
    str, PromptVariablesResponseInputText, PromptVariablesResponseInputImage, PromptVariablesResponseInputFile
]


class Prompt(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """
    Reference to a prompt template and its variables.
    [Learn more](https://platform.openai.com/docs/guides/text?api-mode=responses#reusable-prompts).
    """

    id: Required[str]

    variables: Optional[Dict[str, PromptVariables]]

    version: Optional[str]


class Reasoning(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """**gpt-5 and o-series models only**

    Configuration options for
    [reasoning models](https://platform.openai.com/docs/guides/reasoning).
    """

    effort: Optional[Literal["none", "minimal", "low", "medium", "high", "xhigh"]]

    generate_summary: Optional[Literal["auto", "concise", "detailed"]]

    summary: Optional[Literal["auto", "concise", "detailed"]]


class TextFormatResponseFormatText(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Default response format. Used to generate text responses."""

    type: Required[Literal["text"]]


class TextFormatResponseFormatTextJsonSchemaConfig(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """JSON Schema response format.

    Used to generate structured JSON responses.
    Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).
    """

    name: Required[str]

    schema: Required[Dict[str, object]]

    type: Required[Literal["json_schema"]]

    description: Optional[str]

    strict: Optional[bool]


class TextFormatResponseFormatJsonObject(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """JSON object response format.

    An older method of generating JSON responses.
    Using `json_schema` is recommended for models that support it. Note that the
    model will not generate JSON without a system or user message instructing it
    to do so.
    """

    type: Required[Literal["json_object"]]


TextFormat: TypeAlias = Union[
    TextFormatResponseFormatText, TextFormatResponseFormatTextJsonSchemaConfig, TextFormatResponseFormatJsonObject
]


class Text(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Configuration options for a text response from the model.

    Can be plain
    text or structured JSON data. Learn more:
    - [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
    - [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)
    """

    format: Optional[TextFormat]
    """Default response format. Used to generate text responses."""

    verbosity: Optional[Literal["low", "medium", "high"]]


class ToolChoiceToolChoiceAllowed(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Constrains the tools available to the model to a pre-defined set."""

    mode: Required[Literal["auto", "required"]]

    tools: Required[Iterable[Dict[str, object]]]

    type: Required[Literal["allowed_tools"]]


class ToolChoiceToolChoiceTypes(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """
    Indicates that the model should use a built-in tool to generate a response.
    [Learn more about built-in tools](https://platform.openai.com/docs/guides/tools).
    """

    type: Required[
        Literal[
            "file_search",
            "web_search_preview",
            "computer_use_preview",
            "web_search_preview_2025_03_11",
            "image_generation",
            "code_interpreter",
        ]
    ]


class ToolChoiceToolChoiceFunction(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Use this option to force the model to call a specific function."""

    name: Required[str]

    type: Required[Literal["function"]]


class ToolChoiceToolChoiceMcp(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """
    Use this option to force the model to call a specific tool on a remote MCP server.
    """

    server_label: Required[str]

    type: Required[Literal["mcp"]]

    name: Optional[str]


class ToolChoiceToolChoiceCustom(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Use this option to force the model to call a specific custom tool."""

    name: Required[str]

    type: Required[Literal["custom"]]


class ToolChoiceToolChoiceApplyPatch(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Forces the model to call the apply_patch tool when executing a tool call."""

    type: Required[Literal["apply_patch"]]


class ToolChoiceToolChoiceShell(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Forces the model to call the shell tool when a tool call is required."""

    type: Required[Literal["shell"]]


ToolChoice: TypeAlias = Union[
    Literal["none", "auto", "required"],
    ToolChoiceToolChoiceAllowed,
    ToolChoiceToolChoiceTypes,
    ToolChoiceToolChoiceFunction,
    ToolChoiceToolChoiceMcp,
    ToolChoiceToolChoiceCustom,
    ToolChoiceToolChoiceApplyPatch,
    ToolChoiceToolChoiceShell,
]


class ToolFunctionTool(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Defines a function in your own code the model can choose to call.

    Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).
    """

    name: Required[str]

    type: Required[Literal["function"]]

    description: Optional[str]

    parameters: Optional[Dict[str, object]]

    strict: Optional[bool]


ToolFileSearchToolFiltersCompoundFilterFilter: TypeAlias = Union[ComparisonFilterParam, object]


class ToolFileSearchToolFiltersCompoundFilter(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Combine multiple filters using `and` or `or`."""

    filters: Required[Iterable[ToolFileSearchToolFiltersCompoundFilterFilter]]

    type: Required[Literal["and", "or"]]


ToolFileSearchToolFilters: TypeAlias = Union[ComparisonFilterParam, ToolFileSearchToolFiltersCompoundFilter]


class ToolFileSearchToolRankingOptionsHybridSearch(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """
    Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.
    """

    embedding_weight: Required[float]

    text_weight: Required[float]


class ToolFileSearchToolRankingOptions(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Ranking options for search."""

    hybrid_search: Optional[ToolFileSearchToolRankingOptionsHybridSearch]
    """
    Weights that control how reciprocal rank fusion balances semantic embedding
    matches versus sparse keyword matches when hybrid search is enabled.
    """

    ranker: Optional[Literal["auto", "default-2024-11-15"]]

    score_threshold: Optional[float]


class ToolFileSearchTool(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A tool that searches for relevant content from uploaded files.

    Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).
    """

    type: Required[Literal["file_search"]]

    vector_store_ids: Required[SequenceNotStr[str]]

    filters: Optional[ToolFileSearchToolFilters]
    """
    A filter used to compare a specified attribute key to a given value using a
    defined comparison operation.
    """

    max_num_results: Optional[int]

    ranking_options: Optional[ToolFileSearchToolRankingOptions]
    """Ranking options for search."""


class ToolComputerTool(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A tool that controls a virtual computer.

    Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).
    """

    display_height: Required[int]

    display_width: Required[int]

    environment: Required[Literal["windows", "mac", "linux", "ubuntu", "browser"]]

    type: Required[Literal["computer_use_preview"]]


class ToolWebSearchToolFilters(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Filters for the search."""

    allowed_domains: Optional[SequenceNotStr[str]]


class ToolWebSearchToolUserLocation(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """The approximate location of the user."""

    city: Optional[str]

    country: Optional[str]

    region: Optional[str]

    timezone: Optional[str]

    type: Optional[Literal["approximate"]]


class ToolWebSearchTool(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Search the Internet for sources related to the prompt.

    Learn more about the
    [web search tool](https://platform.openai.com/docs/guides/tools-web-search).
    """

    type: Required[Literal["web_search", "web_search_2025_08_26"]]

    filters: Optional[ToolWebSearchToolFilters]
    """Filters for the search."""

    search_context_size: Optional[Literal["low", "medium", "high"]]

    user_location: Optional[ToolWebSearchToolUserLocation]
    """The approximate location of the user."""


class ToolMcpAllowedToolsMcpAllowedToolsMcpToolFilter(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A filter object to specify which tools are allowed."""

    read_only: Optional[bool]

    tool_names: Optional[SequenceNotStr[str]]


ToolMcpAllowedTools: TypeAlias = Union[SequenceNotStr[str], ToolMcpAllowedToolsMcpAllowedToolsMcpToolFilter]


class ToolMcpRequireApprovalMcpRequireApprovalMcpToolApprovalFilterAlways(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A filter object to specify which tools are allowed."""

    read_only: Optional[bool]

    tool_names: Optional[SequenceNotStr[str]]


class ToolMcpRequireApprovalMcpRequireApprovalMcpToolApprovalFilterNever(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A filter object to specify which tools are allowed."""

    read_only: Optional[bool]

    tool_names: Optional[SequenceNotStr[str]]


class ToolMcpRequireApprovalMcpRequireApprovalMcpToolApprovalFilter(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Specify which of the MCP server's tools require approval.

    Can be
    `always`, `never`, or a filter object associated with tools
    that require approval.
    """

    always: Optional[ToolMcpRequireApprovalMcpRequireApprovalMcpToolApprovalFilterAlways]
    """A filter object to specify which tools are allowed."""

    never: Optional[ToolMcpRequireApprovalMcpRequireApprovalMcpToolApprovalFilterNever]
    """A filter object to specify which tools are allowed."""


ToolMcpRequireApproval: TypeAlias = Union[
    ToolMcpRequireApprovalMcpRequireApprovalMcpToolApprovalFilter, Literal["always", "never"]
]


class ToolMcp(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """
    Give the model access to additional tools via remote Model Context Protocol
    (MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).
    """

    server_label: Required[str]

    type: Required[Literal["mcp"]]

    allowed_tools: Optional[ToolMcpAllowedTools]
    """A filter object to specify which tools are allowed."""

    authorization: Optional[str]

    connector_id: Optional[
        Literal[
            "connector_dropbox",
            "connector_gmail",
            "connector_googlecalendar",
            "connector_googledrive",
            "connector_microsoftteams",
            "connector_outlookcalendar",
            "connector_outlookemail",
            "connector_sharepoint",
        ]
    ]

    headers: Optional[Dict[str, str]]

    require_approval: Optional[ToolMcpRequireApproval]
    """Specify which of the MCP server's tools require approval.

    Can be `always`, `never`, or a filter object associated with tools that require
    approval.
    """

    server_description: Optional[str]

    server_url: Optional[str]


class ToolCodeInterpreterContainerCodeInterpreterContainerCodeInterpreterToolAuto(  # type: ignore[call-arg]
    TypedDict, total=False, extra_items=object
):
    """Configuration for a code interpreter container.

    Optionally specify the IDs of the files to run the code on.
    """

    type: Required[Literal["auto"]]

    file_ids: Optional[SequenceNotStr[str]]

    memory_limit: Optional[Literal["1g", "4g", "16g", "64g"]]


ToolCodeInterpreterContainer: TypeAlias = Union[
    str, ToolCodeInterpreterContainerCodeInterpreterContainerCodeInterpreterToolAuto
]


class ToolCodeInterpreter(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A tool that runs Python code to help generate a response to a prompt."""

    container: Required[ToolCodeInterpreterContainer]
    """Configuration for a code interpreter container.

    Optionally specify the IDs of the files to run the code on.
    """

    type: Required[Literal["code_interpreter"]]


class ToolImageGenerationInputImageMask(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Optional mask for inpainting.

    Contains `image_url`
    (string, optional) and `file_id` (string, optional).
    """

    file_id: Optional[str]

    image_url: Optional[str]


class ToolImageGeneration(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A tool that generates images using the GPT image models."""

    type: Required[Literal["image_generation"]]

    background: Optional[Literal["transparent", "opaque", "auto"]]

    input_fidelity: Optional[Literal["high", "low"]]

    input_image_mask: Optional[ToolImageGenerationInputImageMask]
    """Optional mask for inpainting.

    Contains `image_url` (string, optional) and `file_id` (string, optional).
    """

    model: Union[str, Literal["gpt-image-1", "gpt-image-1-mini"], None]

    moderation: Optional[Literal["auto", "low"]]

    output_compression: Optional[int]

    output_format: Optional[Literal["png", "webp", "jpeg"]]

    partial_images: Optional[int]

    quality: Optional[Literal["low", "medium", "high", "auto"]]

    size: Optional[Literal["1024x1024", "1024x1536", "1536x1024", "auto"]]


class ToolLocalShell(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A tool that allows the model to execute shell commands in a local environment."""

    type: Required[Literal["local_shell"]]


class ToolFunctionShellTool(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A tool that allows the model to execute shell commands."""

    type: Required[Literal["shell"]]


class ToolCustomToolFormatText(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Unconstrained free-form text."""

    type: Required[Literal["text"]]


class ToolCustomToolFormatGrammar(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A grammar defined by the user."""

    definition: Required[str]

    syntax: Required[Literal["lark", "regex"]]

    type: Required[Literal["grammar"]]


ToolCustomToolFormat: TypeAlias = Union[ToolCustomToolFormatText, ToolCustomToolFormatGrammar]


class ToolCustomTool(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A custom tool that processes input using a specified format.

    Learn more about   [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)
    """

    name: Required[str]

    type: Required[Literal["custom"]]

    description: Optional[str]

    format: Optional[ToolCustomToolFormat]
    """Unconstrained free-form text."""


class ToolWebSearchPreviewToolUserLocation(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """The user's location."""

    type: Required[Literal["approximate"]]

    city: Optional[str]

    country: Optional[str]

    region: Optional[str]

    timezone: Optional[str]


class ToolWebSearchPreviewTool(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """This tool searches the web for relevant results to use in a response.

    Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).
    """

    type: Required[Literal["web_search_preview", "web_search_preview_2025_03_11"]]

    search_context_size: Optional[Literal["low", "medium", "high"]]

    user_location: Optional[ToolWebSearchPreviewToolUserLocation]
    """The user's location."""


class ToolApplyPatchTool(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Allows the assistant to create, delete, or update files using unified diffs."""

    type: Required[Literal["apply_patch"]]


Tool: TypeAlias = Union[
    ToolFunctionTool,
    ToolFileSearchTool,
    ToolComputerTool,
    ToolWebSearchTool,
    ToolMcp,
    ToolCodeInterpreter,
    ToolImageGeneration,
    ToolLocalShell,
    ToolFunctionShellTool,
    ToolCustomTool,
    ToolWebSearchPreviewTool,
    ToolApplyPatchTool,
]
