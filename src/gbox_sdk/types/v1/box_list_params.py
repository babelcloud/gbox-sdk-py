# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BoxListParams"]


class BoxListParams(TypedDict, total=False):
    page: float
    """Page number"""

    page_size: Annotated[float, PropertyInfo(alias="pageSize")]
    """Page size"""
