# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["TaskStartResponse"]


class TaskStartResponse(BaseModel):
    status: Optional[str] = None

    task_id: Optional[str] = None
