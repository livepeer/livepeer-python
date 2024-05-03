"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import playback_info as components_playback_info
from typing import Optional


@dataclasses.dataclass
class GetPlaybackInfoRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""The playback ID from the asset or livestream, e.g. `eaw4nk06ts2d0mzb`."""
    



@dataclasses.dataclass
class GetPlaybackInfoResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    playback_info: Optional[components_playback_info.PlaybackInfo] = dataclasses.field(default=None)
    r"""Successful response"""
    
