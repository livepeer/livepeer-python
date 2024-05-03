"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from livepeer import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RoomUserUpdatePayload:
    can_publish: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('canPublish'), 'exclude': lambda f: f is None }})
    r"""Whether a user is allowed to publish audio/video tracks (i.e. their microphone and webcam)"""
    can_publish_data: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('canPublishData'), 'exclude': lambda f: f is None }})
    r"""Whether a user is allowed to publish data messages to the room"""
    metadata: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    r"""User defined payload to store for the participant"""
    

