# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["AndroidListAppResponse", "Data"]


class Data(BaseModel):
    apk_path: str = FieldInfo(alias="apkPath")
    """Android apk path"""

    is_running: bool = FieldInfo(alias="isRunning")
    """Whether the pkg is currently running"""

    name: str
    """Android pkg name"""

    package_name: str = FieldInfo(alias="packageName")
    """Android package name"""

    pkg_type: Literal["system", "thirdParty"] = FieldInfo(alias="pkgType")
    """Package type: system or third-party"""

    version: str
    """Android pkg version"""


class AndroidListAppResponse(BaseModel):
    data: List[Data]
    """App list"""
