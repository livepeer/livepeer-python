"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from livepeer.types import BaseModel
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class IpfsFileInfoTypedDict(TypedDict):
    cid: str
    r"""CID of the file on IPFS"""
    url: NotRequired[str]
    r"""URL with IPFS scheme for the file"""
    gateway_url: NotRequired[str]
    r"""URL to access file via HTTP through an IPFS gateway"""


class IpfsFileInfo(BaseModel):
    cid: str
    r"""CID of the file on IPFS"""

    url: Optional[str] = None
    r"""URL with IPFS scheme for the file"""

    gateway_url: Annotated[Optional[str], pydantic.Field(alias="gatewayUrl")] = None
    r"""URL to access file via HTTP through an IPFS gateway"""
