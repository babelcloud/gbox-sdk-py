# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ActionClickResponse", "Actual", "Screenshot", "ScreenshotAfter", "ScreenshotBefore", "ScreenshotTrace"]


class Actual(BaseModel):
    button: Literal["left", "right", "middle"]
    """Mouse button that was clicked"""

    double: bool
    """Whether a double click was performed"""

    x: float
    """X coordinate where the click was executed"""

    y: float
    """Y coordinate where the click was executed"""

    modifier_keys: Optional[
        List[
            Literal[
                "a",
                "b",
                "c",
                "d",
                "e",
                "f",
                "g",
                "h",
                "i",
                "j",
                "k",
                "l",
                "m",
                "n",
                "o",
                "p",
                "q",
                "r",
                "s",
                "t",
                "u",
                "v",
                "w",
                "x",
                "y",
                "z",
                "0",
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "f1",
                "f2",
                "f3",
                "f4",
                "f5",
                "f6",
                "f7",
                "f8",
                "f9",
                "f10",
                "f11",
                "f12",
                "control",
                "alt",
                "shift",
                "meta",
                "win",
                "cmd",
                "option",
                "arrowUp",
                "arrowDown",
                "arrowLeft",
                "arrowRight",
                "home",
                "end",
                "pageUp",
                "pageDown",
                "enter",
                "space",
                "tab",
                "escape",
                "backspace",
                "delete",
                "insert",
                "capsLock",
                "numLock",
                "scrollLock",
                "pause",
                "printScreen",
                ";",
                "=",
                ",",
                "-",
                ".",
                "/",
                "`",
                "[",
                "\\",
                "]",
                "'",
                "numpad0",
                "numpad1",
                "numpad2",
                "numpad3",
                "numpad4",
                "numpad5",
                "numpad6",
                "numpad7",
                "numpad8",
                "numpad9",
                "numpadAdd",
                "numpadSubtract",
                "numpadMultiply",
                "numpadDivide",
                "numpadDecimal",
                "numpadEnter",
                "numpadEqual",
                "volumeUp",
                "volumeDown",
                "volumeMute",
                "mediaPlayPause",
                "mediaStop",
                "mediaNextTrack",
                "mediaPreviousTrack",
            ]
        ]
    ] = FieldInfo(alias="modifierKeys", default=None)
    """Modifier keys that were pressed during the click (e.g., control, shift, alt).

    Matches the KeyboardKey enum used by pressKey action.
    """


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


class ActionClickResponse(BaseModel):
    action_id: str = FieldInfo(alias="actionId")
    """Unique identifier for each action.

    Use this ID to locate the action and report issues.
    """

    actual: Actual
    """
    Actual parameters used when executing the click action, with the same field
    names as input parameters
    """

    message: str
    """message"""

    screenshot: Optional[Screenshot] = None
    """Complete screenshot result with operation trace, before and after images"""
