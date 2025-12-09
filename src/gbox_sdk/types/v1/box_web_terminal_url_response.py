# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["BoxWebTerminalURLResponse"]


class BoxWebTerminalURLResponse(BaseModel):
    """Web terminal result"""

    url: str
    """Web terminal url"""
