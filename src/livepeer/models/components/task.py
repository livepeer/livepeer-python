"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .asset import Asset, AssetTypedDict
from .encryption_output import EncryptionOutput, EncryptionOutputTypedDict
from .export_task_params import ExportTaskParams, ExportTaskParamsTypedDict
from .input_creator_id import InputCreatorID, InputCreatorIDTypedDict
from .ipfs_export_params import IpfsExportParams, IpfsExportParamsTypedDict
from .transcode_profile import TranscodeProfile, TranscodeProfileTypedDict
from enum import Enum
from livepeer.types import BaseModel
import pydantic
from pydantic import ConfigDict
from typing import Any, Dict, List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class TaskType(str, Enum):
    r"""Type of the task"""

    UPLOAD = "upload"
    EXPORT = "export"
    EXPORT_DATA = "export-data"
    TRANSCODE_FILE = "transcode-file"
    CLIP = "clip"


class UploadTypedDict(TypedDict):
    r"""Parameters for the upload task"""

    url: NotRequired[str]
    r"""URL of the asset to \"upload\" """
    encryption: NotRequired[EncryptionOutputTypedDict]
    c2pa: NotRequired[bool]
    r"""Decides if the output video should include C2PA signature"""
    profiles: NotRequired[List[TranscodeProfileTypedDict]]
    target_segment_size_secs: NotRequired[float]
    r"""How many seconds the duration of each output segment should be"""


class Upload(BaseModel):
    r"""Parameters for the upload task"""

    url: Optional[str] = None
    r"""URL of the asset to \"upload\" """

    encryption: Optional[EncryptionOutput] = None

    c2pa: Optional[bool] = None
    r"""Decides if the output video should include C2PA signature"""

    profiles: Optional[List[TranscodeProfile]] = None

    target_segment_size_secs: Annotated[
        Optional[float], pydantic.Field(alias="targetSegmentSizeSecs")
    ] = None
    r"""How many seconds the duration of each output segment should be"""


class ContentTypedDict(TypedDict):
    r"""File content to store into IPFS"""


class Content(BaseModel):
    r"""File content to store into IPFS"""


class TaskExportDataTypedDict(TypedDict):
    r"""Parameters for the export-data task"""

    content: ContentTypedDict
    r"""File content to store into IPFS"""
    ipfs: NotRequired[IpfsExportParamsTypedDict]
    type: NotRequired[str]
    r"""Optional type of content"""
    id: NotRequired[str]
    r"""Optional ID of the content"""


class TaskExportData(BaseModel):
    r"""Parameters for the export-data task"""

    content: Content
    r"""File content to store into IPFS"""

    ipfs: Optional[IpfsExportParams] = None

    type: Optional[str] = None
    r"""Optional type of content"""

    id: Optional[str] = None
    r"""Optional ID of the content"""


class TaskInputTypedDict(TypedDict):
    r"""Input video file to transcode"""

    url: NotRequired[str]
    r"""URL of a video to transcode, accepts object-store format
    \"s3+https\" 

    """


class TaskInput(BaseModel):
    r"""Input video file to transcode"""

    url: Optional[str] = None
    r"""URL of a video to transcode, accepts object-store format
    \"s3+https\" 

    """


class TaskStorageTypedDict(TypedDict):
    r"""Storage for the output files"""

    url: NotRequired[str]
    r"""URL of the output storage, accepts object-store format
    \"s3+https\" 

    """


class TaskStorage(BaseModel):
    r"""Storage for the output files"""

    url: Optional[str] = None
    r"""URL of the output storage, accepts object-store format
    \"s3+https\" 

    """


class TaskHlsTypedDict(TypedDict):
    r"""HLS output format"""

    path: NotRequired[str]
    r"""Path for the HLS output"""


class TaskHls(BaseModel):
    r"""HLS output format"""

    path: Optional[str] = None
    r"""Path for the HLS output"""


class TaskMp4TypedDict(TypedDict):
    r"""MP4 output format"""

    path: NotRequired[str]
    r"""Path for the MP4 output"""


class TaskMp4(BaseModel):
    r"""MP4 output format"""

    path: Optional[str] = None
    r"""Path for the MP4 output"""


class TaskOutputsTypedDict(TypedDict):
    r"""Output formats"""

    hls: NotRequired[TaskHlsTypedDict]
    r"""HLS output format"""
    mp4: NotRequired[TaskMp4TypedDict]
    r"""MP4 output format"""


class TaskOutputs(BaseModel):
    r"""Output formats"""

    hls: Optional[TaskHls] = None
    r"""HLS output format"""

    mp4: Optional[TaskMp4] = None
    r"""MP4 output format"""


