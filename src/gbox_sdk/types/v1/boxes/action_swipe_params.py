# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ActionSwipeParams", "SwipeSimple", "Swipe"]


class SwipeSimple(TypedDict, total=False):
    direction: Required[Literal["up", "down", "left", "right", "upLeft", "upRight", "downLeft", "downRight"]]
    """Direction of the swipe"""

    distance: float
    """Distance of the swipe in pixels.

    If not provided, will use a default distance based on screen size
    """

    duration: str
    """Duration of the swipe"""


class Swipe(TypedDict, total=False):
    end: Required[object]
    """End point of the swipe path"""

    start: Required[object]
    """Start point of the swipe path"""

    duration: str
    """Duration of the swipe"""

    output_format: Annotated[Literal["base64", "storageKey"], PropertyInfo(alias="outputFormat")]
    """Type of the URI. default is base64."""

    screenshot_delay: Annotated[str, PropertyInfo(alias="screenshotDelay")]
    """Delay after performing the action, before taking the final screenshot.

    Execution flow:

    1. Take screenshot before action
    2. Perform the action
    3. Wait for screenshotDelay (this parameter)
    4. Take screenshot after action

    Example: '500ms' means wait 500ms after the action before capturing the final
    screenshot.
    """


ActionSwipeParams: TypeAlias = Union[SwipeSimple, Swipe]
