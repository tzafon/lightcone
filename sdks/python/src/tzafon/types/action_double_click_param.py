# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ActionDoubleClickParam"]


class ActionDoubleClickParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A double click action."""

    type: Required[Literal["double_click"]]

    x: Required[int]

    y: Required[int]
