"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .asset import Asset
from .creator_id import CreatorID
from .encryption import Encryption
from .export_task_params import ExportTaskParams
from .input_creator_id import InputCreatorID
from .ipfs_export_params import IpfsExportParams
from .transcode_profile import TranscodeProfile
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Any, Dict, List, Optional, Union

class TaskType(str, Enum):
    r"""Type of the task"""
    UPLOAD = 'upload'
    EXPORT = 'export'
    EXPORT_DATA = 'export-data'
    TRANSCODE_FILE = 'transcode-file'
    CLIP = 'clip'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Upload:
    r"""Parameters for the upload task"""
    c2pa: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('c2pa'), 'exclude': lambda f: f is None }})
    r"""Decides if the output video should include C2PA signature"""
    encryption: Optional[Encryption] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('encryption'), 'exclude': lambda f: f is None }})
    url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url'), 'exclude': lambda f: f is None }})
    r"""URL of the asset to \\"upload\\" """
    



@dataclasses.dataclass
class Content:
    r"""File content to store into IPFS"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ExportData:
    r"""Parameters for the export-data task"""
    content: Content = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('content') }})
    r"""File content to store into IPFS"""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Optional ID of the content"""
    ipfs: Optional[IpfsExportParams] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ipfs'), 'exclude': lambda f: f is None }})
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    r"""Optional type of content"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TaskInput:
    r"""Input video file to transcode"""
    url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url'), 'exclude': lambda f: f is None }})
    r"""URL of a video to transcode, accepts object-store format
    \"s3+https\" 
    """
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TaskStorage:
    r"""Storage for the output files"""
    url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url'), 'exclude': lambda f: f is None }})
    r"""URL of the output storage, accepts object-store format
    \"s3+https\" 
    """
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TaskHls:
    r"""HLS output format"""
    path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('path'), 'exclude': lambda f: f is None }})
    r"""Path for the HLS output"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TaskMp4:
    r"""MP4 output format"""
    path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('path'), 'exclude': lambda f: f is None }})
    r"""Path for the MP4 output"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TaskOutputs:
    r"""Output formats"""
    hls: Optional[TaskHls] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hls'), 'exclude': lambda f: f is None }})
    r"""HLS output format"""
    mp4: Optional[TaskMp4] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mp4'), 'exclude': lambda f: f is None }})
    r"""MP4 output format"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TranscodeFile:
    r"""Parameters for the transcode-file task"""
    c2pa: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('c2pa'), 'exclude': lambda f: f is None }})
    r"""Decides if the output video should include C2PA signature"""
    creator_id: Optional[Union[Union[CreatorID1], str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('creatorId'), 'exclude': lambda f: f is None }})
    input: Optional[TaskInput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('input'), 'exclude': lambda f: f is None }})
    r"""Input video file to transcode"""
    outputs: Optional[TaskOutputs] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('outputs'), 'exclude': lambda f: f is None }})
    r"""Output formats"""
    profiles: Optional[List[TranscodeProfile]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('profiles'), 'exclude': lambda f: f is None }})
    storage: Optional[TaskStorage] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage'), 'exclude': lambda f: f is None }})
    r"""Storage for the output files"""
    target_segment_size_secs: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('targetSegmentSizeSecs'), 'exclude': lambda f: f is None }})
    r"""How many seconds the duration of each output segment should
    be
    """
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ClipStrategy:
    r"""Strategy to use for clipping the asset. If not specified, the default strategy that Catalyst is configured for will be used. This field only available for admin users, and is only used for E2E testing."""
    end_time: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('endTime'), 'exclude': lambda f: f is None }})
    r"""End time of the clip in milliseconds"""
    playback_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('playbackId'), 'exclude': lambda f: f is None }})
    r"""Playback ID of the stream or asset to clip"""
    start_time: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('startTime'), 'exclude': lambda f: f is None }})
    r"""Start time of the clip in milliseconds"""
    


