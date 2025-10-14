# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["AndroidAppiumURLResponse"]


class AndroidAppiumURLResponse(BaseModel):
    default_option: object = FieldInfo(alias="defaultOption")
    """A ready-to-use default WebdriverIO remote options object"""

    udid: str
    """Device UDID for Appium connection"""

    url: str
    """Appium connection URL"""
