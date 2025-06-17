# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["FInfoResponse"]


class FInfoResponse(BaseModel):
    path: str
    """Path to the file/directory.

    If the path is not start with '/', the file/directory will be checked from the
    working directory
    """

    working_dir: Optional[str] = FieldInfo(alias="workingDir", default=None)
    """Working directory.

    If not provided, the file will be read from the root directory.
    """
