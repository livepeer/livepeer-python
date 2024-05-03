"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import asset as components_asset
from ...models.components import httpmetadata as components_httpmetadata
from ...models.errors import error as errors_error
from dataclasses_json import Undefined, dataclass_json
from livepeer import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UploadAssetTask:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UploadAssetData:
    r"""Success"""
    asset: components_asset.Asset = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('asset') }})
    task: UploadAssetTask = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('task') }})
    



@dataclasses.dataclass
class UploadAssetResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    data: Optional[UploadAssetData] = dataclasses.field(default=None)
    r"""Success"""
    error: Optional[errors_error.Error] = dataclasses.field(default=None)
    r"""Error"""
    
