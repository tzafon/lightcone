# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["FileParam", "File"]


class File(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    file_data: str

    file_id: str

    filename: str


class FileParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """
    Learn about [file inputs](https://platform.openai.com/docs/guides/text) for text generation.
    """

    file: Required[File]

    type: Required[Literal["file"]]
