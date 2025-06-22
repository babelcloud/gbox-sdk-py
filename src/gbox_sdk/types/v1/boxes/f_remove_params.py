# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["FRemoveParams"]


class FRemoveParams(TypedDict, total=False):
    path: Required[str]
    """Path to the file/directory.

    If the path is not start with '/', the file/directory will be deleted from the
    working directory. If target path is not exists, the delete will be failed.
    """

    working_dir: Annotated[str, PropertyInfo(alias="workingDir")]
    """Working directory.

    If not provided, the file will be read from the `box.config.workingDir`
    directory.
    """
