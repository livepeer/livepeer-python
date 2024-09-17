"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from livepeer.types import BaseModel
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class RoomUserUpdatePayloadTypedDict(TypedDict):
    can_publish: NotRequired[bool]
    r"""Whether a user is allowed to publish audio/video tracks (i.e. their microphone and webcam)"""
    can_publish_data: NotRequired[bool]
    r"""Whether a user is allowed to publish data messages to the room"""
    metadata: NotRequired[str]
    r"""User defined payload to store for the participant"""


class RoomUserUpdatePayload(BaseModel):
    can_publish: Annotated[Optional[bool], pydantic.Field(alias="canPublish")] = True
    r"""Whether a user is allowed to publish audio/video tracks (i.e. their microphone and webcam)"""

    can_publish_data: Annotated[
        Optional[bool], pydantic.Field(alias="canPublishData")
    ] = True
    r"""Whether a user is allowed to publish data messages to the room"""

    metadata: Optional[str] = None
    r"""User defined payload to store for the participant"""
