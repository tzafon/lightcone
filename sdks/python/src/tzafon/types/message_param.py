# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MessageParam", "Author"]


class Author(TypedDict, total=False):
    role: Required[Literal["user", "assistant", "system", "developer", "tool"]]
    """The role of a message author (mirrors `chat::Role`)."""

    name: Optional[str]


class MessageParam(TypedDict, total=False):
    author: Required[Author]

    channel: Optional[str]

    content: Iterable[object]

    content_type: Optional[str]

    recipient: Optional[str]
