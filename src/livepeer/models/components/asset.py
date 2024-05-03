"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .creator_id import CreatorID1
from .encryption import Encryption
from .encryption_output import EncryptionOutput
from .ipfs_file_info import IpfsFileInfo
from .ipfs_file_info_input import IpfsFileInfoInput
from .playback_policy import PlaybackPolicy
from .storage_status import StorageStatus
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from livepeer import utils
from typing import Any, List, Optional, Union

class AssetType(str, Enum):
    r"""Type of the asset."""
    VIDEO = 'video'
    AUDIO = 'audio'

class AssetSource3Type(str, Enum):
    DIRECT_UPLOAD = 'directUpload'
    CLIP = 'clip'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AssetSource3:
    type: AssetSource3Type = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    encryption: Optional[EncryptionOutput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('encryption'), 'exclude': lambda f: f is None }})
    source_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceId'), 'exclude': lambda f: f is None }})
    r"""ID of the asset or stream from which this asset was created."""
    session_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sessionId'), 'exclude': lambda f: f is None }})
    r"""ID of the session from which this asset was created."""
    playback_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('playbackId'), 'exclude': lambda f: f is None }})
    r"""Playback ID of the asset or stream from which this asset was created."""
    requester_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('requesterId'), 'exclude': lambda f: f is None }})
    r"""ID of the requester from which this asset was created."""
    asset_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('assetId'), 'exclude': lambda f: f is None }})
    r"""ID of the asset from which this asset was created."""
    


class AssetSourceType(str, Enum):
    RECORDING = 'recording'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Two:
    type: AssetSourceType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    session_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sessionId') }})
    r"""ID of the session from which this asset was created"""
    


class SourceType(str, Enum):
    URL = 'url'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Source1:
    type: SourceType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url') }})
    r"""URL from which the asset was uploaded."""
    gateway_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gatewayUrl'), 'exclude': lambda f: f is None }})
    r"""Gateway URL from asset if parsed from provided URL on upload."""
    encryption: Optional[EncryptionOutput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('encryption'), 'exclude': lambda f: f is None }})
    


class AssetNftMetadataTemplate(str, Enum):
    r"""Name of the NFT metadata template to export. 'player'
    will embed the Livepeer Player on the NFT while 'file'
    will reference only the immutable MP4 files.
    """
    FILE = 'file'
    PLAYER = 'player'


