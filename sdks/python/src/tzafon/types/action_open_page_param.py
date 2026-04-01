# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ActionOpenPageParam"]


class ActionOpenPageParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Action type "open_page" - Opens a specific URL from search results."""

    type: Required[Literal["open_page"]]

    url: Required[str]
