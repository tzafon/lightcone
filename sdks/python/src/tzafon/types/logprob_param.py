# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["LogprobParam", "TopLogprob"]


class TopLogprob(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """The top log probability of a token."""

    token: Required[str]

    bytes: Required[Iterable[int]]

    logprob: Required[float]


class LogprobParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """The log probability of a token."""

    token: Required[str]

    bytes: Required[Iterable[int]]

    logprob: Required[float]

    top_logprobs: Required[Iterable[TopLogprob]]
