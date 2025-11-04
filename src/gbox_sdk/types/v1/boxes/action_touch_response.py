# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "ActionTouchResponse",
    "Actual",
    "ActualPoint",
    "ActualPointStart",
    "ActualPointAction",
    "ActualPointActionTouchPointMoveAction",
    "ActualPointActionTouchPointWaitAction",
    "Screenshot",
    "ScreenshotAfter",
    "ScreenshotBefore",
    "ScreenshotTrace",
]


class ActualPointStart(BaseModel):
    x: float
    """Starting X coordinate"""

    y: float
    """Starting Y coordinate"""


class ActualPointActionTouchPointMoveAction(BaseModel):
    duration: str
    """Duration of the movement (e.g. "200ms")

    Supported time units: ms (milliseconds), s (seconds), m (minutes), h (hours)
    Example formats: "500ms", "30s", "5m", "1h" Default: 200ms
    """

    type: str
    """Type of the action"""

    x: float
    """Target X coordinate"""

    y: float
    """Target Y coordinate"""


class ActualPointActionTouchPointWaitAction(BaseModel):
    duration: str
    """Duration to wait (e.g. "500ms")

    Supported time units: ms (milliseconds), s (seconds), m (minutes), h (hours)
    Example formats: "500ms", "30s", "5m", "1h" Default: 500ms
    """

    type: str
    """Type of the action"""


ActualPointAction: TypeAlias = Union[ActualPointActionTouchPointMoveAction, ActualPointActionTouchPointWaitAction]


class ActualPoint(BaseModel):
    start: ActualPointStart
    """Initial touch point position"""

    actions: Optional[List[ActualPointAction]] = None
    """Sequence of actions to perform after initial touch"""


class Actual(BaseModel):
    points: List[ActualPoint]
    """Array of touch points with their normalized coordinates and actions"""


class ScreenshotAfter(BaseModel):
    uri: str
    """URI of the screenshot after the action"""

    presigned_url: Optional[str] = FieldInfo(alias="presignedUrl", default=None)
    """Presigned url of the screenshot before the action"""


class ScreenshotBefore(BaseModel):
    uri: str
    """URI of the screenshot before the action"""

    presigned_url: Optional[str] = FieldInfo(alias="presignedUrl", default=None)
    """Presigned url of the screenshot before the action"""


class ScreenshotTrace(BaseModel):
    uri: str
    """URI of the screenshot with operation trace"""


class Screenshot(BaseModel):
    after: Optional[ScreenshotAfter] = None
    """Screenshot taken after action execution"""

    before: Optional[ScreenshotBefore] = None
    """Screenshot taken before action execution"""

    trace: Optional[ScreenshotTrace] = None
    """Screenshot with action operation trace"""


class ActionTouchResponse(BaseModel):
    action_id: str = FieldInfo(alias="actionId")
    """Unique identifier for each action.

    Use this ID to locate the action and report issues.
    """

    actual: Actual
    """Actual parameters used when executing the touch action"""

    message: str
    """message"""

    screenshot: Optional[Screenshot] = None
    """Complete screenshot result with operation trace, before and after images"""
