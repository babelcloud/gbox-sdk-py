# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["SnapshotCreateResponse"]


class SnapshotCreateResponse(BaseModel):
    """Snapshot configuration"""

    id: str
    """Unique identifier for the snapshot"""

    box_type: Literal["linux", "android"] = FieldInfo(alias="boxType")
    """The type of the box that the snapshot is taken from"""

    name: str
    """Name of the snapshot. This name must be unique within the organization."""

    provider_type: Literal["vm"] = FieldInfo(alias="providerType")
    """The provider type of the snapshot"""

    status: Literal["Pending", "Available", "Error"]
    """The status of the snapshot"""
