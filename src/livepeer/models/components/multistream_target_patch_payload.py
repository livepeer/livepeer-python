"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from livepeer.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class MultistreamTargetPatchPayloadTypedDict(TypedDict):
    url: str
    r"""Livepeer-compatible multistream target URL (RTMP(S) or SRT)"""
    name: NotRequired[str]
    disabled: NotRequired[bool]
    r"""If true then this multistream target will not be used for pushing
    even if it is configured in a stream object.

    """


class MultistreamTargetPatchPayload(BaseModel):
    url: str
    r"""Livepeer-compatible multistream target URL (RTMP(S) or SRT)"""

    name: Optional[str] = None

    disabled: Optional[bool] = None
    r"""If true then this multistream target will not be used for pushing
    even if it is configured in a stream object.

    """
