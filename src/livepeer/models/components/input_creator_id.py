"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from livepeer import utils
from typing import Union


class InputCreatorIDType(str, Enum):
    UNVERIFIED = 'unverified'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class InputCreatorID1:
    type: InputCreatorIDType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    value: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value') }})
    


InputCreatorID = Union[InputCreatorID1, str]
