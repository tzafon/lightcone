# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["ComputerActionParam", "Debug", "Path"]


class Debug(TypedDict, total=False):
    command: str

    cwd: str

    env: Dict[str, str]

    max_output_length: int

    stream: bool

    timeout_seconds: int


class Path(TypedDict, total=False):
    x: float

    y: float


class ComputerActionParam(TypedDict, total=False):
    auto_detect_encoding: bool
    """For get_html_content"""

    base64: bool
    """For screenshot"""

    button: str

    debug: Debug

    dx: float
    """For scrolling"""

    dy: float

    height: int

    include_context: bool
    """Include page context in response"""

    key: str
    """For key_down/key_up"""

    keys: SequenceNotStr[str]

    ms: int

    path: Iterable[Path]

    proxy_url: str

    request_id: str
    """RequestId correlates streaming output to the originating request.

    Set at the top level of the action envelope, not on individual action types.
    """

    scale_factor: float

    scroll_x: float
    """
    OpenAI CUA-spec aliases for the same data; used as fallbacks when
    dx/dy/x1/y1/x2/y2 are absent on the request.
    """

    scroll_y: float

    tab_id: str
    """For tab management (browser sessions only)"""

    text: str

    type: str
    """
    click|double_click|right_click|drag|type|keypress|scroll|wait|screenshot|go_to_url|debug|get_html_content|set_viewport|list_tabs|new_tab|switch_tab|close_tab|key_down|key_up|mouse_down|mouse_up
    """

    url: str

    width: int
    """For set_viewport"""

    x: float

    x1: float
    """For dragging/scrolling"""

    x2: float
    """For dragging"""

    y: float

    y1: float

    y2: float
