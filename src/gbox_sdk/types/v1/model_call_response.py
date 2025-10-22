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
    x: float
    """X coordinate. Returns -1 if no valid target is found."""

    y: float
    """Y coordinate. Returns -1 if no valid target is found."""


class ResponseModelClickResponseData(BaseModel):
    coordinates: ResponseModelClickResponseDataCoordinates
    """Single click result with coordinates"""

    type: Literal["click", "drag", "scroll"]
    """Action type"""


class ResponseModelDragResponseDataCoordinatesDestination(BaseModel):
    x: float
    """X coordinate. Returns -1 if no valid target is found."""

    y: float
    """Y coordinate. Returns -1 if no valid target is found."""


class ResponseModelDragResponseDataCoordinatesTarget(BaseModel):
    x: float
    """X coordinate. Returns -1 if no valid target is found."""

    y: float
    """Y coordinate. Returns -1 if no valid target is found."""


class ResponseModelDragResponseDataCoordinates(BaseModel):
    destination: ResponseModelDragResponseDataCoordinatesDestination
    """X and Y coordinates. Returns -1, -1 if no valid target is found."""

    target: ResponseModelDragResponseDataCoordinatesTarget
    """X and Y coordinates. Returns -1, -1 if no valid target is found."""


class ResponseModelDragResponseData(BaseModel):
    coordinates: ResponseModelDragResponseDataCoordinates
    """Single drag result with target and destination coordinates"""

    type: Literal["click", "drag", "scroll"]
    """Action type"""


class ResponseModelScrollResponseDataCoordinates(BaseModel):
    scroll_x: float = FieldInfo(alias="scrollX")
    """Horizontal scroll amount"""

    scroll_y: float = FieldInfo(alias="scrollY")
    """Vertical scroll amount"""

    x: float
    """X coordinate"""

    y: float
    """Y coordinate"""


class ResponseModelScrollResponseData(BaseModel):
    coordinates: ResponseModelScrollResponseDataCoordinates
    """Single scroll result with location and direction"""

    type: Literal["click", "drag", "scroll"]
    """Action type"""


Response: TypeAlias = Union[
    ResponseModelClickResponseData, ResponseModelDragResponseData, ResponseModelScrollResponseData
]


class ModelCallResponse(BaseModel):
    id: str
    """Unique ID of this request, can be used for issue reporting and feedback"""

    response: Response
    """Model response data"""
