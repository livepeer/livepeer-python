"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import multistream_target_patch_payload as components_multistream_target_patch_payload
from ...models.errors import error as errors_error
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclasses.dataclass
class UpdateMultistreamTargetRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""ID of the multistream target"""
    multistream_target_patch_payload: components_multistream_target_patch_payload.MultistreamTargetPatchPayload = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateMultistreamTargetResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    error: Optional[errors_error.Error] = dataclasses.field(default=None)
    r"""Error"""
    

