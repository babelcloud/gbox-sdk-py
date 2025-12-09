# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "ActionDragResponse",
    "Actual",
    "ActualEnd",
    "ActualStart",
    "Screenshot",
    "ScreenshotAfter",
    "ScreenshotBefore",
    "ScreenshotTrace",
]


class ActualEnd(BaseModel):
    """Single point in a drag path"""

    x: float
    """X coordinate of a point in the drag path"""

    y: float
    """Y coordinate of a point in the drag path"""


class ActualStart(BaseModel):
    """Single point in a drag path"""

    x: float
    """X coordinate of a point in the drag path"""

    y: float
    """Y coordinate of a point in the drag path"""


class Actual(BaseModel):
    """Actual parameters used when executing the drag action"""

    duration: str
    """Duration of the drag

    Supported time units: ms (milliseconds), s (seconds), m (minutes), h (hours)
    Example formats: "500ms", "30s", "5m", "1h" Default: 500ms
    """

    end: ActualEnd
    """Single point in a drag path"""

    start: ActualStart
    """Single point in a drag path"""


class ScreenshotAfter(BaseModel):
    """Screenshot taken after action execution"""

    uri: str
    """URI of the screenshot after the action"""

    presigned_url: Optional[str] = FieldInfo(alias="presignedUrl", default=None)
    """Presigned url of the screenshot before the action"""


class ScreenshotBefore(BaseModel):
    """Screenshot taken before action execution"""

    uri: str
    """URI of the screenshot before the action"""

    presigned_url: Optional[str] = FieldInfo(alias="presignedUrl", default=None)
    """Presigned url of the screenshot before the action"""


class ScreenshotTrace(BaseModel):
    """Screenshot with action operation trace"""

    uri: str
    """URI of the screenshot with operation trace"""


class Screenshot(BaseModel):
    """Complete screenshot result with operation trace, before and after images"""

    after: Optional[ScreenshotAfter] = None
    """Screenshot taken after action execution"""

    before: Optional[ScreenshotBefore] = None
    """Screenshot taken before action execution"""

    trace: Optional[ScreenshotTrace] = None
    """Screenshot with action operation trace"""


class ActionDragResponse(BaseModel):
    """Result of drag action execution with actual parameters used"""

    action_id: str = FieldInfo(alias="actionId")
    """Unique identifier for each action.

    Use this ID to locate the action and report issues.
    """

    actual: Actual
    """Actual parameters used when executing the drag action"""

    message: str
    """message"""

    screenshot: Optional[Screenshot] = None
    """Complete screenshot result with operation trace, before and after images"""
