# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["AndroidListSimpleResponse", "Data"]


class Data(BaseModel):
    apk_path: str = FieldInfo(alias="apkPath")
    """Android app apk path"""

    app_type: Literal["system", "thirdParty"] = FieldInfo(alias="appType")
    """Application type: system or third-party"""

    package_name: str = FieldInfo(alias="packageName")
    """Android app package name"""


class AndroidListSimpleResponse(BaseModel):
    data: List[Data]
    """Android app simple list"""
