# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ComputerCreateParams", "Display"]


class ComputerCreateParams(TypedDict, total=False):
    auto_kill: bool
    """If true (default), kill session after inactivity"""

    context_id: str

    display: Display

    environment_id: str

    inactivity_timeout_seconds: int
    """Idle timeout before auto-kill"""

    kind: str
    """\"browser" (default) or "desktop" """

    persistent: bool
    """Persist cookies/storage state to DB on session teardown only if true"""

    stealth: object

    timeout_seconds: int

    use_advanced_proxy: bool
    """If true (browser sessions), use ADVANCED_PROXY_URL on session start"""


class Display(TypedDict, total=False):
    height: int

    scale: float

    width: int
