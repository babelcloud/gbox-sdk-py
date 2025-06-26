# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "ActionAIResponse",
    "AIActionScreenshotResult",
    "AIActionScreenshotResultAIResponse",
    "AIActionScreenshotResultAIResponseAction",
    "AIActionScreenshotResultAIResponseActionTypedClickAction",
    "AIActionScreenshotResultAIResponseActionTypedTouchAction",
    "AIActionScreenshotResultAIResponseActionTypedTouchActionPoint",
    "AIActionScreenshotResultAIResponseActionTypedTouchActionPointStart",
    "AIActionScreenshotResultAIResponseActionTypedDragAction",
    "AIActionScreenshotResultAIResponseActionTypedDragActionPath",
    "AIActionScreenshotResultAIResponseActionTypedScrollAction",
    "AIActionScreenshotResultAIResponseActionTypedSwipeSimpleAction",
    "AIActionScreenshotResultAIResponseActionTypedSwipeAdvancedAction",
    "AIActionScreenshotResultAIResponseActionTypedSwipeAdvancedActionEnd",
    "AIActionScreenshotResultAIResponseActionTypedSwipeAdvancedActionStart",
    "AIActionScreenshotResultAIResponseActionTypedPressKeyAction",
    "AIActionScreenshotResultAIResponseActionTypedPressButtonAction",
    "AIActionScreenshotResultAIResponseActionTypedTypeAction",
    "AIActionScreenshotResultAIResponseActionTypedMoveAction",
    "AIActionScreenshotResultAIResponseActionTypedScreenRotationAction",
    "AIActionScreenshotResultAIResponseActionTypedScreenshotAction",
    "AIActionScreenshotResultAIResponseActionTypedScreenshotActionClip",
    "AIActionScreenshotResultScreenshot",
    "AIActionScreenshotResultScreenshotAfter",
    "AIActionScreenshotResultScreenshotBefore",
    "AIActionScreenshotResultScreenshotTrace",
    "AIActionResultDto",
    "AIActionResultDtoAIResponse",
    "AIActionResultDtoAIResponseAction",
    "AIActionResultDtoAIResponseActionTypedClickAction",
    "AIActionResultDtoAIResponseActionTypedTouchAction",
    "AIActionResultDtoAIResponseActionTypedTouchActionPoint",
    "AIActionResultDtoAIResponseActionTypedTouchActionPointStart",
    "AIActionResultDtoAIResponseActionTypedDragAction",
    "AIActionResultDtoAIResponseActionTypedDragActionPath",
    "AIActionResultDtoAIResponseActionTypedScrollAction",
    "AIActionResultDtoAIResponseActionTypedSwipeSimpleAction",
    "AIActionResultDtoAIResponseActionTypedSwipeAdvancedAction",
    "AIActionResultDtoAIResponseActionTypedSwipeAdvancedActionEnd",
    "AIActionResultDtoAIResponseActionTypedSwipeAdvancedActionStart",
    "AIActionResultDtoAIResponseActionTypedPressKeyAction",
    "AIActionResultDtoAIResponseActionTypedPressButtonAction",
    "AIActionResultDtoAIResponseActionTypedTypeAction",
    "AIActionResultDtoAIResponseActionTypedMoveAction",
    "AIActionResultDtoAIResponseActionTypedScreenRotationAction",
    "AIActionResultDtoAIResponseActionTypedScreenshotAction",
    "AIActionResultDtoAIResponseActionTypedScreenshotActionClip",
]


class AIActionScreenshotResultAIResponseActionTypedClickAction(BaseModel):
    x: float
    """X coordinate of the click"""

    y: float
    """Y coordinate of the click"""

    button: Optional[Literal["left", "right", "middle"]] = None
    """Mouse button to click"""

    double: Optional[bool] = None
    """Whether to perform a double click"""

    include_screenshot: Optional[bool] = FieldInfo(alias="includeScreenshot", default=None)
    """Whether to include screenshots in the action response.

    If false, the screenshot object will still be returned but with empty URIs.
    Default is false.
    """

    output_format: Optional[Literal["base64", "storageKey"]] = FieldInfo(alias="outputFormat", default=None)
    """Type of the URI. default is base64."""

    screenshot_delay: Optional[str] = FieldInfo(alias="screenshotDelay", default=None)
    """Delay after performing the action, before taking the final screenshot.

    Execution flow:

    1. Take screenshot before action
    2. Perform the action
    3. Wait for screenshotDelay (this parameter)
    4. Take screenshot after action

    Example: '500ms' means wait 500ms after the action before capturing the final
    screenshot.

    Supported time units: ms (milliseconds), s (seconds), m (minutes), h (hours)
    Example formats: "500ms", "30s", "5m", "1h" Default: 500ms Maximum allowed: 30s
    """


