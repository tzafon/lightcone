# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .logprob import Logprob
from .._models import BaseModel
from .action_drag import ActionDrag
from .action_move import ActionMove
from .action_type import ActionType
from .action_wait import ActionWait
from .action_click import ActionClick
from .action_scroll import ActionScroll
from .action_keypress import ActionKeypress
from .action_screenshot import ActionScreenshot
from .action_double_click import ActionDoubleClick
from .annotation_file_path import AnnotationFilePath
from .annotation_url_citation import AnnotationURLCitation
from .annotation_file_citation import AnnotationFileCitation
from .annotation_container_file_citation import AnnotationContainerFileCitation

__all__ = [
    "ResponseCreateResponse",
    "Output",
    "OutputResponseOutputMessage",
    "OutputResponseOutputMessageContent",
    "OutputResponseOutputMessageContentResponseOutputText",
    "OutputResponseOutputMessageContentResponseOutputTextAnnotation",
    "OutputResponseOutputMessageContentResponseOutputRefusal",
    "OutputResponseFunctionToolCall",
    "OutputResponseComputerToolCall",
    "OutputResponseComputerToolCallAction",
    "OutputResponseComputerToolCallPendingSafetyCheck",
    "Usage",
]

OutputResponseOutputMessageContentResponseOutputTextAnnotation: TypeAlias = Union[
    AnnotationFileCitation, AnnotationURLCitation, AnnotationContainerFileCitation, AnnotationFilePath
]


class OutputResponseOutputMessageContentResponseOutputText(BaseModel):
    """A text output from the model."""

    annotations: List[OutputResponseOutputMessageContentResponseOutputTextAnnotation]

    text: str

    type: Literal["output_text"]

    logprobs: Optional[List[Logprob]] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class OutputResponseOutputMessageContentResponseOutputRefusal(BaseModel):
    """A refusal from the model."""

    refusal: str

    type: Literal["refusal"]

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


OutputResponseOutputMessageContent: TypeAlias = Union[
    OutputResponseOutputMessageContentResponseOutputText, OutputResponseOutputMessageContentResponseOutputRefusal
]


class OutputResponseOutputMessage(BaseModel):
    """An output message from the model."""

    id: str

    content: List[OutputResponseOutputMessageContent]

    role: Literal["assistant"]

    status: Literal["in_progress", "completed", "incomplete"]

    type: Literal["message"]

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class OutputResponseFunctionToolCall(BaseModel):
    """A tool call to run a function.

    See the
    [function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.
    """

    arguments: str

    call_id: str

    name: str

    type: Literal["function_call"]

    id: Optional[str] = None

    status: Optional[Literal["in_progress", "completed", "incomplete"]] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


OutputResponseComputerToolCallAction: TypeAlias = Union[
    ActionClick,
    ActionDoubleClick,
    ActionDrag,
    ActionKeypress,
    ActionMove,
    ActionScreenshot,
    ActionScroll,
    ActionType,
    ActionWait,
]


class OutputResponseComputerToolCallPendingSafetyCheck(BaseModel):
    """A pending safety check for the computer call."""

    id: str

    code: Optional[str] = None

    message: Optional[str] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class OutputResponseComputerToolCall(BaseModel):
    """A tool call to a computer use tool.

    See the
    [computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.
    """

    id: str

    action: OutputResponseComputerToolCallAction
    """A click action."""

    call_id: str

    pending_safety_checks: List[OutputResponseComputerToolCallPendingSafetyCheck]

    status: Literal["in_progress", "completed", "incomplete"]

    type: Literal["computer_call"]

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


Output: TypeAlias = Union[
    OutputResponseOutputMessage, OutputResponseFunctionToolCall, OutputResponseComputerToolCall, Dict[str, object]
]


class Usage(BaseModel):
    input_tokens: Optional[int] = None

    output_tokens: Optional[int] = None

    total_tokens: Optional[int] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class ResponseCreateResponse(BaseModel):
    """The response object returned by the Responses API."""

    id: str

    created_at: int

    model: str

    object: Literal["response"]

    output: List[Output]

    status: Literal["completed", "failed", "in_progress", "incomplete", "cancelled"]

    error: Optional[Dict[str, builtins.object]] = None

    tools: Optional[List[Dict[str, builtins.object]]] = None

    usage: Optional[Usage] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, builtins.object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> builtins.object: ...
    else:
        __pydantic_extra__: Dict[str, builtins.object]
