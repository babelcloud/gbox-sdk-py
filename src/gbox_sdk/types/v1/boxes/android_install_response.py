# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["AndroidInstallResponse", "Activity"]


class Activity(BaseModel):
    class_name: str = FieldInfo(alias="className")
    """Activity class name"""

    is_exported: bool = FieldInfo(alias="isExported")
    """Activity class name"""

    is_main: bool = FieldInfo(alias="isMain")
    """Whether the activity is the main activity"""

    name: str
    """Activity name"""

    package_name: str = FieldInfo(alias="packageName")
    """Activity package name"""


class AndroidInstallResponse(BaseModel):
    activities: List[Activity]
    """Activity list"""

    apk_path: str = FieldInfo(alias="apkPath")
    """Android app apk path"""

    app_type: Literal["system", "third-party"] = FieldInfo(alias="appType")
    """Application type: system or third-party"""

    package_name: str = FieldInfo(alias="packageName")
    """Android app package name"""
