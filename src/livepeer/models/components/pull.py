"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from livepeer import utils
from typing import Dict, Optional, Union


class One(int, Enum):
    r"""0: not mobile, 1: mobile screen share, 2: mobile camera."""
    ZERO = 0
    ONE = 1
    TWO = 2


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Location:
    r"""Approximate location of the pull source. The location is used to
    determine the closest Livepeer region to pull the stream from.
    """
    lat: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lat') }})
    r"""Latitude of the pull source in degrees. North is positive,
    south is negative.
    """
    lon: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lon') }})
    r"""Longitude of the pull source in degrees. East is positive,
    west is negative.
    """
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Pull:
    r"""Configuration for a stream that should be actively pulled from an
    external source, rather than pushed to Livepeer. If specified, the
    stream will not have a streamKey.
    """
    source: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source') }})
    r"""URL from which to pull from."""
    headers: Optional[Dict[str, str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('headers'), 'exclude': lambda f: f is None }})
    r"""Headers to be sent with the request to the pull source."""
    is_mobile: Optional[IsMobile] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isMobile'), 'exclude': lambda f: f is None }})
    r"""Indicates whether the stream will be pulled from a mobile source."""
    location: Optional[Location] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('location'), 'exclude': lambda f: f is None }})
    r"""Approximate location of the pull source. The location is used to
    determine the closest Livepeer region to pull the stream from.
    """
    


IsMobile = Union[One, bool]
