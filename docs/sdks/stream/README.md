# Stream
(*stream*)

### Available Operations

* [get_all](#get_all) - Retrieve streams
* [create](#create) - Create a stream
* [delete](#delete) - Delete a stream
* [get](#get) - Retrieve a stream
* [update](#update) - Update a stream
* [terminate](#terminate) - Terminates a live stream
* [create_clip](#create_clip) - Create a clip
* [get_all_clips](#get_all_clips) - Retrieve clips of a livestream
* [create_multistream_target](#create_multistream_target) - Add a multistream target
* [delete_multistream_target](#delete_multistream_target) - Remove a multistream target

## get_all

Retrieve streams

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    api_key="",
)


res = s.stream.get_all(streamsonly='string')

if res.classes is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `streamsonly`      | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetStreamsResponse](../../models/operations/getstreamsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

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
import sdk
from sdk.models import components

s = sdk.SDK(
    api_key="",
)

req = components.NewStreamPayload(
    name='test_stream',
    components.CreatorID1(
        type=components.CreatorIDType.UNVERIFIED,
        value='string',
    ),
    playback_policy=components.PlaybackPolicy(
        type=components.Type.JWT,
        webhook_context={
            "key": 'string',
        },
    ),
    profiles=[
        components.FfmpegProfile(
            width=638424,
            name='720p',
            height=859213,
            bitrate=417458,
            fps=288408,
        ),
    ],
    record=False,
    multistream=components.Multistream(
        targets=[
            components.Target(
                profile='720p',
                spec=components.TargetSpec(
                    url='rtmps://live.my-service.tv/channel/secretKey',
                ),
            ),
        ],
    ),
)

res = s.stream.create(req)

if res.classes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [components.NewStreamPayload](../../models/components/newstreampayload.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.CreateStreamResponse](../../models/operations/createstreamresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## delete


This will also suspend any active stream sessions, so make sure to wait
until the stream has finished. To explicitly interrupt an active
session, consider instead updating the suspended field in the stream
using the PATCH stream API.


### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    api_key="",
)


res = s.stream.delete(id='string')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | ID of the stream   |


### Response

**[operations.DeleteStreamResponse](../../models/operations/deletestreamresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get

Retrieve a stream

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    api_key="",
)


res = s.stream.get(id='string')

if res.stream is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | ID of the stream   |


### Response

**[operations.GetStreamResponse](../../models/operations/getstreamresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## update

Update a stream

### Example Usage

```python
import sdk
from sdk.models import components, operations

s = sdk.SDK(
    api_key="",
)


res = s.stream.update(id='string', stream_patch_payload=components.StreamPatchPayload(
'string',
    record=False,
    multistream=components.Multistream(
        targets=[
            components.Target(
                profile='720p',
                spec=components.TargetSpec(
                    url='rtmps://live.my-service.tv/channel/secretKey',
                ),
            ),
        ],
    ),
    playback_policy=components.PlaybackPolicy(
        type=components.Type.PUBLIC,
        webhook_context={
            "key": 'string',
        },
    ),
    profiles=[
        components.FfmpegProfile(
            width=597129,
            name='720p',
            height=15652,
            bitrate=344620,
            fps=708455,
        ),
    ],
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `id`                                                                           | *str*                                                                          | :heavy_check_mark:                                                             | ID of the stream                                                               |
| `stream_patch_payload`                                                         | [components.StreamPatchPayload](../../models/components/streampatchpayload.md) | :heavy_check_mark:                                                             | N/A                                                                            |


### Response

**[operations.UpdateStreamResponse](../../models/operations/updatestreamresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

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
import sdk
from sdk.models import operations

s = sdk.SDK(
    api_key="",
)


res = s.stream.terminate(id='string')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | ID of the stream   |


### Response

**[operations.TerminateStreamResponse](../../models/operations/terminatestreamresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## create_clip

Create a clip

### Example Usage

```python
import sdk
from sdk.models import components

s = sdk.SDK(
    api_key="",
)

req = components.ClipPayload(
    playback_id='string',
    start_time=9418.72,
)

res = s.stream.create_clip(req)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                        | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `request`                                                        | [components.ClipPayload](../../models/components/clippayload.md) | :heavy_check_mark:                                               | The request object to use for the request.                       |


### Response

**[operations.PostClipResponse](../../models/operations/postclipresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_all_clips

Retrieve clips of a livestream

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    api_key="",
)


res = s.stream.get_all_clips(id='string')

if res.classes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                              | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `id`                                                   | *str*                                                  | :heavy_check_mark:                                     | ID of the parent stream or playbackId of parent stream |


### Response

**[operations.GetStreamIDClipsResponse](../../models/operations/getstreamidclipsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## create_multistream_target

Add a multistream target

### Example Usage

```python
import sdk
from sdk.models import components, operations

s = sdk.SDK(
    api_key="",
)


res = s.stream.create_multistream_target(id='string', target_add_payload=components.TargetAddPayload(
    profile='720p',
    spec=components.TargetAddPayloadSpec(
        url='rtmps://live.my-service.tv/channel/secretKey',
    ),
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `id`                                                                       | *str*                                                                      | :heavy_check_mark:                                                         | ID of the parent stream                                                    |
| `target_add_payload`                                                       | [components.TargetAddPayload](../../models/components/targetaddpayload.md) | :heavy_check_mark:                                                         | N/A                                                                        |


### Response

**[operations.AddMultistreamTargetResponse](../../models/operations/addmultistreamtargetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## delete_multistream_target

Remove a multistream target

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    api_key="",
)


res = s.stream.delete_multistream_target(id='string', target_id='string')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                    | Type                         | Required                     | Description                  |
| ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- |
| `id`                         | *str*                        | :heavy_check_mark:           | ID of the parent stream      |
| `target_id`                  | *str*                        | :heavy_check_mark:           | ID of the multistream target |


### Response

**[operations.RemoveMultistreamTargetResponse](../../models/operations/removemultistreamtargetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