class TranscodeFileTypedDict(TypedDict):
    r"""Parameters for the transcode-file task"""

    input: NotRequired[TaskInputTypedDict]
    r"""Input video file to transcode"""
    storage: NotRequired[TaskStorageTypedDict]
    r"""Storage for the output files"""
    outputs: NotRequired[TaskOutputsTypedDict]
    r"""Output formats"""
    profiles: NotRequired[List[TranscodeProfileTypedDict]]
    target_segment_size_secs: NotRequired[float]
    r"""How many seconds the duration of each output segment should
    be

    """
    creator_id: NotRequired[InputCreatorIDTypedDict]
    c2pa: NotRequired[bool]
    r"""Decides if the output video should include C2PA signature"""


class TranscodeFile(BaseModel):
    r"""Parameters for the transcode-file task"""

    input: Optional[TaskInput] = None
    r"""Input video file to transcode"""

    storage: Optional[TaskStorage] = None
    r"""Storage for the output files"""

    outputs: Optional[TaskOutputs] = None
    r"""Output formats"""

    profiles: Optional[List[TranscodeProfile]] = None

    target_segment_size_secs: Annotated[
        Optional[float], pydantic.Field(alias="targetSegmentSizeSecs")
    ] = None
    r"""How many seconds the duration of each output segment should
    be

    """

    creator_id: Annotated[
        Optional[InputCreatorID], pydantic.Field(alias="creatorId")
    ] = None

    c2pa: Optional[bool] = None
    r"""Decides if the output video should include C2PA signature"""


class ClipStrategyTypedDict(TypedDict):
    r"""Strategy to use for clipping the asset. If not specified, the default strategy that Catalyst is configured for will be used. This field only available for admin users, and is only used for E2E testing."""

    start_time: NotRequired[float]
    r"""The start timestamp of the clip in Unix milliseconds. _See the ClipTrigger in the UI Kit for an example of how this is calculated (for HLS, it uses `Program Date-Time` tags, and for WebRTC, it uses the latency from server to client at stream startup)._"""
    end_time: NotRequired[float]
    r"""The end timestamp of the clip in Unix milliseconds. _See the ClipTrigger in the UI Kit for an example of how this is calculated (for HLS, it uses `Program Date-Time` tags, and for WebRTC, it uses the latency from server to client at stream startup)._"""
    playback_id: NotRequired[str]
    r"""The playback ID of the stream or stream recording to clip. Asset playback IDs are not supported yet."""


class ClipStrategy(BaseModel):
    r"""Strategy to use for clipping the asset. If not specified, the default strategy that Catalyst is configured for will be used. This field only available for admin users, and is only used for E2E testing."""

    start_time: Annotated[Optional[float], pydantic.Field(alias="startTime")] = None
    r"""The start timestamp of the clip in Unix milliseconds. _See the ClipTrigger in the UI Kit for an example of how this is calculated (for HLS, it uses `Program Date-Time` tags, and for WebRTC, it uses the latency from server to client at stream startup)._"""

    end_time: Annotated[Optional[float], pydantic.Field(alias="endTime")] = None
    r"""The end timestamp of the clip in Unix milliseconds. _See the ClipTrigger in the UI Kit for an example of how this is calculated (for HLS, it uses `Program Date-Time` tags, and for WebRTC, it uses the latency from server to client at stream startup)._"""

    playback_id: Annotated[Optional[str], pydantic.Field(alias="playbackId")] = None
    r"""The playback ID of the stream or stream recording to clip. Asset playback IDs are not supported yet."""


class CatalystPipelineStrategy(str, Enum):
    r"""Force to use a specific strategy in the Catalyst pipeline. If not specified, the default strategy that Catalyst is configured for will be used. This field only available for admin users, and is only used for E2E testing."""

    CATALYST = "catalyst"
    CATALYST_FFMPEG = "catalyst_ffmpeg"
    BACKGROUND_EXTERNAL = "background_external"
    BACKGROUND_MIST = "background_mist"
    FALLBACK_EXTERNAL = "fallback_external"
    EXTERNAL = "external"


class ClipTypedDict(TypedDict):
    url: NotRequired[str]
    r"""URL of the asset to \"clip\" """
    clip_strategy: NotRequired[ClipStrategyTypedDict]
    r"""Strategy to use for clipping the asset. If not specified, the default strategy that Catalyst is configured for will be used. This field only available for admin users, and is only used for E2E testing."""
    catalyst_pipeline_strategy: NotRequired[CatalystPipelineStrategy]
    r"""Force to use a specific strategy in the Catalyst pipeline. If not specified, the default strategy that Catalyst is configured for will be used. This field only available for admin users, and is only used for E2E testing."""
    session_id: NotRequired[str]
    r"""ID of the session"""
    input_id: NotRequired[str]
    r"""ID of the input asset or stream"""


