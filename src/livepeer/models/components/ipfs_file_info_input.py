"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from livepeer import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class IpfsFileInfoInput:
    cid: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cid') }})
    r"""CID of the file on IPFS"""
    
