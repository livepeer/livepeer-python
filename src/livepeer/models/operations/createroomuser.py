"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from livepeer.models.components import (
    httpmetadata as components_httpmetadata,
    room_user_payload as components_room_user_payload,
    room_user_response as components_room_user_response,
)
from livepeer.models.errors import error as errors_error
from livepeer.types import BaseModel
from livepeer.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class CreateRoomUserRequestTypedDict(TypedDict):
    id: str
    room_user_payload: components_room_user_payload.RoomUserPayloadTypedDict


class CreateRoomUserRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    room_user_payload: Annotated[
        components_room_user_payload.RoomUserPayload,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class CreateRoomUserResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    room_user_response: NotRequired[
        components_room_user_response.RoomUserResponseTypedDict
    ]
    r"""Success"""
    error: NotRequired[errors_error.Error]
    r"""Error"""


class CreateRoomUserResponse(BaseModel):
    http_meta: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    room_user_response: Optional[components_room_user_response.RoomUserResponse] = None
    r"""Success"""

    error: Optional[errors_error.Error] = None
    r"""Error"""
