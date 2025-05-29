# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel

__all__ = ["FListResponse"]


class FListResponse(BaseModel):
    data: List[object]
    """A box instance that can be either Linux or Android type"""
