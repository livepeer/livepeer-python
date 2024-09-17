"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from livepeer.models.components import (
    httpmetadata as components_httpmetadata,
    room_egress_payload as components_room_egress_payload,
)
from livepeer.models.errors import error as errors_error
from livepeer.types import BaseModel
from livepeer.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class StartRoomEgressRequestTypedDict(TypedDict):
    id: str
    room_egress_payload: components_room_egress_payload.RoomEgressPayloadTypedDict


class StartRoomEgressRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    room_egress_payload: Annotated[
        components_room_egress_payload.RoomEgressPayload,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class StartRoomEgressResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    error: NotRequired[errors_error.Error]
    r"""Error"""


class StartRoomEgressResponse(BaseModel):
    http_meta: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    error: Optional[errors_error.Error] = None
    r"""Error"""