class CatalystPipelineStrategy(str, Enum):
    r"""Force to use a specific strategy in the Catalyst pipeline. If not specified, the default strategy that Catalyst is configured for will be used. This field only available for admin users, and is only used for E2E testing."""
    CATALYST = 'catalyst'
    CATALYST_FFMPEG = 'catalyst_ffmpeg'
    BACKGROUND_EXTERNAL = 'background_external'
    BACKGROUND_MIST = 'background_mist'
    FALLBACK_EXTERNAL = 'fallback_external'
    EXTERNAL = 'external'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Clip:
    catalyst_pipeline_strategy: Optional[CatalystPipelineStrategy] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('catalystPipelineStrategy'), 'exclude': lambda f: f is None }})
    r"""Force to use a specific strategy in the Catalyst pipeline. If not specified, the default strategy that Catalyst is configured for will be used. This field only available for admin users, and is only used for E2E testing."""
    clip_strategy: Optional[ClipStrategy] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clipStrategy'), 'exclude': lambda f: f is None }})
    r"""Strategy to use for clipping the asset. If not specified, the default strategy that Catalyst is configured for will be used. This field only available for admin users, and is only used for E2E testing."""
    input_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('inputId'), 'exclude': lambda f: f is None }})
    r"""ID of the input asset or stream"""
    session_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sessionId'), 'exclude': lambda f: f is None }})
    r"""ID of the session"""
    url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url'), 'exclude': lambda f: f is None }})
    r"""URL of the asset to \\"clip\\" """
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Params:
    r"""Parameters of the task"""
    clip: Optional[Clip] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clip'), 'exclude': lambda f: f is None }})
    export: Optional[Union[ExportTaskParams1, ExportTaskParams2]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('export'), 'exclude': lambda f: f is None }})
    r"""Parameters for the export task"""
    export_data: Optional[ExportData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('exportData'), 'exclude': lambda f: f is None }})
    r"""Parameters for the export-data task"""
    transcode_file: Optional[TranscodeFile] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transcode-file'), 'exclude': lambda f: f is None }})
    r"""Parameters for the transcode-file task"""
    upload: Optional[Upload] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('upload'), 'exclude': lambda f: f is None }})
    r"""Parameters for the upload task"""
    


class TaskPhase(str, Enum):
    r"""Phase of the task"""
    PENDING = 'pending'
    WAITING = 'waiting'
    RUNNING = 'running'
    FAILED = 'failed'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TaskStatus:
    r"""Status of the task"""
    phase: TaskPhase = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phase') }})
    r"""Phase of the task"""
    updated_at: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt') }})
    r"""Timestamp (in milliseconds) at which task was updated"""
    error_message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errorMessage'), 'exclude': lambda f: f is None }})
    r"""Error message if the task failed"""
    progress: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('progress'), 'exclude': lambda f: f is None }})
    r"""Current progress of the task in a 0-1 ratio"""
    retries: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('retries'), 'exclude': lambda f: f is None }})
    r"""Number of retries done on the task"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TaskUpload:
    r"""Output of the upload task"""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    asset_spec: Optional[Asset] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('assetSpec'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TaskIpfs:
    video_file_cid: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('videoFileCid') }})
    r"""IPFS CID of the exported video file"""
    nft_metadata_cid: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nftMetadataCid'), 'exclude': lambda f: f is None }})
    r"""IPFS CID of the default metadata exported for the video"""
    nft_metadata_gateway_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nftMetadataGatewayUrl'), 'exclude': lambda f: f is None }})
    r"""URL to access metadata file via HTTP through an IPFS
    gateway
    """
    nft_metadata_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nftMetadataUrl'), 'exclude': lambda f: f is None }})
    r"""URL for the metadata file with the IPFS protocol"""
    video_file_gateway_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('videoFileGatewayUrl'), 'exclude': lambda f: f is None }})
    r"""URL to access file via HTTP through an IPFS gateway"""
    video_file_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('videoFileUrl'), 'exclude': lambda f: f is None }})
    r"""URL for the file with the IPFS protocol"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Export:
    r"""Output of the export task"""
    ipfs: Optional[TaskIpfs] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ipfs'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TaskSchemasIpfs:
    cid: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cid') }})
    r"""IPFS CID of the exported data"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TaskExportData:
    r"""Output of the export data task"""
    ipfs: Optional[TaskSchemasIpfs] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ipfs'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Output:
    r"""Output of the task"""
    export: Optional[Export] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('export'), 'exclude': lambda f: f is None }})
    r"""Output of the export task"""
    export_data: Optional[TaskExportData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('exportData'), 'exclude': lambda f: f is None }})
    r"""Output of the export data task"""
    upload: Optional[TaskUpload] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('upload'), 'exclude': lambda f: f is None }})
    r"""Output of the upload task"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Task:
    created_at: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt'), 'exclude': lambda f: f is None }})
    r"""Timestamp (in milliseconds) at which task was created"""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Task ID"""
    input_asset_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('inputAssetId'), 'exclude': lambda f: f is None }})
    r"""ID of the input asset"""
    output: Optional[Output] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('output'), 'exclude': lambda f: f is None }})
    r"""Output of the task"""
    output_asset_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('outputAssetId'), 'exclude': lambda f: f is None }})
    r"""ID of the output asset"""
    params: Optional[Params] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('params'), 'exclude': lambda f: f is None }})
    r"""Parameters of the task"""
    requester_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('requesterId'), 'exclude': lambda f: f is None }})
    r"""ID of the requester hash(IP + SALT + PlaybackId)"""
    scheduled_at: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scheduledAt'), 'exclude': lambda f: f is None }})
    r"""Timestamp (in milliseconds) at which the task was scheduled for
    execution (e.g. after file upload finished).
    """
    status: Optional[TaskStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""Status of the task"""
    type: Optional[TaskType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    r"""Type of the task"""
    

