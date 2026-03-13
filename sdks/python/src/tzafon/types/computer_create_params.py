# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ComputerCreateParams", "Display"]


class ComputerCreateParams(TypedDict, total=False):
    auto_kill: bool
    """Deprecated: use idle_timeout_enabled"""

    context_id: str

    display: Display

    environment_id: str

    idle_timeout_enabled: bool
    """If true (default), kill session after inactivity"""

    inactivity_timeout_seconds: int
    """Idle timeout before kill"""

    kind: str
    """\"browser" (default) or "desktop" """

    max_lifetime_seconds: int
    """Max session duration in seconds"""

    persistent: bool
    """Persist cookies/storage state to DB on session teardown only if true"""

    stealth: object

    timeout_seconds: int
    """Deprecated: use max_lifetime_seconds"""

    use_advanced_proxy: bool
    """If true (browser sessions), use ADVANCED_PROXY_URL on session start"""


class Display(TypedDict, total=False):
    height: int

    scale: float

    width: int
