# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ActionMoveParam"]


class ActionMoveParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A mouse move action."""

    type: Required[Literal["move"]]

    x: Required[int]

    y: Required[int]
