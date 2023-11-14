# Stream
(*stream*)

### Available Operations

* [get_all](#get_all) - Retrieve streams
* [create](#create) - Create a stream
* [delete](#delete) - Delete a stream
* [get](#get) - Retrieve a stream
* [update](#update) - Update a stream
* [create_clip](#create_clip) - Create a clip
* [get_all_clips](#get_all_clips) - Retrieve clips of a livestream

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

if res.data is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `streamsonly`                                                                                      | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | Filter the API response and retrieve a specific subset of stream objects based on certain criteria |


### Response

**[operations.GetStreamsResponse](../../models/operations/getstreamsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## create

Create a stream

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
        webhook_id='3e02c844-d364-4d48-b401-24b2773b5d6c',
        webhook_context={
            "foo": 'string',
        },
    ),
    profiles=[
        components.FfmpegProfile(
            width=1280,
            name='720p',
            height=720,
            bitrate=4000,
            fps=30,
            fps_den=1,
            gop='60',
            profile=components.Profile.H264_HIGH,
            encoder=components.Encoder.H264,
        ),
    ],
    record=False,
    multistream=components.Multistream(
        targets=[
            components.Targets(
                profile='720p',
                spec=components.MultistreamSpec(
                    url='rtmps://live.my-service.tv/channel/secretKey',
                ),
            ),
        ],
    ),
)

res = s.stream.create(req)

if res.data is not None:
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

Delete a stream

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
            components.Targets(
                profile='720p',
                spec=components.MultistreamSpec(
                    url='rtmps://live.my-service.tv/channel/secretKey',
                ),
            ),
        ],
    ),
    playback_policy=components.PlaybackPolicy(
        type=components.Type.PUBLIC,
        webhook_id='3e02c844-d364-4d48-b401-24b2773b5d6c',
        webhook_context={
            "foo": 'string',
        },
    ),
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

## create_clip

Create a clip from a livestream


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

if res.data is not None:
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

if res.data is not None:
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
