# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["ComputerResponse"]


class ComputerResponse(BaseModel):
    id: Optional[str] = None

    auto_kill: Optional[bool] = None

    created_at: Optional[str] = None

    endpoints: Optional[Dict[str, str]] = None

    expires_at: Optional[str] = None

    idle_expires_at: Optional[str] = None

    inactivity_timeout_seconds: Optional[int] = None

    kind: Optional[str] = None

    last_activity_at: Optional[str] = None

    max_lifetime_seconds: Optional[int] = None

    status: Optional[str] = None
