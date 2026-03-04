# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BoxCreateWindowsParams", "Config"]


class BoxCreateWindowsParams(TypedDict, total=False):
    config: Config
    """Configuration for a Windows box instance"""

    api_timeout: Annotated[str, PropertyInfo(alias="timeout")]
    """
    Timeout for waiting the box to transition from pending to running state, default
    is 30s. If the box doesn't reach running state within this timeout, the API will
    return HTTP status code 408. The timed-out box will be automatically deleted and
    will not count towards your quota.

    Supported time units: ms (milliseconds), s (seconds), m (minutes), h (hours)
    Example formats: "500ms", "30s", "5m", "1h" Default: 30s Maximum allowed: 5m
    """

    wait: bool
    """Wait for the box operation to be completed, default is true"""


class Config(TypedDict, total=False):
    """Configuration for a Windows box instance"""

    envs: Dict[str, str]
    """Environment variables for the box.

    These variables will be available in all operations including command execution,
    code running, and other box behaviors
    """

    expires_in: Annotated[str, PropertyInfo(alias="expiresIn")]
    """The box will be alive for the given duration

    Supported time units: ms (milliseconds), s (seconds), m (minutes), h (hours)
    Example formats: "500ms", "30s", "5m", "1h" Default: 60m
    """

    keep_alive: Annotated[str, PropertyInfo(alias="keepAlive")]
    """Keep alive duration on activity.

    When set to a positive value (e.g., '5m'), the box expiration time (expiresIn)
    will be automatically extended to ensure at least this duration remains whenever
    there is an box operation on this specific box. For example, when calling UI
    Action, FS, Browser, Command, Media, or Run Code operations with this box's
    boxId, the box will be kept alive. If keepAlive is '5m' and the box has 2
    minutes remaining, any operation on this boxId will extend the remaining time to
    5 minutes. Set to '0ms' to disable automatic keep alive extension. This helps
    keep frequently-used boxes alive without manual intervention.

    Supported time units: ms (milliseconds), s (seconds), m (minutes), h (hours)
    Example formats: "500ms", "30s", "5m", "1h" Default: 0ms
    """

    labels: Dict[str, str]
    """Key-value pairs of labels for the box.

    Labels are used to add custom metadata to help identify, categorize, and manage
    boxes. Common use cases include project names, environments, teams,
    applications, or any other organizational tags that help you organize and filter
    your boxes.
    """

    version: Literal["10", "11"]
    """Windows operating system version"""
