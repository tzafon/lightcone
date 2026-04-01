# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SummaryParam"]


class SummaryParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A summary text from the model."""

    text: Required[str]

    type: Required[Literal["summary_text"]]
