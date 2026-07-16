# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .logprob_param import LogprobParam
from .annotation_file_path_param import AnnotationFilePathParam
from .annotation_url_citation_param import AnnotationURLCitationParam
from .annotation_file_citation_param import AnnotationFileCitationParam
from .annotation_container_file_citation_param import AnnotationContainerFileCitationParam

__all__ = ["ResponseOutputTextParam", "Annotation"]

Annotation: TypeAlias = Union[
    AnnotationFileCitationParam,
    AnnotationURLCitationParam,
    AnnotationContainerFileCitationParam,
    AnnotationFilePathParam,
]


class ResponseOutputTextParam(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    """A text output from the model."""

    annotations: Required[Iterable[Annotation]]

    text: Required[str]

    type: Required[Literal["output_text"]]

    logprobs: Optional[Iterable[LogprobParam]]
