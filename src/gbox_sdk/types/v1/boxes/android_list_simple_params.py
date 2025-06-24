# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["AndroidListSimpleParams"]


class AndroidListSimpleParams(TypedDict, total=False):
    app_type: Annotated[List[Literal["system", "thirdParty"]], PropertyInfo(alias="appType")]
    """Application type: system or third-party, default is third-party"""
