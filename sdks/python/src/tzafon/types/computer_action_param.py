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

    from_shm: bool
    """
    FromShm (screenshot only) asks the guest to serve the screenshot from the
    capture loop's latest frame instead of a fresh full-grab. Desktop VM sessions
    only; falls back to full-grab if no frame is available.
    """

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

    screenshot_after: bool
    """
    ScreenshotAfter, when true, asks the engine to capture a screenshot immediately
    after the action and return its URL in the same response (act+observe in one
    round-trip). Feature-flagged, defaults off.
    """

    scroll_x: float
    """
    OpenAI CUA-spec aliases for the same data; used as fallbacks when
    dx/dy/x1/y1/x2/y2 are absent on the request.
    """

    scroll_y: float

    settle_ms: int
    """
    SettleMs overrides, per-action, the settle time (ms) the guest waits between
    input sub-steps. Absent => guest process default. Lower = faster but riskier on
    slow-rendering targets.
    """

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
