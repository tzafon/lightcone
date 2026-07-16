# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .response_output_message import ResponseOutputMessage
from .response_computer_tool_call import ResponseComputerToolCall
from .response_function_tool_call import ResponseFunctionToolCall

__all__ = ["ResponseCreateResponse", "Output", "Usage"]

Output: TypeAlias = Union[ResponseOutputMessage, ResponseFunctionToolCall, ResponseComputerToolCall, Dict[str, object]]


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
