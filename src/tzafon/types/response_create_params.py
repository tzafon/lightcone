# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, TypedDict

__all__ = ["ResponseCreateParams", "Tool"]


class ResponseCreateParams(TypedDict, total=False):
    instructions: str

    max_output_tokens: int

    model: str

    previous_response_id: str

    stream: bool

    temperature: float

    tools: Iterable[Tool]

    top_p: float


class Tool(TypedDict, total=False):
    display_height: int

    display_width: int

    environment: str

    type: Literal["computer_use"]
