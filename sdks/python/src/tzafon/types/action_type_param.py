# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ActionTypeParam"]


class ActionTypeParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """An action to type in text."""

    text: Required[str]

    type: Required[Literal["type"]]
