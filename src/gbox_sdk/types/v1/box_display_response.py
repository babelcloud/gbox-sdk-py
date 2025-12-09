# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BoxDisplayResponse", "Resolution"]


class Resolution(BaseModel):
    """Resolution configuration"""

    height: float
    """Height of the screen"""

    width: float
    """Width of the screen"""


class BoxDisplayResponse(BaseModel):
    """Box display"""

    orientation: Literal["portrait", "landscapeLeft", "portraitUpsideDown", "landscapeRight"]
    """Orientation of the box"""

    resolution: Resolution
    """Resolution configuration"""
