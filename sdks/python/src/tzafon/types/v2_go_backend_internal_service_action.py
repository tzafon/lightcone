# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["V2GoBackendInternalServiceAction"]


class V2GoBackendInternalServiceAction(BaseModel):
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
            "mouse_down",
            "mouse_up",
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
