# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["BrowserOpenTabResponse"]


class BrowserOpenTabResponse(BaseModel):
    favicon: str
    """The tab favicon"""

    index: float
    """The tab index, starting from 0"""

    title: str
    """The tab title"""

    url: str
    """The tab url"""
