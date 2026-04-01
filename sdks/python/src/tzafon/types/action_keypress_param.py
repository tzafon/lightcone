# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["ActionKeypressParam"]


class ActionKeypressParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A collection of keypresses the model would like to perform."""

    keys: Required[SequenceNotStr[str]]

    type: Required[Literal["keypress"]]
