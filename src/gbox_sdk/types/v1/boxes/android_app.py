# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["AndroidApp"]


class AndroidApp(BaseModel):
    apk_path: str = FieldInfo(alias="apkPath")
    """Android app apk path"""

    name: str
    """Android app name"""

    package_name: str = FieldInfo(alias="packageName")
    """Android app package name"""

    version: str
    """Android app version"""
