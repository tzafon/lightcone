# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .content_block import ContentBlock

__all__ = ["ResponsesResponse", "Output", "OutputAction", "Usage", "Viewport"]


class OutputAction(BaseModel):
    button: Optional[str] = None

    end_x: Optional[int] = None

    end_y: Optional[int] = None

    keys: Optional[List[str]] = None

    result: Optional[str] = None

    scroll_x: Optional[int] = None

    scroll_y: Optional[int] = None

    status: Optional[str] = None

    text: Optional[str] = None

    type: Optional[
        Literal[
            "click",
            "double_click",
            "triple_click",
            "right_click",
            "type",
            "key",
            "keypress",
            "key_down",
            "key_up",
            "scroll",
            "hscroll",
            "navigate",
            "drag",
            "wait",
            "terminate",
            "answer",
            "done",
        ]
    ] = None

    url: Optional[str] = None

    x: Optional[int] = None

    y: Optional[int] = None


class Output(BaseModel):
    id: Optional[str] = None

    action: Optional[OutputAction] = None

    call_id: Optional[str] = None

    content: Optional[List[ContentBlock]] = None

    role: Optional[str] = None

    status: Optional[str] = None

    summary: Optional[List[ContentBlock]] = None

    type: Optional[Literal["reasoning", "computer_call", "computer_call_output", "message"]] = None


class Usage(BaseModel):
    input_tokens: Optional[int] = None

    output_tokens: Optional[int] = None

    total_tokens: Optional[int] = None


class Viewport(BaseModel):
    environment: Optional[str] = None

    height: Optional[int] = None

    width: Optional[int] = None


class ResponsesResponse(BaseModel):
    id: Optional[str] = None

    computer_id: Optional[str] = None

    created_at: Optional[str] = None

    max_output_tokens: Optional[int] = None

    model: Optional[str] = None

    object: Optional[str] = None

    output: Optional[List[Output]] = None

    status: Optional[str] = None

    temperature: Optional[float] = None

    top_p: Optional[float] = None

    usage: Optional[Usage] = None

    viewport: Optional[Viewport] = None
