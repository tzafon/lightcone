# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["ExecExecuteSyncParams"]


class ExecExecuteSyncParams(TypedDict, total=False):
    command: str

    cwd: str

    env: Dict[str, str]

    timeout_seconds: int
