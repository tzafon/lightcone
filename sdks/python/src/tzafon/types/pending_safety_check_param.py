# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["PendingSafetyCheckParam"]


class PendingSafetyCheckParam(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    """A pending safety check for the computer call."""

    id: Required[str]

    code: Optional[str]

    message: Optional[str]
