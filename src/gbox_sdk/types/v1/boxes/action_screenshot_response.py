# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ActionScreenshotResponse"]


class ActionScreenshotResponse(BaseModel):
    """Result of screenshot capture action"""

    uri: str
    """URL of the screenshot"""

    presigned_url: Optional[str] = FieldInfo(alias="presignedUrl", default=None)
    """Presigned url of the screenshot"""
