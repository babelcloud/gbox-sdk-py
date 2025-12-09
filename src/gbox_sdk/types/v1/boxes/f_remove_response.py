# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["FRemoveResponse"]


class FRemoveResponse(BaseModel):
    """Response after deleting file/directory"""

    message: str
    """Success message"""
