# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "ModelCallResponse",
    "Response",
    "ResponseModelClickResponseData",
    "ResponseModelClickResponseDataCoordinates",
    "ResponseModelDragResponseData",
    "ResponseModelDragResponseDataCoordinates",
    "ResponseModelDragResponseDataCoordinatesDestination",
    "ResponseModelDragResponseDataCoordinatesTarget",
    "ResponseModelScrollResponseData",
    "ResponseModelScrollResponseDataCoordinates",
]


class ResponseModelClickResponseDataCoordinates(BaseModel):
    """Single click result with coordinates"""

    x: float
    """X coordinate. Returns -1 if no valid target is found."""

    y: float
    """Y coordinate. Returns -1 if no valid target is found."""


class ResponseModelClickResponseData(BaseModel):
    """Model click response data structure"""

    coordinates: ResponseModelClickResponseDataCoordinates
    """Single click result with coordinates"""

    type: Literal["click", "drag", "scroll"]
    """Action type"""


class ResponseModelDragResponseDataCoordinatesDestination(BaseModel):
    """X and Y coordinates. Returns -1, -1 if no valid target is found."""

    x: float
    """X coordinate. Returns -1 if no valid target is found."""

    y: float
    """Y coordinate. Returns -1 if no valid target is found."""


class ResponseModelDragResponseDataCoordinatesTarget(BaseModel):
    """X and Y coordinates. Returns -1, -1 if no valid target is found."""

    x: float
    """X coordinate. Returns -1 if no valid target is found."""

    y: float
    """Y coordinate. Returns -1 if no valid target is found."""


class ResponseModelDragResponseDataCoordinates(BaseModel):
    """Single drag result with target and destination coordinates"""

    destination: ResponseModelDragResponseDataCoordinatesDestination
    """X and Y coordinates. Returns -1, -1 if no valid target is found."""

    target: ResponseModelDragResponseDataCoordinatesTarget
    """X and Y coordinates. Returns -1, -1 if no valid target is found."""


class ResponseModelDragResponseData(BaseModel):
    """Drag response data structure"""

    coordinates: ResponseModelDragResponseDataCoordinates
    """Single drag result with target and destination coordinates"""

    type: Literal["click", "drag", "scroll"]
    """Action type"""


class ResponseModelScrollResponseDataCoordinates(BaseModel):
    """Single scroll result with location and direction"""

    scroll_x: float = FieldInfo(alias="scrollX")
    """Horizontal scroll amount"""

    scroll_y: float = FieldInfo(alias="scrollY")
    """Vertical scroll amount"""

    x: float
    """X coordinate"""

    y: float
    """Y coordinate"""


class ResponseModelScrollResponseData(BaseModel):
    """Scroll response data structure"""

    coordinates: ResponseModelScrollResponseDataCoordinates
    """Single scroll result with location and direction"""

    type: Literal["click", "drag", "scroll"]
    """Action type"""


Response: TypeAlias = Union[
    ResponseModelClickResponseData, ResponseModelDragResponseData, ResponseModelScrollResponseData
]


class ModelCallResponse(BaseModel):
    """Model response data structure"""

    id: str
    """Unique ID of this request, can be used for issue reporting and feedback"""

    response: Response
    """Model response data"""
