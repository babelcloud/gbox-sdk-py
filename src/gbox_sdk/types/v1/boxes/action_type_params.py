# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ActionTypeParams"]


class ActionTypeParams(TypedDict, total=False):
    text: Required[str]
    """Text to type"""

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
