# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ActionDragParam", "Path"]


class Path(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """An x/y coordinate pair, e.g. `{ x: 100, y: 200 }`."""

    x: Required[int]

    y: Required[int]


class ActionDragParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A drag action."""

    path: Required[Iterable[Path]]

    type: Required[Literal["drag"]]
