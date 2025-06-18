# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BoxListParams"]


class BoxListParams(TypedDict, total=False):
    labels: object
    """Filter boxes by their labels, default is all"""

    page: int
    """Page number"""

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Page size"""

    status: List[Literal["all", "pending", "running", "stopped", "error", "terminated"]]
    """
    Filter boxes by their current status (pending, running, stopped, error,
    terminated, all). Must be an array of statuses. Use 'all' to get boxes with any
    status.
    """

    type: List[Literal["all", "linux", "android"]]
    """Filter boxes by their type (linux, android, all).

    Must be an array of types. Use 'all' to get boxes of any type.
    """
