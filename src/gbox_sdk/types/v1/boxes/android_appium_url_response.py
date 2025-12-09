# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["AndroidAppiumURLResponse", "DefaultOption", "DefaultOptionCapabilities"]


class DefaultOptionCapabilities(BaseModel):
    """Appium capabilities for WebdriverIO"""

    appium_automation_name: str = FieldInfo(alias="appium:automationName")
    """Appium automation name"""

    appium_device_name: str = FieldInfo(alias="appium:deviceName")
    """Device name"""

    appium_udid: str = FieldInfo(alias="appium:udid")
    """Device UDID"""

    platform_name: str = FieldInfo(alias="platformName")
    """Platform name"""


class DefaultOption(BaseModel):
    """Ready-to-use WebdriverIO remote options"""

    capabilities: DefaultOptionCapabilities
    """Appium capabilities for WebdriverIO"""

    hostname: str
    """Hostname"""

    path: str
    """URL pathname"""

    port: float
    """Port number"""

    protocol: str
    """Protocol (http or https)"""


class AndroidAppiumURLResponse(BaseModel):
    """Appium connection information"""

    default_option: DefaultOption = FieldInfo(alias="defaultOption")
    """Ready-to-use WebdriverIO remote options"""

    log_level: Literal["trace", "debug", "info", "warn", "error", "silent"] = FieldInfo(alias="logLevel")
    """Log level for WebdriverIO/Appium client"""

    udid: str
    """Device UDID for Appium connection"""

    url: str
    """Appium connection URL"""
