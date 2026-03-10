# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from .computer_action_param import ComputerActionParam

__all__ = ["ComputerBatchParams"]


class ComputerBatchParams(TypedDict, total=False):
    actions: Iterable[ComputerActionParam]