class Clip(BaseModel):
    url: Optional[str] = None
    r"""URL of the asset to \"clip\" """

    clip_strategy: Annotated[
        Optional[ClipStrategy], pydantic.Field(alias="clipStrategy")
    ] = None
    r"""Strategy to use for clipping the asset. If not specified, the default strategy that Catalyst is configured for will be used. This field only available for admin users, and is only used for E2E testing."""

    catalyst_pipeline_strategy: Annotated[
        Optional[CatalystPipelineStrategy],
        pydantic.Field(alias="catalystPipelineStrategy"),
    ] = None
    r"""Force to use a specific strategy in the Catalyst pipeline. If not specified, the default strategy that Catalyst is configured for will be used. This field only available for admin users, and is only used for E2E testing."""

    session_id: Annotated[Optional[str], pydantic.Field(alias="sessionId")] = None
    r"""ID of the session"""

    input_id: Annotated[Optional[str], pydantic.Field(alias="inputId")] = None
    r"""ID of the input asset or stream"""


class ParamsTypedDict(TypedDict):
    r"""Parameters of the task"""

    upload: NotRequired[UploadTypedDict]
    r"""Parameters for the upload task"""
    export: NotRequired[ExportTaskParamsTypedDict]
    r"""Parameters for the export task"""
    export_data: NotRequired[TaskExportDataTypedDict]
    r"""Parameters for the export-data task"""
    transcode_file: NotRequired[TranscodeFileTypedDict]
    r"""Parameters for the transcode-file task"""
    clip: NotRequired[ClipTypedDict]


class Params(BaseModel):
    r"""Parameters of the task"""

    upload: Optional[Upload] = None
    r"""Parameters for the upload task"""

    export: Optional[ExportTaskParams] = None
    r"""Parameters for the export task"""

    export_data: Annotated[
        Optional[TaskExportData], pydantic.Field(alias="exportData")
    ] = None
    r"""Parameters for the export-data task"""

    transcode_file: Annotated[
        Optional[TranscodeFile], pydantic.Field(alias="transcode-file")
    ] = None
    r"""Parameters for the transcode-file task"""

    clip: Optional[Clip] = None


class TaskPhase(str, Enum):
    r"""Phase of the task"""

    PENDING = "pending"
    WAITING = "waiting"
    RUNNING = "running"
    FAILED = "failed"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class TaskStatusTypedDict(TypedDict):
    r"""Status of the task"""

    phase: TaskPhase
    r"""Phase of the task"""
    updated_at: float
    r"""Timestamp (in milliseconds) at which task was updated"""
    progress: NotRequired[float]
    r"""Current progress of the task in a 0-1 ratio"""
    error_message: NotRequired[str]
    r"""Error message if the task failed"""
    retries: NotRequired[float]
    r"""Number of retries done on the task"""


class TaskStatus(BaseModel):
    r"""Status of the task"""

    phase: TaskPhase
    r"""Phase of the task"""

    updated_at: Annotated[float, pydantic.Field(alias="updatedAt")]
    r"""Timestamp (in milliseconds) at which task was updated"""

    progress: Optional[float] = None
    r"""Current progress of the task in a 0-1 ratio"""

    error_message: Annotated[Optional[str], pydantic.Field(alias="errorMessage")] = None
    r"""Error message if the task failed"""

    retries: Optional[float] = None
    r"""Number of retries done on the task"""


class TaskUploadTypedDict(TypedDict):
    r"""Output of the upload task"""

    asset_spec: NotRequired[AssetTypedDict]


class TaskUpload(BaseModel):
    r"""Output of the upload task"""

    model_config = ConfigDict(
        populate_by_name=True, arbitrary_types_allowed=True, extra="allow"
    )
    __pydantic_extra__: Dict[str, Any] = pydantic.Field(init=False)

    asset_spec: Annotated[Optional[Asset], pydantic.Field(alias="assetSpec")] = None

    @property
    def additional_properties(self):
        return self.__pydantic_extra__

    @additional_properties.setter
    def additional_properties(self, value):
        self.__pydantic_extra__ = value  # pyright: ignore[reportIncompatibleVariableOverride]


class TaskIpfsTypedDict(TypedDict):
    video_file_cid: str
    r"""IPFS CID of the exported video file"""
    video_file_url: NotRequired[str]
    r"""URL for the file with the IPFS protocol"""
    video_file_gateway_url: NotRequired[str]
    r"""URL to access file via HTTP through an IPFS gateway"""
    nft_metadata_cid: NotRequired[str]
    r"""IPFS CID of the default metadata exported for the video"""
    nft_metadata_url: NotRequired[str]
    r"""URL for the metadata file with the IPFS protocol"""
    nft_metadata_gateway_url: NotRequired[str]
    r"""URL to access metadata file via HTTP through an IPFS
    gateway

    """


