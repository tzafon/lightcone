# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ExecExecuteResponse"]


class ExecExecuteResponse(BaseModel):
    code: Optional[int] = None
    """for exit"""

    data: Optional[str] = None
    """for stdout/stderr"""

    message: Optional[str] = None
    """for error"""

    type: Optional[str] = None
    """\"stdout", "stderr", "exit", "error" """