class AIActionScreenshotResultAIResponseActionTypedTouchActionPointStart(BaseModel):
    x: float
    """Starting X coordinate"""

    y: float
    """Starting Y coordinate"""


class AIActionScreenshotResultAIResponseActionTypedTouchActionPoint(BaseModel):
    start: AIActionScreenshotResultAIResponseActionTypedTouchActionPointStart
    """Initial touch point position"""

    actions: Optional[List[object]] = None
    """Sequence of actions to perform after initial touch"""


class AIActionScreenshotResultAIResponseActionTypedTouchAction(BaseModel):
    points: List[AIActionScreenshotResultAIResponseActionTypedTouchActionPoint]
    """Array of touch points and their actions"""

    include_screenshot: Optional[bool] = FieldInfo(alias="includeScreenshot", default=None)
    """Whether to include screenshots in the action response.

    If false, the screenshot object will still be returned but with empty URIs.
    Default is false.
    """

    output_format: Optional[Literal["base64", "storageKey"]] = FieldInfo(alias="outputFormat", default=None)
    """Type of the URI. default is base64."""

    screenshot_delay: Optional[str] = FieldInfo(alias="screenshotDelay", default=None)
    """Delay after performing the action, before taking the final screenshot.

    Execution flow:

    1. Take screenshot before action
    2. Perform the action
    3. Wait for screenshotDelay (this parameter)
    4. Take screenshot after action

    Example: '500ms' means wait 500ms after the action before capturing the final
    screenshot.

    Supported time units: ms (milliseconds), s (seconds), m (minutes), h (hours)
    Example formats: "500ms", "30s", "5m", "1h" Default: 500ms Maximum allowed: 30s
    """


class AIActionScreenshotResultAIResponseActionTypedDragActionPath(BaseModel):
    x: float
    """X coordinate of a point in the drag path"""

    y: float
    """Y coordinate of a point in the drag path"""


class AIActionScreenshotResultAIResponseActionTypedDragAction(BaseModel):
    path: List[AIActionScreenshotResultAIResponseActionTypedDragActionPath]
    """Path of the drag action as a series of coordinates"""

    duration: Optional[str] = None
    """Time interval between points (e.g. "50ms")

    Supported time units: ms (milliseconds), s (seconds), m (minutes), h (hours)
    Example formats: "500ms", "30s", "5m", "1h" Default: 50ms
    """

    include_screenshot: Optional[bool] = FieldInfo(alias="includeScreenshot", default=None)
    """Whether to include screenshots in the action response.

    If false, the screenshot object will still be returned but with empty URIs.
    Default is false.
    """

    output_format: Optional[Literal["base64", "storageKey"]] = FieldInfo(alias="outputFormat", default=None)
    """Type of the URI. default is base64."""

    screenshot_delay: Optional[str] = FieldInfo(alias="screenshotDelay", default=None)
    """Delay after performing the action, before taking the final screenshot.

    Execution flow:

    1. Take screenshot before action
    2. Perform the action
    3. Wait for screenshotDelay (this parameter)
    4. Take screenshot after action

    Example: '500ms' means wait 500ms after the action before capturing the final
    screenshot.

    Supported time units: ms (milliseconds), s (seconds), m (minutes), h (hours)
    Example formats: "500ms", "30s", "5m", "1h" Default: 500ms Maximum allowed: 30s
    """


class AIActionScreenshotResultAIResponseActionTypedScrollAction(BaseModel):
    scroll_x: float = FieldInfo(alias="scrollX")
    """Horizontal scroll amount"""

    scroll_y: float = FieldInfo(alias="scrollY")
    """Vertical scroll amount"""

    x: float
    """X coordinate of the scroll position"""

    y: float
    """Y coordinate of the scroll position"""

    include_screenshot: Optional[bool] = FieldInfo(alias="includeScreenshot", default=None)
    """Whether to include screenshots in the action response.

    If false, the screenshot object will still be returned but with empty URIs.
    Default is false.
    """

    output_format: Optional[Literal["base64", "storageKey"]] = FieldInfo(alias="outputFormat", default=None)
    """Type of the URI. default is base64."""

    screenshot_delay: Optional[str] = FieldInfo(alias="screenshotDelay", default=None)
    """Delay after performing the action, before taking the final screenshot.

    Execution flow:

    1. Take screenshot before action
    2. Perform the action
    3. Wait for screenshotDelay (this parameter)
    4. Take screenshot after action

    Example: '500ms' means wait 500ms after the action before capturing the final
    screenshot.

    Supported time units: ms (milliseconds), s (seconds), m (minutes), h (hours)
    Example formats: "500ms", "30s", "5m", "1h" Default: 500ms Maximum allowed: 30s
    """


