# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AnnotationFileCitationParam"]


class AnnotationFileCitationParam(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    """A citation to a file."""

    file_id: Required[str]

    filename: Required[str]

    index: Required[int]

    type: Required[Literal["file_citation"]]
