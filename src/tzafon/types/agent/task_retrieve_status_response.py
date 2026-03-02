# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["TaskRetrieveStatusResponse"]


class TaskRetrieveStatusResponse(BaseModel):
    exit_code: Optional[int] = None

    status: Optional[str] = None

    task_id: Optional[str] = None
