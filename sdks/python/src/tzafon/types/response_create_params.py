# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, TypedDict

from .content_block_param import ContentBlockParam

__all__ = ["ResponseCreateParams", "Input", "Tool"]


class ResponseCreateParams(TypedDict, total=False):
    input: Iterable[Input]

    instructions: str

    max_output_tokens: int

    model: str

    previous_response_id: str

    stream: bool

    temperature: float

    tools: Iterable[Tool]

    top_p: float


class Input(TypedDict, total=False):
    call_id: str

    content: Iterable[ContentBlockParam]

    output: ContentBlockParam

    role: str

    type: Literal["computer_call_output"]


class Tool(TypedDict, total=False):
    display_height: int

    display_width: int

    environment: str

    type: Literal["computer_use"]
