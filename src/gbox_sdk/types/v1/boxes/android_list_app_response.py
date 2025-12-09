# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .android_app import AndroidApp

__all__ = ["AndroidListAppResponse"]


class AndroidListAppResponse(BaseModel):
    """Android app list"""

    data: List[AndroidApp]
    """App list"""
