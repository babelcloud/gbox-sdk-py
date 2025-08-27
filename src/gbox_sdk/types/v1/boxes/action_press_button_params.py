# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ...._utils import PropertyInfo

__all__ = [
    "ActionPressButtonParams",
    "Options",
    "OptionsScreenshot",
    "OptionsScreenshotUnionMember0",
    "OptionsScreenshotActionScreenshotOptionDto",
]


class ActionPressButtonParams(TypedDict, total=False):
    buttons: Required[
        List[Literal["power", "volumeUp", "volumeDown", "volumeMute", "home", "back", "menu", "appSwitch"]]
    ]
    """Button to press"""

    include_screenshot: Annotated[bool, PropertyInfo(alias="includeScreenshot")]
    """⚠️ DEPRECATED: Use `options.screenshot.range` instead.

    This field will be ignored when `options.screenshot` is provided. Whether to
    include screenshots in the action response. If false, the screenshot object will
    still be returned but with empty URIs. Default is false.
    """

    options: Options
    """Action options.

    When `options.screenshot` is provided, ALL deprecated screenshot fields
    (outputFormat, presignedExpiresIn, screenshotDelay, screenshotRange,
    includeScreenshot) will be completely ignored.
    """

    output_format: Annotated[Literal["base64", "storageKey"], PropertyInfo(alias="outputFormat")]
    """⚠️ DEPRECATED: Use `options.screenshot.outputFormat` instead.

    Type of the URI. default is base64. This field will be ignored when
    `options.screenshot` is provided.
    """

    presigned_expires_in: Annotated[str, PropertyInfo(alias="presignedExpiresIn")]
    """⚠️ DEPRECATED: Use `options.screenshot.presignedExpiresIn` instead.

    Presigned url expires in. Only takes effect when outputFormat is storageKey.
    This field will be ignored when `options.screenshot` is provided.

    Supported time units: ms (milliseconds), s (seconds), m (minutes), h (hours)
    Example formats: "500ms", "30s", "5m", "1h" Default: 30m
    """

    screenshot_delay: Annotated[str, PropertyInfo(alias="screenshotDelay")]
    """⚠️ DEPRECATED: Use `options.screenshot.delay` instead.

    This field will be ignored when `options.screenshot` is provided.

    Delay after performing the action, before taking the final screenshot.

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


class OptionsScreenshotUnionMember0(TypedDict, total=False):
    delay: str
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

    output_format: Annotated[Literal["base64", "storageKey"], PropertyInfo(alias="outputFormat")]
    """Type of the URI. default is base64."""

    presigned_expires_in: Annotated[str, PropertyInfo(alias="presignedExpiresIn")]
    """Presigned url expires in. Only takes effect when outputFormat is storageKey.

    Supported time units: ms (milliseconds), s (seconds), m (minutes), h (hours)
    Example formats: "500ms", "30s", "5m", "1h" Default: 30m
    """

    range: List[Literal["before", "after", "trace"]]
    """Specify which screenshots to capture.

    Available options:

    - before: Screenshot before the action
    - after: Screenshot after the action
    - trace: Screenshot with operation trace

    Default captures all three types. Can specify one or multiple in an array.
    """


class OptionsScreenshotActionScreenshotOptionDto(TypedDict, total=False):
    delay: str
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

    output_format: Annotated[Literal["base64", "storageKey"], PropertyInfo(alias="outputFormat")]
    """Type of the URI. default is base64."""

    presigned_expires_in: Annotated[str, PropertyInfo(alias="presignedExpiresIn")]
    """Presigned url expires in. Only takes effect when outputFormat is storageKey.

    Supported time units: ms (milliseconds), s (seconds), m (minutes), h (hours)
    Example formats: "500ms", "30s", "5m", "1h" Default: 30m
    """

    range: List[Literal["before", "after", "trace"]]
    """Specify which screenshots to capture.

    Available options:

    - before: Screenshot before the action
    - after: Screenshot after the action
    - trace: Screenshot with operation trace

    Default captures all three types. Can specify one or multiple in an array.
    """


OptionsScreenshot: TypeAlias = Union[OptionsScreenshotUnionMember0, OptionsScreenshotActionScreenshotOptionDto]


class Options(TypedDict, total=False):
    screenshot: OptionsScreenshot
    """Screenshot options.

    Can be a boolean to enable/disable screenshots, or an object to configure
    screenshot options.
    """
