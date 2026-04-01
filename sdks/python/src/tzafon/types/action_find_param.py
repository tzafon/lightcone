# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ActionFindParam"]


class ActionFindParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Action type "find": Searches for a pattern within a loaded page."""

    pattern: Required[str]

    type: Required[Literal["find"]]

    url: Required[str]
