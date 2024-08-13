"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .encryption import Encryption
from .input_creator_id import InputCreatorID
from .playback_policy import PlaybackPolicy
from .storage import Storage
from .transcode_profile import TranscodeProfile
from dataclasses_json import Undefined, dataclass_json
from livepeer import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class NewAssetFromURLPayload:
    UNSET='__SPEAKEASY_UNSET__'
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the asset. This is not necessarily the filename - it can be a custom name or title."""
    url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url') }})
    r"""URL where the asset contents can be retrieved, e.g. `https://s3.amazonaws.com/my-bucket/path/filename.mp4`.
    For an IPFS source, this should be similar to: `ipfs://{CID}`. For an Arweave
    source: `ar://{CID}`.
    """
    static_mp4: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('staticMp4'), 'exclude': lambda f: f is None }})
    r"""Whether to generate MP4s for the asset."""
    playback_policy: Optional[PlaybackPolicy] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('playbackPolicy'), 'exclude': lambda f: f is NewAssetFromURLPayload.UNSET }})
    r"""Whether the playback policy for an asset or stream is public or signed"""
    creator_id: Optional[InputCreatorID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('creatorId'), 'exclude': lambda f: f is None }})
    storage: Optional[Storage] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage'), 'exclude': lambda f: f is None }})
    encryption: Optional[Encryption] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('encryption'), 'exclude': lambda f: f is None }})
    c2pa: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('c2pa'), 'exclude': lambda f: f is None }})
    r"""Decides if the output video should include C2PA signature"""
    profiles: Optional[List[TranscodeProfile]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('profiles'), 'exclude': lambda f: f is NewAssetFromURLPayload.UNSET }})
    target_segment_size_secs: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('targetSegmentSizeSecs'), 'exclude': lambda f: f is None }})
    r"""How many seconds the duration of each output segment should be"""
    

