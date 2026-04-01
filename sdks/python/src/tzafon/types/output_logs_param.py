# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["OutputLogsParam"]


class OutputLogsParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """The logs output from the code interpreter."""

    logs: Required[str]

    type: Required[Literal["logs"]]
