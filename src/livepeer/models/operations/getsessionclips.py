"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import asset as components_asset
from ...models.components import httpmetadata as components_httpmetadata
from ...models.errors import error as errors_error
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional


@dataclasses.dataclass
class GetSessionClipsRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""ID of the parent session"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSessionClipsResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    data: Optional[List[components_asset.Asset]] = dataclasses.field(default=None)
    r"""Success"""
    error: Optional[errors_error.Error] = dataclasses.field(default=None)
    r"""Error"""
    

