# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .linux_box import LinuxBox
from .android_box import AndroidBox

__all__ = ["BoxListResponse", "Data", "DataWindowsBox", "DataWindowsBoxConfig", "DataWindowsBoxConfigOs"]


class DataWindowsBoxConfigOs(BaseModel):
    """Windows operating system configuration"""

    version: Literal["10", "11"]
    """Supported Windows versions"""


class DataWindowsBoxConfig(BaseModel):
    """Windows box instance configuration"""

    arch: object
    """Architecture of the box"""

    cpu: float
    """CPU cores allocated to the box"""

    memory: float
    """Memory allocated to the box in MiB"""

    novnc_url: object = FieldInfo(alias="novncUrl")
    """NOVNC URL of the box"""

    os: DataWindowsBoxConfigOs
    """Windows operating system configuration"""

    public_ip: object = FieldInfo(alias="publicIp")
    """Public IP address of the box"""

    storage: float
    """Storage allocated to the box in GiB"""

    vnc_url: object = FieldInfo(alias="vncUrl")
    """VNC URL of the box"""


class DataWindowsBox(BaseModel):
    """Windows VM box instance with full configuration and status"""

    id: str
    """Unique identifier for the box"""

    config: DataWindowsBoxConfig
    """Windows box instance configuration"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Creation timestamp of the box"""

    expires_at: Optional[datetime] = FieldInfo(alias="expiresAt", default=None)
    """Expiration timestamp of the box"""

    status: Literal["pending", "running", "error", "terminated"]
    """The current status of a box instance"""

    type: Literal["windows"]
    """Box type is Windows"""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Last update timestamp of the box"""

    reason: Optional[str] = None
    """The reason for the current status, if any"""


Data: TypeAlias = Union[LinuxBox, AndroidBox, DataWindowsBox]


class BoxListResponse(BaseModel):
    """Response containing paginated list of box instances"""

    data: List[Data]
    """A box instance that can be Linux, Android, or Windows type"""

    page: int
    """Page number"""

    page_size: int = FieldInfo(alias="pageSize")
    """Page size"""

    total: int
    """Total number of items"""
