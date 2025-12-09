# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ActionLongPressResponse", "Actual", "Screenshot", "ScreenshotAfter", "ScreenshotBefore", "ScreenshotTrace"]


class Actual(BaseModel):
    """Actual parameters used when executing the long press action"""

    duration: str
    """Duration of the long press

    Supported time units: ms (milliseconds), s (seconds), m (minutes), h (hours)
    Example formats: "500ms", "30s", "5m", "1h" Default: 1s
    """

    x: float
    """X coordinate where the long press was executed"""

    y: float
    """Y coordinate where the long press was executed"""


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


class ActionLongPressResponse(BaseModel):
    """Result of long press action execution with actual parameters used"""

    action_id: str = FieldInfo(alias="actionId")
    """Unique identifier for each action.

    Use this ID to locate the action and report issues.
    """

    actual: Actual
    """Actual parameters used when executing the long press action"""

    message: str
    """message"""

    screenshot: Optional[Screenshot] = None
    """Complete screenshot result with operation trace, before and after images"""
