# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["SnapshotListResponse", "Data"]


class Data(BaseModel):
    """Snapshot configuration"""

    id: str
    """Unique identifier for the snapshot"""

    box_type: Literal["linux", "android", "windows"] = FieldInfo(alias="boxType")
    """The type of the box that the snapshot is taken from"""

    name: str
    """Name of the snapshot. This name must be unique within the organization."""

    provider_type: Literal["vm"] = FieldInfo(alias="providerType")
    """The provider type of the snapshot"""

    status: Literal["Pending", "Available", "Error"]
    """The status of the snapshot"""


class SnapshotListResponse(BaseModel):
    """Response containing paginated list of snapshots"""

    data: List[Data]
    """List of snapshots"""

    page: int
    """Page number"""

    page_size: int = FieldInfo(alias="pageSize")
    """Page size"""

    total: int
    """Total number of items"""
