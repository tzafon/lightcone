# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["ComparisonFilterParam"]


class ComparisonFilterParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """
    A filter used to compare a specified attribute key to a given value using a defined comparison operation.
    """

    key: Required[str]

    type: Required[Literal["eq", "ne", "gt", "gte", "lt", "lte"]]

    value: Required[Union[str, float, bool, SequenceNotStr[Union[str, float]]]]
