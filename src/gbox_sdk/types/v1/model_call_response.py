# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ModelCallResponse"]


class ModelCallResponse(BaseModel):
    id: str
    """Unique ID of this request, can be used for issue reporting and feedback"""

    response: object
    """Model response data"""
