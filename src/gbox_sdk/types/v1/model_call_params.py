# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["ModelCallParams", "Action", "ActionClickAction", "ActionDragAction", "ActionScrollAction"]


class ModelCallParams(TypedDict, total=False):
    action: Required[Action]
    """Structured action object (click or drag)"""

    screenshot: Required[str]
    """Screenshot image as HTTP(S) URL or base64-encoded data URI.

    Supports both formats: 1) HTTP(S) URL pointing to an image file; 2)
    Base64-encoded data URI with format 'data:image/png;base64,[data]' or
    'data:image/jpeg;base64,[data]'. Only PNG and JPEG formats are supported for
    base64.
    """

    model: Literal["gbox-handy-1"]
    """Model to use"""


class ActionClickAction(TypedDict, total=False):
    """Click action structure"""

    target: Required[str]
    """Natural language description of what to click"""

    type: Required[Literal["click", "drag", "scroll"]]
    """Action type"""


class ActionDragAction(TypedDict, total=False):
    """Drag action structure"""

    destination: Required[str]
    """Natural language description of ending position"""

    target: Required[str]
    """Natural language description of starting position"""

    type: Required[Literal["click", "drag", "scroll"]]
    """Action type"""


class ActionScrollAction(TypedDict, total=False):
    """Scroll action structure"""

    direction: Required[Literal["up", "down", "left", "right"]]
    """Scroll direction"""

    location: Required[str]
    """Natural language description of the location where the scroll should originate."""

    type: Required[Literal["click", "drag", "scroll"]]
    """Action type"""


Action: TypeAlias = Union[ActionClickAction, ActionDragAction, ActionScrollAction]