class AIActionScreenshotResultAIResponseActionTypedSwipeSimpleAction(BaseModel):
    direction: Literal["up", "down", "left", "right", "upLeft", "upRight", "downLeft", "downRight"]
    """Direction to swipe.

    The gesture will be performed from the center of the screen towards this
    direction.
    """

    distance: Optional[float] = None
    """Distance of the swipe in pixels.

    If not provided, the swipe will be performed from the center of the screen to
    the screen edge
    """

    duration: Optional[str] = None
    """Duration of the swipe

    Supported time units: ms (milliseconds), s (seconds), m (minutes), h (hours)
    Example formats: "500ms", "30s", "5m", "1h" Default: 500ms
    """

    include_screenshot: Optional[bool] = FieldInfo(alias="includeScreenshot", default=None)
    """Whether to include screenshots in the action response.

    If false, the screenshot object will still be returned but with empty URIs.
    Default is false.
    """

    output_format: Optional[Literal["base64", "storageKey"]] = FieldInfo(alias="outputFormat", default=None)
    """Type of the URI. default is base64."""

    screenshot_delay: Optional[str] = FieldInfo(alias="screenshotDelay", default=None)
    """Delay after performing the action, before taking the final screenshot.

    Execution flow:

    1. Take screenshot before action
    2. Perform the action
    3. Wait for screenshotDelay (this parameter)
    4. Take screenshot after action

    Example: '500ms' means wait 500ms after the action before capturing the final
    screenshot.

    Supported time units: ms (milliseconds), s (seconds), m (minutes), h (hours)
    Example formats: "500ms", "30s", "5m", "1h" Default: 500ms Maximum allowed: 30s
    """


class AIActionScreenshotResultAIResponseActionTypedSwipeAdvancedActionEnd(BaseModel):
    x: float
    """Start/end x coordinate of the swipe path"""

    y: float
    """Start/end y coordinate of the swipe path"""


class AIActionScreenshotResultAIResponseActionTypedSwipeAdvancedActionStart(BaseModel):
    x: float
    """Start/end x coordinate of the swipe path"""

    y: float
    """Start/end y coordinate of the swipe path"""


class AIActionScreenshotResultAIResponseActionTypedSwipeAdvancedAction(BaseModel):
    end: AIActionScreenshotResultAIResponseActionTypedSwipeAdvancedActionEnd
    """Swipe path"""

    start: AIActionScreenshotResultAIResponseActionTypedSwipeAdvancedActionStart
    """Swipe path"""

    duration: Optional[str] = None
    """Duration of the swipe

    Supported time units: ms (milliseconds), s (seconds), m (minutes), h (hours)
    Example formats: "500ms", "30s", "5m", "1h" Default: 500ms
    """

    include_screenshot: Optional[bool] = FieldInfo(alias="includeScreenshot", default=None)
    """Whether to include screenshots in the action response.

    If false, the screenshot object will still be returned but with empty URIs.
    Default is false.
    """

    output_format: Optional[Literal["base64", "storageKey"]] = FieldInfo(alias="outputFormat", default=None)
    """Type of the URI. default is base64."""

    screenshot_delay: Optional[str] = FieldInfo(alias="screenshotDelay", default=None)
    """Delay after performing the action, before taking the final screenshot.

    Execution flow:

    1. Take screenshot before action
    2. Perform the action
    3. Wait for screenshotDelay (this parameter)
    4. Take screenshot after action

    Example: '500ms' means wait 500ms after the action before capturing the final
    screenshot.

    Supported time units: ms (milliseconds), s (seconds), m (minutes), h (hours)
    Example formats: "500ms", "30s", "5m", "1h" Default: 500ms Maximum allowed: 30s
    """


