# Stream
(*stream*)

## Overview

Operations related to livestream api

### Available Operations

* [create](#create) - Create a stream
* [get_all](#get_all) - Retrieve streams
* [get](#get) - Retrieve a stream
* [update](#update) - Update a stream
* [delete](#delete) - Delete a stream
* [terminate](#terminate) - Terminates a live stream
* [start_pull](#start_pull) - Start ingest for a pull stream
* [create_clip](#create_clip) - Create a clip
* [get_clips](#get_clips) - Retrieve clips of a livestream
* [add_multistream_target](#add_multistream_target) - Add a multistream target
* [remove_multistream_target](#remove_multistream_target) - Remove a multistream target

## create

The only parameter you are required to set is the name of your stream,
but we also highly recommend that you define transcoding profiles
parameter that suits your specific broadcasting configuration.
\
\
If you do not define transcoding rendition profiles when creating the
stream, a default set of profiles will be used. These profiles include
240p,  360p, 480p and 720p.
\
\
The playback policy is set to public by default for new streams. It can
also be added upon the creation of a new stream by adding
`"playbackPolicy": {"type": "jwt"}`


### Example Usage

```python
from livepeer import Livepeer
from livepeer.models import components

s = Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.stream.create(request={
    "name": "test_stream",
    "pull": {
        "source": "https://myservice.com/live/stream.flv",
        "headers": {
            "Authorization": "Bearer 123",
        },
        "location": {
            "lat": 39.739,
            "lon": -104.988,
        },
    },
    "playback_policy": {
        "type": components.Type.WEBHOOK,
        "webhook_id": "1bde4o2i6xycudoy",
        "webhook_context": {
            "streamerId": "my-custom-id",
        },
        "refresh_interval": 600,
    },
    "profiles": [
        {
            "width": 1280,
            "name": "720p",
            "height": 720,
            "bitrate": 3000000,
            "fps": 30,
            "fps_den": 1,
            "quality": 23,
            "gop": "2",
            "profile": components.Profile.H264_BASELINE,
        },
    ],
    "record": False,
    "recording_spec": {
        "profiles": [
            {
                "bitrate": 3000000,
                "width": 1280,
                "name": "720p",
                "height": 720,
                "quality": 23,
                "fps": 30,
                "fps_den": 1,
                "gop": "2",
                "profile": components.TranscodeProfileProfile.H264_BASELINE,
                "encoder": components.TranscodeProfileEncoder.H_264,
            },
        ],
    },
    "multistream": {
        "targets": [
            {
                "profile": "720p",
                "video_only": False,
                "id": "PUSH123",
                "spec": {
                    "url": "rtmps://live.my-service.tv/channel/secretKey",
                    "name": "My target",
                },
            },
        ],
    },
})

if res.stream is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [components.NewStreamPayload](../../models/components/newstreampayload.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[operations.CreateStreamResponse](../../models/operations/createstreamresponse.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |


## get_all

Retrieve streams

### Example Usage

```python
from livepeer import Livepeer

s = Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.stream.get_all()

if res.data is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `streamsonly`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetStreamsResponse](../../models/operations/getstreamsresponse.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |


## get

Retrieve a stream

### Example Usage

```python
from livepeer import Livepeer

s = Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.stream.get(id="<id>")

if res.stream is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | ID of the stream                                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetStreamResponse](../../models/operations/getstreamresponse.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |


## update

Update a stream

### Example Usage

```python
from livepeer import Livepeer
from livepeer.models import components

s = Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.stream.update(id="<id>", stream_patch_payload={
    "record": False,
    "multistream": {
        "targets": [
            {
                "profile": "720p",
                "video_only": False,
                "id": "PUSH123",
                "spec": {
                    "url": "rtmps://live.my-service.tv/channel/secretKey",
                    "name": "My target",
                },
            },
        ],
    },
    "playback_policy": {
        "type": components.Type.WEBHOOK,
        "webhook_id": "1bde4o2i6xycudoy",
        "webhook_context": {
            "streamerId": "my-custom-id",
        },
        "refresh_interval": 600,
    },
    "profiles": [
        {
            "width": 1280,
            "name": "720p",
            "height": 720,
            "bitrate": 3000000,
            "fps": 30,
            "fps_den": 1,
            "quality": 23,
            "gop": "2",
            "profile": components.Profile.H264_BASELINE,
        },
    ],
    "recording_spec": {
        "profiles": [
            {
                "bitrate": 3000000,
                "width": 1280,
                "name": "720p",
                "height": 720,
                "quality": 23,
                "fps": 30,
                "fps_den": 1,
                "gop": "2",
                "profile": components.TranscodeProfileProfile.H264_BASELINE,
                "encoder": components.TranscodeProfileEncoder.H_264,
            },
        ],
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `id`                                                                           | *str*                                                                          | :heavy_check_mark:                                                             | ID of the stream                                                               |
| `stream_patch_payload`                                                         | [components.StreamPatchPayload](../../models/components/streampatchpayload.md) | :heavy_check_mark:                                                             | N/A                                                                            |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.UpdateStreamResponse](../../models/operations/updatestreamresponse.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |


## delete

This will also suspend any active stream sessions, so make sure to wait
until the stream has finished. To explicitly interrupt an active
session, consider instead updating the suspended field in the stream
using the PATCH stream API.


### Example Usage

```python
from livepeer import Livepeer

s = Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.stream.delete(id="<id>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | ID of the stream                                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.DeleteStreamResponse](../../models/operations/deletestreamresponse.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |


## terminate

`DELETE /stream/{id}/terminate` can be used to terminate an ongoing
session on a live stream. Unlike suspending the stream, it allows the
streamer to restart streaming even immediately, but it will force
terminate the current session and stop the recording.
\
\
A 204 No Content status response indicates the stream was successfully
terminated.


### Example Usage

```python
from livepeer import Livepeer

s = Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.stream.terminate(id="<id>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | ID of the stream                                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.TerminateStreamResponse](../../models/operations/terminatestreamresponse.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |


## start_pull

`POST /stream/{id}/start-pull` can be used to start ingest for a stream
configured with a pull source. If the stream has recording configured,
it will also start recording.
\
\
A 204 No Content status response indicates the stream was successfully
started.


### Example Usage

```python
from livepeer import Livepeer

s = Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.stream.start_pull(id="<id>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | ID of the stream                                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.StartPullStreamResponse](../../models/operations/startpullstreamresponse.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |


## create_clip

Create a clip

### Example Usage

```python
from livepeer import Livepeer

s = Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.stream.create_clip(request={
    "playback_id": "eaw4nk06ts2d0mzb",
    "start_time": 1587667174725,
    "end_time": 1587667174725,
    "name": "My Clip",
    "session_id": "de7818e7-610a-4057-8f6f-b785dc1e6f88",
})

if res.data is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [components.ClipPayload](../../models/components/clippayload.md)    | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.CreateClipResponse](../../models/operations/createclipresponse.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |


## get_clips

Retrieve clips of a livestream

### Example Usage

```python
from livepeer import Livepeer

s = Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.stream.get_clips(id="<id>")

if res.data is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | ID of the parent stream or playbackId of parent stream              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetClipsResponse](../../models/operations/getclipsresponse.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |


## add_multistream_target

Add a multistream target

### Example Usage

```python
from livepeer import Livepeer

s = Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.stream.add_multistream_target(id="<id>", target_add_payload={
    "profile": "720p0",
    "video_only": False,
    "id": "PUSH123",
    "spec": {
        "url": "rtmps://live.my-service.tv/channel/secretKey",
        "name": "My target",
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `id`                                                                       | *str*                                                                      | :heavy_check_mark:                                                         | ID of the parent stream                                                    |
| `target_add_payload`                                                       | [components.TargetAddPayload](../../models/components/targetaddpayload.md) | :heavy_check_mark:                                                         | N/A                                                                        |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[operations.AddMultistreamTargetResponse](../../models/operations/addmultistreamtargetresponse.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |


## remove_multistream_target

Remove a multistream target

### Example Usage

```python
from livepeer import Livepeer

s = Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.stream.remove_multistream_target(id="<id>", target_id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | ID of the parent stream                                             |
| `target_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | ID of the multistream target                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.RemoveMultistreamTargetResponse](../../models/operations/removemultistreamtargetresponse.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
