"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import get_room_user_response as components_get_room_user_response
from ...models.components import httpmetadata as components_httpmetadata
from ...models.errors import error as errors_error
from typing import Optional


@dataclasses.dataclass
class GetRoomUserRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    user_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'userId', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class GetRoomUserResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    get_room_user_response: Optional[components_get_room_user_response.GetRoomUserResponse] = dataclasses.field(default=None)
    r"""Success"""
    error: Optional[errors_error.Error] = dataclasses.field(default=None)
    r"""Error"""
    
