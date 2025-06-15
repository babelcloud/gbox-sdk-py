# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["FExistsResponse"]


class FExistsResponse(BaseModel):
    exists: bool
    """Exists"""
