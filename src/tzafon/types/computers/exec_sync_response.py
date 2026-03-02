# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ExecSyncResponse"]


class ExecSyncResponse(BaseModel):
    exit_code: Optional[int] = None

    stderr: Optional[str] = None

    stdout: Optional[str] = None
