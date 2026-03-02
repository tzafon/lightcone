# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .computer_action_param import ComputerActionParam

__all__ = ["ComputerExecuteParams"]


class ComputerExecuteParams(TypedDict, total=False):
    action: ComputerActionParam
