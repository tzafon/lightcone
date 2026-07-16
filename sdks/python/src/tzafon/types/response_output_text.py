# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .logprob import Logprob
from .._models import BaseModel
from .annotation_file_path import AnnotationFilePath
from .annotation_url_citation import AnnotationURLCitation
from .annotation_file_citation import AnnotationFileCitation
from .annotation_container_file_citation import AnnotationContainerFileCitation

__all__ = ["ResponseOutputText", "Annotation"]

Annotation: TypeAlias = Union[
    AnnotationFileCitation, AnnotationURLCitation, AnnotationContainerFileCitation, AnnotationFilePath
]


class ResponseOutputText(BaseModel):
    """A text output from the model."""

    annotations: List[Annotation]

    text: str

    type: Literal["output_text"]

    logprobs: Optional[List[Logprob]] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]
