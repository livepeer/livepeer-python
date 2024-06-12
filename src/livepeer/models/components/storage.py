"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .spec import Spec
from dataclasses_json import Undefined, dataclass_json
from livepeer import utils
from typing import Optional, Union


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Ipfs1:
    UNSET='__SPEAKEASY_UNSET__'
    spec: Optional[Spec] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('spec'), 'exclude': lambda f: f is Ipfs1.UNSET }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Storage:
    UNSET='__SPEAKEASY_UNSET__'
    ipfs: Optional[Ipfs] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ipfs'), 'exclude': lambda f: f is Storage.UNSET }})
    r"""Set to true to make default export to IPFS. To customize the
    pinned files, specify an object with a spec field. False or null
    means to unpin from IPFS, but it's unsupported right now.
    """
    


Ipfs = Union[Ipfs1, bool]