@dataclasses.dataclass
class AssetNftMetadata:
    r"""Additional data to add to the NFT metadata exported to
    IPFS. Will be deep merged with the default metadata
    exported.
    """
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AssetSpec:
    nft_metadata_template: Optional[AssetNftMetadataTemplate] = dataclasses.field(default=AssetNftMetadataTemplate.FILE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nftMetadataTemplate'), 'exclude': lambda f: f is None }})
    r"""Name of the NFT metadata template to export. 'player'
    will embed the Livepeer Player on the NFT while 'file'
    will reference only the immutable MP4 files.
    """
    nft_metadata: Optional[AssetNftMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nftMetadata'), 'exclude': lambda f: f is None }})
    r"""Additional data to add to the NFT metadata exported to
    IPFS. Will be deep merged with the default metadata
    exported.
    """
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AssetIpfs:
    spec: Optional[AssetSpec] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('spec'), 'exclude': lambda f: f is None }})
    dollar_ref: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('$ref'), 'exclude': lambda f: f is None }})
    nft_metadata: Optional[IpfsFileInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nftMetadata'), 'exclude': lambda f: f is None }})
    updated_at: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt'), 'exclude': lambda f: f is None }})
    r"""Timestamp (in milliseconds) at which IPFS export task was
    updated
    """
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AssetStorage:
    ipfs: Optional[AssetIpfs] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ipfs'), 'exclude': lambda f: f is None }})
    status: Optional[StorageStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    


class AssetPhase(str, Enum):
    r"""Phase of the asset"""
    UPLOADING = 'uploading'
    WAITING = 'waiting'
    PROCESSING = 'processing'
    READY = 'ready'
    FAILED = 'failed'
    DELETING = 'deleting'
    DELETED = 'deleted'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AssetStatus:
    r"""Status of the asset"""
    phase: AssetPhase = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phase') }})
    r"""Phase of the asset"""
    updated_at: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt') }})
    r"""Timestamp (in milliseconds) at which the asset was last updated"""
    progress: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('progress'), 'exclude': lambda f: f is None }})
    r"""Current progress of the task creating this asset."""
    error_message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errorMessage'), 'exclude': lambda f: f is None }})
    r"""Error message if the asset creation failed."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Hash:
    hash: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hash'), 'exclude': lambda f: f is None }})
    r"""Hash of the asset"""
    algorithm: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('algorithm'), 'exclude': lambda f: f is None }})
    r"""Hash algorithm used to compute the hash"""
    


class AssetVideoSpecType(str, Enum):
    r"""type of track"""
    VIDEO = 'video'
    AUDIO = 'audio'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Tracks:
    type: AssetVideoSpecType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""type of track"""
    codec: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('codec') }})
    r"""Codec of the track"""
    start_time: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('startTime'), 'exclude': lambda f: f is None }})
    r"""Start time of the track in seconds"""
    duration: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('duration'), 'exclude': lambda f: f is None }})
    r"""Duration of the track in seconds"""
    bitrate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bitrate'), 'exclude': lambda f: f is None }})
    r"""Bitrate of the track in bits per second"""
    width: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('width'), 'exclude': lambda f: f is None }})
    r"""Width of the track - only for video tracks"""
    height: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('height'), 'exclude': lambda f: f is None }})
    r"""Height of the track - only for video tracks"""
    pixel_format: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pixelFormat'), 'exclude': lambda f: f is None }})
    r"""Pixel format of the track - only for video tracks"""
    fps: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fps'), 'exclude': lambda f: f is None }})
    r"""Frame rate of the track - only for video tracks"""
    channels: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('channels'), 'exclude': lambda f: f is None }})
    r"""Amount of audio channels in the track"""
    sample_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sampleRate'), 'exclude': lambda f: f is None }})
    r"""Sample rate of the track in samples per second - only for
    audio tracks
    """
    bit_depth: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bitDepth'), 'exclude': lambda f: f is None }})
    r"""Bit depth of the track - only for audio tracks"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class VideoSpec:
    r"""Video metadata"""
    format: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format'), 'exclude': lambda f: f is None }})
    r"""Format of the asset"""
    duration: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('duration'), 'exclude': lambda f: f is None }})
    r"""Duration of the asset in seconds (float)"""
    bitrate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bitrate'), 'exclude': lambda f: f is None }})
    r"""Bitrate of the video in bits per second"""
    tracks: Optional[List[Tracks]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tracks'), 'exclude': lambda f: f is None }})
    r"""List of tracks associated with the asset when the format
    contemplates them (e.g. mp4)
    """
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Asset:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    source: Union[Source1, Two, AssetSource3] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the asset. This is not necessarily the filename - it can be a custom name or title."""
    type: Optional[AssetType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    r"""Type of the asset."""
    playback_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('playbackId'), 'exclude': lambda f: f is None }})
    r"""The playback ID to use with the Playback Info endpoint to retrieve playback URLs."""
    user_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userId'), 'exclude': lambda f: f is None }})
    r"""Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible."""
    playback_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('playbackUrl'), 'exclude': lambda f: f is None }})
    r"""URL for HLS playback. **It is recommended to not use this URL**, and instead use playback IDs with the Playback Info endpoint to retrieve the playback URLs - this URL format is subject to change (e.g. https://livepeercdn.com/asset/ea03f37e-f861-4cdd-b495-0e60b6d753ad/index.m3u8)."""
    download_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('downloadUrl'), 'exclude': lambda f: f is None }})
    r"""The URL to directly download the asset, e.g. `https://livepeercdn.com/asset/eawrrk06ts2d0mzb/video`. It is not recommended to use this for playback."""
    playback_policy: Optional[PlaybackPolicy] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('playbackPolicy'), 'exclude': lambda f: f is None }})
    r"""Whether the playback policy for a asset or stream is public or signed"""
    creator_id: Optional[Union[CreatorID1]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('creatorId'), 'exclude': lambda f: f is None }})
    storage: Optional[AssetStorage] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage'), 'exclude': lambda f: f is None }})
    status: Optional[AssetStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""Status of the asset"""
    project_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('projectId'), 'exclude': lambda f: f is None }})
    r"""The ID of the project"""
    created_at: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt'), 'exclude': lambda f: f is None }})
    r"""Timestamp (in milliseconds) at which asset was created"""
    created_by_token_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdByTokenName'), 'exclude': lambda f: f is None }})
    r"""Name of the token used to create this object"""
    size: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('size'), 'exclude': lambda f: f is None }})
    r"""Size of the asset in bytes"""
    hash: Optional[List[Hash]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hash'), 'exclude': lambda f: f is None }})
    r"""Hash of the asset"""
    video_spec: Optional[VideoSpec] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('videoSpec'), 'exclude': lambda f: f is None }})
    r"""Video metadata"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Source3:
    type: AssetSource3Type = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    encryption: Optional[Encryption] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('encryption'), 'exclude': lambda f: f is None }})
    source_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceId'), 'exclude': lambda f: f is None }})
    r"""ID of the asset or stream from which this asset was created."""
    session_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sessionId'), 'exclude': lambda f: f is None }})
    r"""ID of the session from which this asset was created."""
    playback_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('playbackId'), 'exclude': lambda f: f is None }})
    r"""Playback ID of the asset or stream from which this asset was created."""
    requester_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('requesterId'), 'exclude': lambda f: f is None }})
    r"""ID of the requester from which this asset was created."""
    asset_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('assetId'), 'exclude': lambda f: f is None }})
    r"""ID of the asset from which this asset was created."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class One:
    type: SourceType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url') }})
    r"""URL from which the asset was uploaded."""
    gateway_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gatewayUrl'), 'exclude': lambda f: f is None }})
    r"""Gateway URL from asset if parsed from provided URL on upload."""
    encryption: Optional[Encryption] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('encryption'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AssetIpfsInput:
    spec: Optional[AssetSpec] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('spec'), 'exclude': lambda f: f is None }})
    dollar_ref: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('$ref'), 'exclude': lambda f: f is None }})
    nft_metadata: Optional[IpfsFileInfoInput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nftMetadata'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AssetStorageInput:
    ipfs: Optional[AssetIpfsInput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ipfs'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AssetInput:
    source: Union[One, Two, Source3] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the asset. This is not necessarily the filename - it can be a custom name or title."""
    type: Optional[AssetType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    r"""Type of the asset."""
    playback_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('playbackId'), 'exclude': lambda f: f is None }})
    r"""The playback ID to use with the Playback Info endpoint to retrieve playback URLs."""
    static_mp4: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('staticMp4'), 'exclude': lambda f: f is None }})
    r"""Whether to generate MP4s for the asset."""
    playback_policy: Optional[PlaybackPolicy] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('playbackPolicy'), 'exclude': lambda f: f is None }})
    r"""Whether the playback policy for a asset or stream is public or signed"""
    creator_id: Optional[Union[CreatorID1]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('creatorId'), 'exclude': lambda f: f is None }})
    storage: Optional[AssetStorageInput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage'), 'exclude': lambda f: f is None }})
    project_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('projectId'), 'exclude': lambda f: f is None }})
    r"""The ID of the project"""
    hash: Optional[List[Hash]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hash'), 'exclude': lambda f: f is None }})
    r"""Hash of the asset"""
    
