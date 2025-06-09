# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["ActionResult", "Screenshot", "ScreenshotAfter", "ScreenshotBefore", "ScreenshotTrace"]


class ScreenshotAfter(BaseModel):
    uri: str
    """URI of the screenshot after the action"""


class ScreenshotBefore(BaseModel):
    uri: str
    """URI of the screenshot before the action"""


class ScreenshotTrace(BaseModel):
    uri: str
    """URI of the screenshot with operation trace"""


class Screenshot(BaseModel):
    after: ScreenshotAfter
    """Screenshot taken after action execution"""

    before: ScreenshotBefore
    """Screenshot taken before action execution"""

    trace: ScreenshotTrace
    """Screenshot with action operation trace"""


class ActionResult(BaseModel):
    screenshot: Screenshot
    """Complete screenshot result with operation trace, before and after images"""
