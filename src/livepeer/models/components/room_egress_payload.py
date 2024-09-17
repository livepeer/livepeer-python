"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from livepeer.types import BaseModel
import pydantic
from typing import TypedDict
from typing_extensions import Annotated


class RoomEgressPayloadTypedDict(TypedDict):
    stream_id: str
    r"""The ID of the Livepeer Stream to stream to"""


class RoomEgressPayload(BaseModel):
    stream_id: Annotated[str, pydantic.Field(alias="streamId")]
    r"""The ID of the Livepeer Stream to stream to"""