class AIActionScreenshotResultAIResponseActionTypedPressKeyAction(BaseModel):
    keys: List[
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
    """This is an array of keyboard keys to press.

    Supports cross-platform compatibility.
    """

    include_screenshot: Optional[bool] = FieldInfo(alias="includeScreenshot", default=None)
    """Whether to include screenshots in the action response.

    If false, the screenshot object will still be returned but with empty URIs.
    Default is false.
    """

    output_format: Optional[Literal["base64", "storageKey"]] = FieldInfo(alias="outputFormat", default=None)
    """Type of the URI. default is base64."""

    screenshot_delay: Optional[str] = FieldInfo(alias="screenshotDelay", default=None)
    """Delay after performing the action, before taking the final screenshot.

    Execution flow:

    1. Take screenshot before action
    2. Perform the action
    3. Wait for screenshotDelay (this parameter)
    4. Take screenshot after action

    Example: '500ms' means wait 500ms after the action before capturing the final
    screenshot.

    Supported time units: ms (milliseconds), s (seconds), m (minutes), h (hours)
    Example formats: "500ms", "30s", "5m", "1h" Default: 500ms Maximum allowed: 30s
    """


class AIActionScreenshotResultAIResponseActionTypedPressButtonAction(BaseModel):
    buttons: List[Literal["power", "volumeUp", "volumeDown", "volumeMute", "home", "back", "menu", "appSwitch"]]
    """Button to press"""

    include_screenshot: Optional[bool] = FieldInfo(alias="includeScreenshot", default=None)
    """Whether to include screenshots in the action response.

    If false, the screenshot object will still be returned but with empty URIs.
    Default is false.
    """

    output_format: Optional[Literal["base64", "storageKey"]] = FieldInfo(alias="outputFormat", default=None)
    """Type of the URI. default is base64."""

    screenshot_delay: Optional[str] = FieldInfo(alias="screenshotDelay", default=None)
    """Delay after performing the action, before taking the final screenshot.

    Execution flow:

    1. Take screenshot before action
    2. Perform the action
    3. Wait for screenshotDelay (this parameter)
    4. Take screenshot after action

    Example: '500ms' means wait 500ms after the action before capturing the final
    screenshot.

    Supported time units: ms (milliseconds), s (seconds), m (minutes), h (hours)
    Example formats: "500ms", "30s", "5m", "1h" Default: 500ms Maximum allowed: 30s
    """


class AIActionScreenshotResultAIResponseActionTypedTypeAction(BaseModel):
    text: str
    """Text to type"""

    include_screenshot: Optional[bool] = FieldInfo(alias="includeScreenshot", default=None)
    """Whether to include screenshots in the action response.

    If false, the screenshot object will still be returned but with empty URIs.
    Default is false.
    """

    output_format: Optional[Literal["base64", "storageKey"]] = FieldInfo(alias="outputFormat", default=None)
    """Type of the URI. default is base64."""

    screenshot_delay: Optional[str] = FieldInfo(alias="screenshotDelay", default=None)
    """Delay after performing the action, before taking the final screenshot.

    Execution flow:

    1. Take screenshot before action
    2. Perform the action
    3. Wait for screenshotDelay (this parameter)
    4. Take screenshot after action

    Example: '500ms' means wait 500ms after the action before capturing the final
    screenshot.

    Supported time units: ms (milliseconds), s (seconds), m (minutes), h (hours)
    Example formats: "500ms", "30s", "5m", "1h" Default: 500ms Maximum allowed: 30s
    """


class AIActionScreenshotResultAIResponseActionTypedMoveAction(BaseModel):
    x: float
    """X coordinate to move to"""

    y: float
    """Y coordinate to move to"""

    include_screenshot: Optional[bool] = FieldInfo(alias="includeScreenshot", default=None)
    """Whether to include screenshots in the action response.

    If false, the screenshot object will still be returned but with empty URIs.
    Default is false.
    """

    output_format: Optional[Literal["base64", "storageKey"]] = FieldInfo(alias="outputFormat", default=None)
    """Type of the URI. default is base64."""

    screenshot_delay: Optional[str] = FieldInfo(alias="screenshotDelay", default=None)
    """Delay after performing the action, before taking the final screenshot.

    Execution flow:

    1. Take screenshot before action
    2. Perform the action
    3. Wait for screenshotDelay (this parameter)
    4. Take screenshot after action

    Example: '500ms' means wait 500ms after the action before capturing the final
    screenshot.

    Supported time units: ms (milliseconds), s (seconds), m (minutes), h (hours)
    Example formats: "500ms", "30s", "5m", "1h" Default: 500ms Maximum allowed: 30s
    """


class AIActionScreenshotResultAIResponseActionTypedScreenRotationAction(BaseModel):
    angle: Literal[90, 180, 270]
    """Rotation angle in degrees"""

    direction: Literal["clockwise", "counter-clockwise"]
    """Rotation direction"""


class AIActionScreenshotResultAIResponseActionTypedScreenshotActionClip(BaseModel):
    height: float
    """Height of the clip"""

    width: float
    """Width of the clip"""

    x: float
    """X coordinate of the clip"""

    y: float
    """Y coordinate of the clip"""


class AIActionScreenshotResultAIResponseActionTypedScreenshotAction(BaseModel):
    clip: Optional[AIActionScreenshotResultAIResponseActionTypedScreenshotActionClip] = None
    """Clipping region for screenshot capture"""

    output_format: Optional[Literal["base64", "storageKey"]] = FieldInfo(alias="outputFormat", default=None)
    """Type of the URI. default is base64."""


AIActionScreenshotResultAIResponseAction: TypeAlias = Union[
    AIActionScreenshotResultAIResponseActionTypedClickAction,
    AIActionScreenshotResultAIResponseActionTypedTouchAction,
    AIActionScreenshotResultAIResponseActionTypedDragAction,
    AIActionScreenshotResultAIResponseActionTypedScrollAction,
    AIActionScreenshotResultAIResponseActionTypedSwipeSimpleAction,
    AIActionScreenshotResultAIResponseActionTypedSwipeAdvancedAction,
    AIActionScreenshotResultAIResponseActionTypedPressKeyAction,
    AIActionScreenshotResultAIResponseActionTypedPressButtonAction,
    AIActionScreenshotResultAIResponseActionTypedTypeAction,
    AIActionScreenshotResultAIResponseActionTypedMoveAction,
    AIActionScreenshotResultAIResponseActionTypedScreenRotationAction,
    AIActionScreenshotResultAIResponseActionTypedScreenshotAction,
]


class AIActionScreenshotResultAIResponse(BaseModel):
    action: AIActionScreenshotResultAIResponseAction
    """Action to be executed by the AI with type identifier"""

    messages: List[List[object]]
    """message"""

    model: str
    """model"""

    reasoning: Optional[str] = None
    """reasoning"""


class AIActionScreenshotResultScreenshotAfter(BaseModel):
    uri: str
    """URI of the screenshot after the action"""


class AIActionScreenshotResultScreenshotBefore(BaseModel):
    uri: str
    """URI of the screenshot before the action"""


class AIActionScreenshotResultScreenshotTrace(BaseModel):
    uri: str
    """URI of the screenshot with operation trace"""


class AIActionScreenshotResultScreenshot(BaseModel):
    after: AIActionScreenshotResultScreenshotAfter
    """Screenshot taken after action execution"""

    before: AIActionScreenshotResultScreenshotBefore
    """Screenshot taken before action execution"""

    trace: AIActionScreenshotResultScreenshotTrace
    """Screenshot with action operation trace"""


class AIActionScreenshotResult(BaseModel):
    ai_response: AIActionScreenshotResultAIResponse = FieldInfo(alias="aiResponse")
    """Response of AI action execution"""

    message: str
    """message"""

    screenshot: AIActionScreenshotResultScreenshot
    """Complete screenshot result with operation trace, before and after images"""


class AIActionResultDtoAIResponseActionTypedClickAction(BaseModel):
    x: float
    """X coordinate of the click"""

    y: float
    """Y coordinate of the click"""

    button: Optional[Literal["left", "right", "middle"]] = None
    """Mouse button to click"""

    double: Optional[bool] = None
    """Whether to perform a double click"""

    include_screenshot: Optional[bool] = FieldInfo(alias="includeScreenshot", default=None)
    """Whether to include screenshots in the action response.

    If false, the screenshot object will still be returned but with empty URIs.
    Default is false.
    """

    output_format: Optional[Literal["base64", "storageKey"]] = FieldInfo(alias="outputFormat", default=None)
    """Type of the URI. default is base64."""

    screenshot_delay: Optional[str] = FieldInfo(alias="screenshotDelay", default=None)
    """Delay after performing the action, before taking the final screenshot.

    Execution flow:

    1. Take screenshot before action
    2. Perform the action
    3. Wait for screenshotDelay (this parameter)
    4. Take screenshot after action

    Example: '500ms' means wait 500ms after the action before capturing the final
    screenshot.

    Supported time units: ms (milliseconds), s (seconds), m (minutes), h (hours)
    Example formats: "500ms", "30s", "5m", "1h" Default: 500ms Maximum allowed: 30s
    """


class AIActionResultDtoAIResponseActionTypedTouchActionPointStart(BaseModel):
    x: float
    """Starting X coordinate"""

    y: float
    """Starting Y coordinate"""


class AIActionResultDtoAIResponseActionTypedTouchActionPoint(BaseModel):
    start: AIActionResultDtoAIResponseActionTypedTouchActionPointStart
    """Initial touch point position"""

    actions: Optional[List[object]] = None
    """Sequence of actions to perform after initial touch"""


class AIActionResultDtoAIResponseActionTypedTouchAction(BaseModel):
    points: List[AIActionResultDtoAIResponseActionTypedTouchActionPoint]
    """Array of touch points and their actions"""

    include_screenshot: Optional[bool] = FieldInfo(alias="includeScreenshot", default=None)
    """Whether to include screenshots in the action response.

    If false, the screenshot object will still be returned but with empty URIs.
    Default is false.
    """

    output_format: Optional[Literal["base64", "storageKey"]] = FieldInfo(alias="outputFormat", default=None)
    """Type of the URI. default is base64."""

    screenshot_delay: Optional[str] = FieldInfo(alias="screenshotDelay", default=None)
    """Delay after performing the action, before taking the final screenshot.

    Execution flow:

    1. Take screenshot before action
    2. Perform the action
    3. Wait for screenshotDelay (this parameter)
    4. Take screenshot after action

    Example: '500ms' means wait 500ms after the action before capturing the final
    screenshot.

    Supported time units: ms (milliseconds), s (seconds), m (minutes), h (hours)
    Example formats: "500ms", "30s", "5m", "1h" Default: 500ms Maximum allowed: 30s
    """


class AIActionResultDtoAIResponseActionTypedDragActionPath(BaseModel):
    x: float
    """X coordinate of a point in the drag path"""

    y: float
    """Y coordinate of a point in the drag path"""


class AIActionResultDtoAIResponseActionTypedDragAction(BaseModel):
    path: List[AIActionResultDtoAIResponseActionTypedDragActionPath]
    """Path of the drag action as a series of coordinates"""

    duration: Optional[str] = None
    """Time interval between points (e.g. "50ms")

    Supported time units: ms (milliseconds), s (seconds), m (minutes), h (hours)
    Example formats: "500ms", "30s", "5m", "1h" Default: 50ms
    """

    include_screenshot: Optional[bool] = FieldInfo(alias="includeScreenshot", default=None)
    """Whether to include screenshots in the action response.

    If false, the screenshot object will still be returned but with empty URIs.
    Default is false.
    """

    output_format: Optional[Literal["base64", "storageKey"]] = FieldInfo(alias="outputFormat", default=None)
    """Type of the URI. default is base64."""

    screenshot_delay: Optional[str] = FieldInfo(alias="screenshotDelay", default=None)
    """Delay after performing the action, before taking the final screenshot.

    Execution flow:

    1. Take screenshot before action
    2. Perform the action
    3. Wait for screenshotDelay (this parameter)
    4. Take screenshot after action

    Example: '500ms' means wait 500ms after the action before capturing the final
    screenshot.

    Supported time units: ms (milliseconds), s (seconds), m (minutes), h (hours)
    Example formats: "500ms", "30s", "5m", "1h" Default: 500ms Maximum allowed: 30s
    """


class AIActionResultDtoAIResponseActionTypedScrollAction(BaseModel):
    scroll_x: float = FieldInfo(alias="scrollX")
    """Horizontal scroll amount"""

    scroll_y: float = FieldInfo(alias="scrollY")
    """Vertical scroll amount"""

    x: float
    """X coordinate of the scroll position"""

    y: float
    """Y coordinate of the scroll position"""

    include_screenshot: Optional[bool] = FieldInfo(alias="includeScreenshot", default=None)
    """Whether to include screenshots in the action response.

    If false, the screenshot object will still be returned but with empty URIs.
    Default is false.
    """

    output_format: Optional[Literal["base64", "storageKey"]] = FieldInfo(alias="outputFormat", default=None)
    """Type of the URI. default is base64."""

    screenshot_delay: Optional[str] = FieldInfo(alias="screenshotDelay", default=None)
    """Delay after performing the action, before taking the final screenshot.

    Execution flow:

    1. Take screenshot before action
    2. Perform the action
    3. Wait for screenshotDelay (this parameter)
    4. Take screenshot after action

    Example: '500ms' means wait 500ms after the action before capturing the final
    screenshot.

    Supported time units: ms (milliseconds), s (seconds), m (minutes), h (hours)
    Example formats: "500ms", "30s", "5m", "1h" Default: 500ms Maximum allowed: 30s
    """


class AIActionResultDtoAIResponseActionTypedSwipeSimpleAction(BaseModel):
    direction: Literal["up", "down", "left", "right", "upLeft", "upRight", "downLeft", "downRight"]
    """Direction to swipe.

    The gesture will be performed from the center of the screen towards this
    direction.
    """

    distance: Optional[float] = None
    """Distance of the swipe in pixels.

    If not provided, the swipe will be performed from the center of the screen to
    the screen edge
    """

    duration: Optional[str] = None
    """Duration of the swipe

    Supported time units: ms (milliseconds), s (seconds), m (minutes), h (hours)
    Example formats: "500ms", "30s", "5m", "1h" Default: 500ms
    """

    include_screenshot: Optional[bool] = FieldInfo(alias="includeScreenshot", default=None)
    """Whether to include screenshots in the action response.

    If false, the screenshot object will still be returned but with empty URIs.
    Default is false.
    """

    output_format: Optional[Literal["base64", "storageKey"]] = FieldInfo(alias="outputFormat", default=None)
    """Type of the URI. default is base64."""

    screenshot_delay: Optional[str] = FieldInfo(alias="screenshotDelay", default=None)
    """Delay after performing the action, before taking the final screenshot.

    Execution flow:

    1. Take screenshot before action
    2. Perform the action
    3. Wait for screenshotDelay (this parameter)
    4. Take screenshot after action

    Example: '500ms' means wait 500ms after the action before capturing the final
    screenshot.

    Supported time units: ms (milliseconds), s (seconds), m (minutes), h (hours)
    Example formats: "500ms", "30s", "5m", "1h" Default: 500ms Maximum allowed: 30s
    """


class AIActionResultDtoAIResponseActionTypedSwipeAdvancedActionEnd(BaseModel):
    x: float
    """Start/end x coordinate of the swipe path"""

    y: float
    """Start/end y coordinate of the swipe path"""


class AIActionResultDtoAIResponseActionTypedSwipeAdvancedActionStart(BaseModel):
    x: float
    """Start/end x coordinate of the swipe path"""

    y: float
    """Start/end y coordinate of the swipe path"""


class AIActionResultDtoAIResponseActionTypedSwipeAdvancedAction(BaseModel):
    end: AIActionResultDtoAIResponseActionTypedSwipeAdvancedActionEnd
    """Swipe path"""

    start: AIActionResultDtoAIResponseActionTypedSwipeAdvancedActionStart
    """Swipe path"""

    duration: Optional[str] = None
    """Duration of the swipe

    Supported time units: ms (milliseconds), s (seconds), m (minutes), h (hours)
    Example formats: "500ms", "30s", "5m", "1h" Default: 500ms
    """

    include_screenshot: Optional[bool] = FieldInfo(alias="includeScreenshot", default=None)
    """Whether to include screenshots in the action response.

    If false, the screenshot object will still be returned but with empty URIs.
    Default is false.
    """

    output_format: Optional[Literal["base64", "storageKey"]] = FieldInfo(alias="outputFormat", default=None)
    """Type of the URI. default is base64."""

    screenshot_delay: Optional[str] = FieldInfo(alias="screenshotDelay", default=None)
    """Delay after performing the action, before taking the final screenshot.

    Execution flow:

    1. Take screenshot before action
    2. Perform the action
    3. Wait for screenshotDelay (this parameter)
    4. Take screenshot after action

    Example: '500ms' means wait 500ms after the action before capturing the final
    screenshot.

    Supported time units: ms (milliseconds), s (seconds), m (minutes), h (hours)
    Example formats: "500ms", "30s", "5m", "1h" Default: 500ms Maximum allowed: 30s
    """


class AIActionResultDtoAIResponseActionTypedPressKeyAction(BaseModel):
    keys: List[
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
    """This is an array of keyboard keys to press.

    Supports cross-platform compatibility.
    """

    include_screenshot: Optional[bool] = FieldInfo(alias="includeScreenshot", default=None)
    """Whether to include screenshots in the action response.

    If false, the screenshot object will still be returned but with empty URIs.
    Default is false.
    """

    output_format: Optional[Literal["base64", "storageKey"]] = FieldInfo(alias="outputFormat", default=None)
    """Type of the URI. default is base64."""

    screenshot_delay: Optional[str] = FieldInfo(alias="screenshotDelay", default=None)
    """Delay after performing the action, before taking the final screenshot.

    Execution flow:

    1. Take screenshot before action
    2. Perform the action
    3. Wait for screenshotDelay (this parameter)
    4. Take screenshot after action

    Example: '500ms' means wait 500ms after the action before capturing the final
    screenshot.

    Supported time units: ms (milliseconds), s (seconds), m (minutes), h (hours)
    Example formats: "500ms", "30s", "5m", "1h" Default: 500ms Maximum allowed: 30s
    """


class AIActionResultDtoAIResponseActionTypedPressButtonAction(BaseModel):
    buttons: List[Literal["power", "volumeUp", "volumeDown", "volumeMute", "home", "back", "menu", "appSwitch"]]
    """Button to press"""

    include_screenshot: Optional[bool] = FieldInfo(alias="includeScreenshot", default=None)
    """Whether to include screenshots in the action response.

    If false, the screenshot object will still be returned but with empty URIs.
    Default is false.
    """

    output_format: Optional[Literal["base64", "storageKey"]] = FieldInfo(alias="outputFormat", default=None)
    """Type of the URI. default is base64."""

    screenshot_delay: Optional[str] = FieldInfo(alias="screenshotDelay", default=None)
    """Delay after performing the action, before taking the final screenshot.

    Execution flow:

    1. Take screenshot before action
    2. Perform the action
    3. Wait for screenshotDelay (this parameter)
    4. Take screenshot after action

    Example: '500ms' means wait 500ms after the action before capturing the final
    screenshot.

    Supported time units: ms (milliseconds), s (seconds), m (minutes), h (hours)
    Example formats: "500ms", "30s", "5m", "1h" Default: 500ms Maximum allowed: 30s
    """


class AIActionResultDtoAIResponseActionTypedTypeAction(BaseModel):
    text: str
    """Text to type"""

    include_screenshot: Optional[bool] = FieldInfo(alias="includeScreenshot", default=None)
    """Whether to include screenshots in the action response.

    If false, the screenshot object will still be returned but with empty URIs.
    Default is false.
    """

    output_format: Optional[Literal["base64", "storageKey"]] = FieldInfo(alias="outputFormat", default=None)
    """Type of the URI. default is base64."""

    screenshot_delay: Optional[str] = FieldInfo(alias="screenshotDelay", default=None)
    """Delay after performing the action, before taking the final screenshot.

    Execution flow:

    1. Take screenshot before action
    2. Perform the action
    3. Wait for screenshotDelay (this parameter)
    4. Take screenshot after action

    Example: '500ms' means wait 500ms after the action before capturing the final
    screenshot.

    Supported time units: ms (milliseconds), s (seconds), m (minutes), h (hours)
    Example formats: "500ms", "30s", "5m", "1h" Default: 500ms Maximum allowed: 30s
    """


class AIActionResultDtoAIResponseActionTypedMoveAction(BaseModel):
    x: float
    """X coordinate to move to"""

    y: float
    """Y coordinate to move to"""

    include_screenshot: Optional[bool] = FieldInfo(alias="includeScreenshot", default=None)
    """Whether to include screenshots in the action response.

    If false, the screenshot object will still be returned but with empty URIs.
    Default is false.
    """

    output_format: Optional[Literal["base64", "storageKey"]] = FieldInfo(alias="outputFormat", default=None)
    """Type of the URI. default is base64."""

    screenshot_delay: Optional[str] = FieldInfo(alias="screenshotDelay", default=None)
    """Delay after performing the action, before taking the final screenshot.

    Execution flow:

    1. Take screenshot before action
    2. Perform the action
    3. Wait for screenshotDelay (this parameter)
    4. Take screenshot after action

    Example: '500ms' means wait 500ms after the action before capturing the final
    screenshot.

    Supported time units: ms (milliseconds), s (seconds), m (minutes), h (hours)
    Example formats: "500ms", "30s", "5m", "1h" Default: 500ms Maximum allowed: 30s
    """


class AIActionResultDtoAIResponseActionTypedScreenRotationAction(BaseModel):
    angle: Literal[90, 180, 270]
    """Rotation angle in degrees"""

    direction: Literal["clockwise", "counter-clockwise"]
    """Rotation direction"""


class AIActionResultDtoAIResponseActionTypedScreenshotActionClip(BaseModel):
    height: float
    """Height of the clip"""

    width: float
    """Width of the clip"""

    x: float
    """X coordinate of the clip"""

    y: float
    """Y coordinate of the clip"""


class AIActionResultDtoAIResponseActionTypedScreenshotAction(BaseModel):
    clip: Optional[AIActionResultDtoAIResponseActionTypedScreenshotActionClip] = None
    """Clipping region for screenshot capture"""

    output_format: Optional[Literal["base64", "storageKey"]] = FieldInfo(alias="outputFormat", default=None)
    """Type of the URI. default is base64."""


AIActionResultDtoAIResponseAction: TypeAlias = Union[
    AIActionResultDtoAIResponseActionTypedClickAction,
    AIActionResultDtoAIResponseActionTypedTouchAction,
    AIActionResultDtoAIResponseActionTypedDragAction,
    AIActionResultDtoAIResponseActionTypedScrollAction,
    AIActionResultDtoAIResponseActionTypedSwipeSimpleAction,
    AIActionResultDtoAIResponseActionTypedSwipeAdvancedAction,
    AIActionResultDtoAIResponseActionTypedPressKeyAction,
    AIActionResultDtoAIResponseActionTypedPressButtonAction,
    AIActionResultDtoAIResponseActionTypedTypeAction,
    AIActionResultDtoAIResponseActionTypedMoveAction,
    AIActionResultDtoAIResponseActionTypedScreenRotationAction,
    AIActionResultDtoAIResponseActionTypedScreenshotAction,
]


class AIActionResultDtoAIResponse(BaseModel):
    action: AIActionResultDtoAIResponseAction
    """Action to be executed by the AI with type identifier"""

    messages: List[List[object]]
    """message"""

    model: str
    """model"""

    reasoning: Optional[str] = None
    """reasoning"""


class AIActionResultDto(BaseModel):
    ai_response: AIActionResultDtoAIResponse = FieldInfo(alias="aiResponse")
    """Response of AI action execution"""

    message: str
    """message"""


ActionAIResponse: TypeAlias = Union[AIActionScreenshotResult, AIActionResultDto]
