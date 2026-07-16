# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ActionPointAndTypeParam"]


class ActionPointAndTypeParam(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    """Click at a position then type text."""

    text: Required[str]

    type: Required[Literal["point_and_type"]]

    x: Required[int]

    y: Required[int]
