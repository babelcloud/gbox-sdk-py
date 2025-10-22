# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["ModelCallParams", "Action", "ActionClickAction", "ActionDragAction", "ActionScrollAction"]


class ModelCallParams(TypedDict, total=False):
    action: Required[Action]
    """Structured action object (click or drag)"""

    screenshot: Required[str]
    """HTTP(S) URL to screenshot image"""

    model: Literal["gbox-handy-1"]
    """Model to use"""


class ActionClickAction(TypedDict, total=False):
    target: Required[str]
    """Natural language description of what to click"""

    type: Required[Literal["click", "drag", "scroll"]]
    """Action type"""


class ActionDragAction(TypedDict, total=False):
    destination: Required[str]
    """Natural language description of ending position"""

    target: Required[str]
    """Natural language description of starting position"""

    type: Required[Literal["click", "drag", "scroll"]]
    """Action type"""


class ActionScrollAction(TypedDict, total=False):
    direction: Required[Literal["up", "down", "left", "right"]]
    """Scroll direction"""

    location: Required[str]
    """Natural language description of the location where the scroll should originate."""

    type: Required[Literal["click", "drag", "scroll"]]
    """Action type"""


Action: TypeAlias = Union[ActionClickAction, ActionDragAction, ActionScrollAction]
