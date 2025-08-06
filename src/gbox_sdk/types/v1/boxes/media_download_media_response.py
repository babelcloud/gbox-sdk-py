# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["MediaDownloadMediaResponse"]


class MediaDownloadMediaResponse(BaseModel):
    content: str
    """Content of the media file (base64 encoded)"""

    mime_type: str = FieldInfo(alias="mimeType")
    """MIME type of the media file"""

    name: str
    """Name of the media file"""

    size: str
    """Size of the media file"""
