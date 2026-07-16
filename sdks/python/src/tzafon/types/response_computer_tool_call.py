# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .action_drag import ActionDrag
from .action_move import ActionMove
from .action_type import ActionType
from .action_wait import ActionWait
from .action_click import ActionClick
from .action_key_up import ActionKeyUp
from .action_scroll import ActionScroll
from .action_key_down import ActionKeyDown
from .action_keypress import ActionKeypress
from .action_mouse_up import ActionMouseUp
from .action_mouse_down import ActionMouseDown
from .action_screenshot import ActionScreenshot
from .action_double_click import ActionDoubleClick
from .pending_safety_check import PendingSafetyCheck
from .action_point_and_type import ActionPointAndType

__all__ = ["ResponseComputerToolCall", "Action"]

Action: TypeAlias = Union[
    ActionClick,
    ActionDoubleClick,
    ActionDrag,
    ActionKeypress,
    ActionMove,
    ActionScreenshot,
    ActionScroll,
    ActionType,
    ActionWait,
    ActionPointAndType,
    ActionMouseDown,
    ActionMouseUp,
    ActionKeyDown,
    ActionKeyUp,
]


class ResponseComputerToolCall(BaseModel):
    """A tool call to a computer use tool.

    See the
    [computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.
    """

    id: str

    action: Action
    """A click action."""

    call_id: str

    pending_safety_checks: List[PendingSafetyCheck]

    status: Literal["in_progress", "completed", "incomplete"]

    type: Literal["computer_call"]

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]
