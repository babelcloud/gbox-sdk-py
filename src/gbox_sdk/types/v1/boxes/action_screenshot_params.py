# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ActionScreenshotParams", "Clip"]


class ActionScreenshotParams(TypedDict, total=False):
    clip: Clip
    """Clipping region for screenshot capture"""

    output_format: Annotated[Literal["base64", "storageKey"], PropertyInfo(alias="outputFormat")]
    """Type of the URI. default is base64."""

    scale: float
    """The scale of the action to be performed.

    Must be greater than 0.1 and less than or equal to 1.

    Notes:

    - Scale does not change the box's actual screen resolution.
    - It affects the size of the output screenshot and the coordinates/distances of
      actions. Coordinates and distances are scaled by this factor. Example: when
      scale = 1, Click({x:100, y:100}); when scale = 0.5, the equivalent position is
      Click({x:50, y:50}).
    """


class Clip(TypedDict, total=False):
    height: Required[float]
    """Height of the clip"""

    width: Required[float]
    """Width of the clip"""

    x: Required[float]
    """X coordinate of the clip"""

    y: Required[float]
    """Y coordinate of the clip"""
