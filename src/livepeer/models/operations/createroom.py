"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import create_room_response as components_create_room_response
from ...models.components import httpmetadata as components_httpmetadata
from ...models.errors import error as errors_error
from typing import Optional


@dataclasses.dataclass
class CreateRoomResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    create_room_response: Optional[components_create_room_response.CreateRoomResponse] = dataclasses.field(default=None)
    r"""Success"""
    error: Optional[errors_error.Error] = dataclasses.field(default=None)
    r"""Error"""
    

