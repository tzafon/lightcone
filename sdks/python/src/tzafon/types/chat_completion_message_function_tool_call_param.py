# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ChatCompletionMessageFunctionToolCallParam", "Function"]


class Function(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """The function that the model called."""

    arguments: Required[str]

    name: Required[str]


class ChatCompletionMessageFunctionToolCallParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A call to a function tool created by the model."""

    id: Required[str]

    function: Required[Function]
    """The function that the model called."""

    type: Required[Literal["function"]]
