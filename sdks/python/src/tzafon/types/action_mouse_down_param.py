# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ActionMouseDownParam"]


class ActionMouseDownParam(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    """Press and hold the left mouse button at a position."""

    type: Required[Literal["mouse_down"]]

    x: Required[int]

    y: Required[int]
