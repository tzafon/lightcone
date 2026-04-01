# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AnnotationContainerFileCitationParam"]


class AnnotationContainerFileCitationParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A citation for a container file used to generate a model response."""

    container_id: Required[str]

    end_index: Required[int]

    file_id: Required[str]

    filename: Required[str]

    start_index: Required[int]

    type: Required[Literal["container_file_citation"]]
