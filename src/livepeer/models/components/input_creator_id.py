"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from livepeer.types import BaseModel
from typing import TypedDict, Union


class InputCreatorIDType(str, Enum):
    UNVERIFIED = "unverified"


class InputCreatorID1TypedDict(TypedDict):
    type: InputCreatorIDType
    value: str


class InputCreatorID1(BaseModel):
    type: InputCreatorIDType

    value: str


InputCreatorIDTypedDict = Union[InputCreatorID1TypedDict, str]


InputCreatorID = Union[InputCreatorID1, str]
