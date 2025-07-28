# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "ActionSwipeResponse",
    "ActionIncludeScreenshotResult",
    "ActionIncludeScreenshotResultScreenshot",
    "ActionIncludeScreenshotResultScreenshotAfter",
    "ActionIncludeScreenshotResultScreenshotBefore",
    "ActionIncludeScreenshotResultScreenshotTrace",
    "ActionCommonResult",
]


class ActionIncludeScreenshotResultScreenshotAfter(BaseModel):
    presigned_url: str = FieldInfo(alias="presignedUrl")
    """Presigned url of the screenshot before the action"""

    uri: str
    """URI of the screenshot after the action"""


class ActionIncludeScreenshotResultScreenshotBefore(BaseModel):
    presigned_url: str = FieldInfo(alias="presignedUrl")
    """Presigned url of the screenshot before the action"""

    uri: str
    """URI of the screenshot before the action"""


class ActionIncludeScreenshotResultScreenshotTrace(BaseModel):
    uri: str
    """URI of the screenshot with operation trace"""


class ActionIncludeScreenshotResultScreenshot(BaseModel):
    after: ActionIncludeScreenshotResultScreenshotAfter
    """Screenshot taken after action execution"""

    before: ActionIncludeScreenshotResultScreenshotBefore
    """Screenshot taken before action execution"""

    trace: ActionIncludeScreenshotResultScreenshotTrace
    """Screenshot with action operation trace"""


class ActionIncludeScreenshotResult(BaseModel):
    screenshot: ActionIncludeScreenshotResultScreenshot
    """Complete screenshot result with operation trace, before and after images"""


class ActionCommonResult(BaseModel):
    message: str
    """message"""


ActionSwipeResponse: TypeAlias = Union[ActionIncludeScreenshotResult, ActionCommonResult]
