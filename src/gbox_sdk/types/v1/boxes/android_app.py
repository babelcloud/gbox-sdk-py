# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["AndroidApp"]


class AndroidApp(BaseModel):
    apk_path: str = FieldInfo(alias="apkPath")
    """Android app apk path"""

    app_type: Literal["system", "thirdParty"] = FieldInfo(alias="appType")
    """Application type: system or third-party"""

    is_running: bool = FieldInfo(alias="isRunning")
    """Whether the application is currently running"""

    name: str
    """Android app name"""

    package_name: str = FieldInfo(alias="packageName")
    """Android app package name"""

    version: str
    """Android app version"""
