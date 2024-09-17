"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from livepeer.types import BaseModel
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class ViewershipMetricTypedDict(TypedDict):
    r"""An individual metric about viewership of a stream/asset. Necessarily, at least
    1 of playbackId and dStorageUrl will be present, depending on the query.

    """

    view_count: int
    r"""The number of views for the stream/asset."""
    playtime_mins: float
    r"""The total playtime in minutes for the stream/asset."""
    playback_id: NotRequired[str]
    r"""The playback ID associated with the metric."""
    creator_id: NotRequired[str]
    r"""The ID of the creator associated with the metric."""
    viewer_id: NotRequired[str]
    r"""The ID of the viewer associated with the metric."""
    d_storage_url: NotRequired[str]
    r"""The URL of the distributed storage used for the asset"""
    timestamp: NotRequired[float]
    r"""Timestamp (in milliseconds) when the metric was recorded. If the
    query contains a time step, this timestamp will point to the
    beginning of the time step period.

    """
    device: NotRequired[str]
    r"""The device used by the viewer."""
    device_type: NotRequired[str]
    r"""The type of the device used by the viewer."""
    cpu: NotRequired[str]
    r"""The CPU used by the viewer's device."""
    os: NotRequired[str]
    r"""The operating system used by the viewer."""
    browser: NotRequired[str]
    r"""The browser used by the viewer."""
    browser_engine: NotRequired[str]
    r"""The browser engine used by the viewer's browser."""
    continent: NotRequired[str]
    r"""The continent where the viewer is located."""
    country: NotRequired[str]
    r"""The country where the viewer is located."""
    subdivision: NotRequired[str]
    r"""The subdivision (e.g., state or province) where the viewer is
    located.

    """
    timezone: NotRequired[str]
    r"""The timezone where the viewer is located."""
    geohash: NotRequired[str]
    r"""Geographic encoding of the viewers location. Accurate to 3 digits."""
    ttff_ms: NotRequired[float]
    r"""The time-to-first-frame (TTFF) in milliseconds."""
    rebuffer_ratio: NotRequired[float]
    r"""The rebuffering ratio for the asset."""
    error_rate: NotRequired[float]
    r"""The error rate for the stream/asset."""
    exits_before_start: NotRequired[float]
    r"""The percentage of sessions that existed before the asset started
    playing.

    """


class ViewershipMetric(BaseModel):
    r"""An individual metric about viewership of a stream/asset. Necessarily, at least
    1 of playbackId and dStorageUrl will be present, depending on the query.

    """

    view_count: Annotated[int, pydantic.Field(alias="viewCount")]
    r"""The number of views for the stream/asset."""

    playtime_mins: Annotated[float, pydantic.Field(alias="playtimeMins")]
    r"""The total playtime in minutes for the stream/asset."""

    playback_id: Annotated[Optional[str], pydantic.Field(alias="playbackId")] = None
    r"""The playback ID associated with the metric."""

    creator_id: Annotated[Optional[str], pydantic.Field(alias="creatorId")] = None
    r"""The ID of the creator associated with the metric."""

    viewer_id: Annotated[Optional[str], pydantic.Field(alias="viewerId")] = None
    r"""The ID of the viewer associated with the metric."""

    d_storage_url: Annotated[Optional[str], pydantic.Field(alias="dStorageUrl")] = None
    r"""The URL of the distributed storage used for the asset"""

    timestamp: Optional[float] = None
    r"""Timestamp (in milliseconds) when the metric was recorded. If the
    query contains a time step, this timestamp will point to the
    beginning of the time step period.

    """

    device: Optional[str] = None
    r"""The device used by the viewer."""

    device_type: Annotated[Optional[str], pydantic.Field(alias="deviceType")] = None
    r"""The type of the device used by the viewer."""

    cpu: Optional[str] = None
    r"""The CPU used by the viewer's device."""

    os: Optional[str] = None
    r"""The operating system used by the viewer."""

    browser: Optional[str] = None
    r"""The browser used by the viewer."""

    browser_engine: Annotated[Optional[str], pydantic.Field(alias="browserEngine")] = (
        None
    )
    r"""The browser engine used by the viewer's browser."""

    continent: Optional[str] = None
    r"""The continent where the viewer is located."""

    country: Optional[str] = None
    r"""The country where the viewer is located."""

    subdivision: Optional[str] = None
    r"""The subdivision (e.g., state or province) where the viewer is
    located.

    """

    timezone: Optional[str] = None
    r"""The timezone where the viewer is located."""

    geohash: Optional[str] = None
    r"""Geographic encoding of the viewers location. Accurate to 3 digits."""

    ttff_ms: Annotated[Optional[float], pydantic.Field(alias="ttffMs")] = None
    r"""The time-to-first-frame (TTFF) in milliseconds."""

    rebuffer_ratio: Annotated[
        Optional[float], pydantic.Field(alias="rebufferRatio")
    ] = None
    r"""The rebuffering ratio for the asset."""

    error_rate: Annotated[Optional[float], pydantic.Field(alias="errorRate")] = None
    r"""The error rate for the stream/asset."""

    exits_before_start: Annotated[
        Optional[float], pydantic.Field(alias="exitsBeforeStart")
    ] = None
    r"""The percentage of sessions that existed before the asset started
    playing.

    """
