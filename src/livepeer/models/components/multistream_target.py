"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from livepeer.types import BaseModel
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class MultistreamTargetTypedDict(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]
    user_id: NotRequired[str]
    disabled: NotRequired[bool]
    r"""If true then this multistream target will not be used for pushing
    even if it is configured in a stream object.

    """
    created_at: NotRequired[float]
    r"""Timestamp (in milliseconds) at which multistream target object was
    created

    """


class MultistreamTarget(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None

    user_id: Annotated[
        Optional[str],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible.",
            alias="userId",
        ),
    ] = None

    disabled: Optional[bool] = None
    r"""If true then this multistream target will not be used for pushing
    even if it is configured in a stream object.

    """

    created_at: Annotated[Optional[float], pydantic.Field(alias="createdAt")] = None
    r"""Timestamp (in milliseconds) at which multistream target object was
    created

    """
