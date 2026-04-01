# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ActionScrollParam"]


class ActionScrollParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A scroll action."""

    scroll_x: Required[int]

    scroll_y: Required[int]

    type: Required[Literal["scroll"]]

    x: Required[int]

    y: Required[int]