class TaskIpfs(BaseModel):
    video_file_cid: Annotated[str, pydantic.Field(alias="videoFileCid")]
    r"""IPFS CID of the exported video file"""

    video_file_url: Annotated[Optional[str], pydantic.Field(alias="videoFileUrl")] = (
        None
    )
    r"""URL for the file with the IPFS protocol"""

    video_file_gateway_url: Annotated[
        Optional[str], pydantic.Field(alias="videoFileGatewayUrl")
    ] = None
    r"""URL to access file via HTTP through an IPFS gateway"""

    nft_metadata_cid: Annotated[
        Optional[str], pydantic.Field(alias="nftMetadataCid")
    ] = None
    r"""IPFS CID of the default metadata exported for the video"""

    nft_metadata_url: Annotated[
        Optional[str], pydantic.Field(alias="nftMetadataUrl")
    ] = None
    r"""URL for the metadata file with the IPFS protocol"""

    nft_metadata_gateway_url: Annotated[
        Optional[str], pydantic.Field(alias="nftMetadataGatewayUrl")
    ] = None
    r"""URL to access metadata file via HTTP through an IPFS
    gateway

    """


class ExportTypedDict(TypedDict):
    r"""Output of the export task"""

    ipfs: NotRequired[TaskIpfsTypedDict]


class Export(BaseModel):
    r"""Output of the export task"""

    ipfs: Optional[TaskIpfs] = None


class TaskOutputIpfsTypedDict(TypedDict):
    cid: str
    r"""IPFS CID of the exported data"""


class TaskOutputIpfs(BaseModel):
    cid: str
    r"""IPFS CID of the exported data"""


class ExportDataTypedDict(TypedDict):
    r"""Output of the export data task"""

    ipfs: NotRequired[TaskOutputIpfsTypedDict]


class ExportData(BaseModel):
    r"""Output of the export data task"""

    ipfs: Optional[TaskOutputIpfs] = None


class OutputTypedDict(TypedDict):
    r"""Output of the task"""

    upload: NotRequired[TaskUploadTypedDict]
    r"""Output of the upload task"""
    export: NotRequired[ExportTypedDict]
    r"""Output of the export task"""
    export_data: NotRequired[ExportDataTypedDict]
    r"""Output of the export data task"""


class Output(BaseModel):
    r"""Output of the task"""

    upload: Optional[TaskUpload] = None
    r"""Output of the upload task"""

    export: Optional[Export] = None
    r"""Output of the export task"""

    export_data: Annotated[Optional[ExportData], pydantic.Field(alias="exportData")] = (
        None
    )
    r"""Output of the export data task"""


class TaskTypedDict(TypedDict):
    id: NotRequired[str]
    r"""Task ID"""
    type: NotRequired[TaskType]
    r"""Type of the task"""
    created_at: NotRequired[float]
    r"""Timestamp (in milliseconds) at which task was created"""
    scheduled_at: NotRequired[float]
    r"""Timestamp (in milliseconds) at which the task was scheduled for
    execution (e.g. after file upload finished).

    """
    input_asset_id: NotRequired[str]
    r"""ID of the input asset"""
    output_asset_id: NotRequired[str]
    r"""ID of the output asset"""
    project_id: NotRequired[str]
    r"""ID of the project"""
    requester_id: NotRequired[str]
    r"""ID of the requester hash(IP + SALT + PlaybackId)"""
    params: NotRequired[ParamsTypedDict]
    r"""Parameters of the task"""
    status: NotRequired[TaskStatusTypedDict]
    r"""Status of the task"""
    output: NotRequired[OutputTypedDict]
    r"""Output of the task"""


class Task(BaseModel):
    id: Optional[str] = None
    r"""Task ID"""

    type: Optional[TaskType] = None
    r"""Type of the task"""

    created_at: Annotated[Optional[float], pydantic.Field(alias="createdAt")] = None
    r"""Timestamp (in milliseconds) at which task was created"""

    scheduled_at: Annotated[Optional[float], pydantic.Field(alias="scheduledAt")] = None
    r"""Timestamp (in milliseconds) at which the task was scheduled for
    execution (e.g. after file upload finished).

    """

    input_asset_id: Annotated[Optional[str], pydantic.Field(alias="inputAssetId")] = (
        None
    )
    r"""ID of the input asset"""

    output_asset_id: Annotated[Optional[str], pydantic.Field(alias="outputAssetId")] = (
        None
    )
    r"""ID of the output asset"""

    project_id: Annotated[Optional[str], pydantic.Field(alias="projectId")] = None
    r"""ID of the project"""

    requester_id: Annotated[Optional[str], pydantic.Field(alias="requesterId")] = None
    r"""ID of the requester hash(IP + SALT + PlaybackId)"""

    params: Optional[Params] = None
    r"""Parameters of the task"""

    status: Optional[TaskStatus] = None
    r"""Status of the task"""

    output: Optional[Output] = None
    r"""Output of the task"""
