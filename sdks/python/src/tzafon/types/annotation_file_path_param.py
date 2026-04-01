# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AnnotationFilePathParam"]


class AnnotationFilePathParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A path to a file."""

    file_id: Required[str]

    index: Required[int]

    type: Required[Literal["file_path"]]
