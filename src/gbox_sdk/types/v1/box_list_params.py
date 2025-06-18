# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BoxListParams"]


class BoxListParams(TypedDict, total=False):
    labels: object
    """Filter boxes by their labels, default is all"""

    page: int
    """Page number"""

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Page size"""

    status: str
    """
    Filter boxes by their current status (pending, running, stopped, error,
    terminated).
    """

    type: str
    """Filter boxes by their type (linux, android etc.) , default is all"""
