# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel

__all__ = ["BrowserGetTabsResponse", "Tab"]


class Tab(BaseModel):
    favicon: str
    """The tab favicon"""

    index: float
    """The tab index, starting from 0"""

    title: str
    """The tab title"""

    url: str
    """The tab url"""


class BrowserGetTabsResponse(BaseModel):
    tabs: List[Tab]
    """The tabs"""
