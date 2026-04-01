# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AnnotationURLCitationParam"]


class AnnotationURLCitationParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A citation for a web resource used to generate a model response."""

    end_index: Required[int]

    start_index: Required[int]

    title: Required[str]

    type: Required[Literal["url_citation"]]

    url: Required[str]
