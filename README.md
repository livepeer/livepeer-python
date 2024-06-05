# Livepeer Python Library

The Livepeer Python library provides convenient access to the Livepeer Studio API from
applications written in Python

## Documentation

For full documentation and examples, please visit [docs.livepeer.org](https://docs.livepeer.org/sdks/python/).

## SDK Installation

```bash
pip install git+https://github.com/livepeer/livepeer-python.git
```

## SDK Example Usage

### Example

```python
import livepeer
from livepeer.models import components

s = livepeer.Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)

req = components.NewStreamPayload(
    name='test_stream',
)

res = s.stream.create(req)

if res.stream is not None:
    # handle response
    pass

```

## Available Resources and Operations

### [stream](docs/sdks/stream/README.md)

- [create](docs/sdks/stream/README.md#create) - Create a stream
- [get_all](docs/sdks/stream/README.md#get_all) - Retrieve streams
- [get](docs/sdks/stream/README.md#get) - Retrieve a stream
- [update](docs/sdks/stream/README.md#update) - Update a stream
- [delete](docs/sdks/stream/README.md#delete) - Delete a stream
- [terminate](docs/sdks/stream/README.md#terminate) - Terminates a live stream
- [start_pull](docs/sdks/stream/README.md#start_pull) - Start ingest for a pull stream
- [create_clip](docs/sdks/stream/README.md#create_clip) - Create a clip
- [get_clips](docs/sdks/stream/README.md#get_clips) - Retrieve clips of a livestream
- [add_multistream_target](docs/sdks/stream/README.md#add_multistream_target) - Add a multistream target
- [remove_multistream_target](docs/sdks/stream/README.md#remove_multistream_target) - Remove a multistream target

### [multistream](docs/sdks/multistream/README.md)

- [get_all](docs/sdks/multistream/README.md#get_all) - Retrieve Multistream Targets
- [create](docs/sdks/multistream/README.md#create) - Create a multistream target
- [get](docs/sdks/multistream/README.md#get) - Retrieve a multistream target
- [update](docs/sdks/multistream/README.md#update) - Update Multistream Target
- [delete](docs/sdks/multistream/README.md#delete) - Delete a multistream target

### [webhook](docs/sdks/webhook/README.md)

- [get_all](docs/sdks/webhook/README.md#get_all) - Retrieve a Webhook
- [create](docs/sdks/webhook/README.md#create) - Create a webhook
- [get](docs/sdks/webhook/README.md#get) - Retrieve a webhook
- [update](docs/sdks/webhook/README.md#update) - Update a webhook
- [delete](docs/sdks/webhook/README.md#delete) - Delete a webhook
- [get_logs](docs/sdks/webhook/README.md#get_logs) - Retrieve webhook logs
- [get_log](docs/sdks/webhook/README.md#get_log) - Retrieve a webhook log
- [resend_log](docs/sdks/webhook/README.md#resend_log) - Resend a webhook

### [asset](docs/sdks/asset/README.md)

- [get_all](docs/sdks/asset/README.md#get_all) - Retrieve assets
- [create](docs/sdks/asset/README.md#create) - Upload an asset
- [create_via_url](docs/sdks/asset/README.md#create_via_url) - Upload asset via URL
- [get](docs/sdks/asset/README.md#get) - Retrieves an asset
- [update](docs/sdks/asset/README.md#update) - Patch an asset
- [delete](docs/sdks/asset/README.md#delete) - Delete an asset

### [session](docs/sdks/session/README.md)

- [get_clips](docs/sdks/session/README.md#get_clips) - Retrieve clips of a session
- [get_all](docs/sdks/session/README.md#get_all) - Retrieve sessions
- [get](docs/sdks/session/README.md#get) - Retrieve a session
- [get_recorded](docs/sdks/session/README.md#get_recorded) - Retrieve Recorded Sessions

### [room](docs/sdks/room/README.md)

- [~~create~~](docs/sdks/room/README.md#create) - Create a room :warning: **Deprecated**
- [~~get~~](docs/sdks/room/README.md#get) - Retrieve a room :warning: **Deprecated**
- [~~delete~~](docs/sdks/room/README.md#delete) - Delete a room :warning: **Deprecated**
- [~~start_egress~~](docs/sdks/room/README.md#start_egress) - Start room RTMP egress :warning: **Deprecated**
- [~~stop_egress~~](docs/sdks/room/README.md#stop_egress) - Stop room RTMP egress :warning: **Deprecated**
- [~~create_user~~](docs/sdks/room/README.md#create_user) - Create a room user :warning: **Deprecated**
- [~~get_user~~](docs/sdks/room/README.md#get_user) - Get user details :warning: **Deprecated**
- [~~update_user~~](docs/sdks/room/README.md#update_user) - Update a room user :warning: **Deprecated**
- [~~delete_user~~](docs/sdks/room/README.md#delete_user) - Remove a user from the room :warning: **Deprecated**

### [metrics](docs/sdks/metrics/README.md)

- [get_viewership](docs/sdks/metrics/README.md#get_viewership) - Query viewership metrics
- [get_creator_viewership](docs/sdks/metrics/README.md#get_creator_viewership) - Query creator viewership metrics
- [get_public_viewership](docs/sdks/metrics/README.md#get_public_viewership) - Query public total views metrics
- [get_usage](docs/sdks/metrics/README.md#get_usage) - Query usage metrics

### [access_control](docs/sdks/accesscontrol/README.md)

- [create](docs/sdks/accesscontrol/README.md#create) - Create a signing key
- [get_all](docs/sdks/accesscontrol/README.md#get_all) - Retrieves signing keys
- [delete](docs/sdks/accesscontrol/README.md#delete) - Delete Signing Key
- [get](docs/sdks/accesscontrol/README.md#get) - Retrieves a signing key
- [update](docs/sdks/accesscontrol/README.md#update) - Update a signing key

### [task](docs/sdks/task/README.md)

- [get_all](docs/sdks/task/README.md#get_all) - Retrieve Tasks
- [get](docs/sdks/task/README.md#get) - Retrieve a Task

### [transcode](docs/sdks/transcode/README.md)

- [create](docs/sdks/transcode/README.md#create) - Transcode a video

### [playback](docs/sdks/playback/README.md)

- [get](docs/sdks/playback/README.md#get) - Retrieve Playback Info
<!-- End Available Resources and Operations [operations] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 404              | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |

### Example

```python
import livepeer
from livepeer.models import errors

s = livepeer.Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)

res = None
try:
    res = s.playback.get(id='<value>')

except errors.Error as e:
    # handle exception
    raise(e)
except errors.SDKError as e:
    # handle exception
    raise(e)

if res.playback_info is not None:
    # handle response
    pass

```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://livepeer.studio/api` | None |

#### Example

```python
import livepeer
from livepeer.models import components

s = livepeer.Livepeer(
    server_idx=0,
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.stream.create(request=components.NewStreamPayload(
    name='test_stream',
    pull=components.Pull(
        source='https://myservice.com/live/stream.flv',
        headers={
            'Authorization': 'Bearer 123',
        },
        location=components.Location(
            lat=39.739,
            lon=-104.988,
        ),
    ),
    playback_policy=components.PlaybackPolicy(
        type=components.Type.WEBHOOK,
        webhook_id='1bde4o2i6xycudoy',
        webhook_context={
            'streamerId': 'my-custom-id',
        },
        refresh_interval=600,
    ),
    profiles=[
        components.FfmpegProfile(
            width=1280,
            name='720p',
            height=486589,
            bitrate=3000000,
            fps=30,
            fps_den=1,
            quality=23,
            gop='2',
            profile=components.Profile.H264_BASELINE,
        ),
    ],
    record=False,
    multistream=components.Multistream(
        targets=[
            components.Target(
                profile='720p',
                video_only=False,
                id='PUSH123',
                spec=components.TargetSpec(
                    url='rtmps://live.my-service.tv/channel/secretKey',
                    name='My target',
                ),
            ),
        ],
    ),
))

if res.stream is not None:
    # handle response
    pass

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import livepeer
from livepeer.models import components

s = livepeer.Livepeer(
    server_url="https://livepeer.studio/api",
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.stream.create(request=components.NewStreamPayload(
    name='test_stream',
    pull=components.Pull(
        source='https://myservice.com/live/stream.flv',
        headers={
            'Authorization': 'Bearer 123',
        },
        location=components.Location(
            lat=39.739,
            lon=-104.988,
        ),
    ),
    playback_policy=components.PlaybackPolicy(
        type=components.Type.WEBHOOK,
        webhook_id='1bde4o2i6xycudoy',
        webhook_context={
            'streamerId': 'my-custom-id',
        },
        refresh_interval=600,
    ),
    profiles=[
        components.FfmpegProfile(
            width=1280,
            name='720p',
            height=486589,
            bitrate=3000000,
            fps=30,
            fps_den=1,
            quality=23,
            gop='2',
            profile=components.Profile.H264_BASELINE,
        ),
    ],
    record=False,
    multistream=components.Multistream(
        targets=[
            components.Target(
                profile='720p',
                video_only=False,
                id='PUSH123',
                spec=components.TargetSpec(
                    url='rtmps://live.my-service.tv/channel/secretKey',
                    name='My target',
                ),
            ),
        ],
    ),
))

if res.stream is not None:
    # handle response
    pass

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [requests](https://pypi.org/project/requests/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import livepeer
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = livepeer.Livepeer(client=http_client)
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name        | Type        | Scheme      |
| ----------- | ----------- | ----------- |
| `api_key`   | http        | HTTP Bearer |

To authenticate with the API the `api_key` parameter must be set when initializing the SDK client instance. For example:
```python
import livepeer
from livepeer.models import components

s = livepeer.Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.stream.create(request=components.NewStreamPayload(
    name='test_stream',
    pull=components.Pull(
        source='https://myservice.com/live/stream.flv',
        headers={
            'Authorization': 'Bearer 123',
        },
        location=components.Location(
            lat=39.739,
            lon=-104.988,
        ),
    ),
    playback_policy=components.PlaybackPolicy(
        type=components.Type.WEBHOOK,
        webhook_id='1bde4o2i6xycudoy',
        webhook_context={
            'streamerId': 'my-custom-id',
        },
        refresh_interval=600,
    ),
    profiles=[
        components.FfmpegProfile(
            width=1280,
            name='720p',
            height=486589,
            bitrate=3000000,
            fps=30,
            fps_den=1,
            quality=23,
            gop='2',
            profile=components.Profile.H264_BASELINE,
        ),
    ],
    record=False,
    multistream=components.Multistream(
        targets=[
            components.Target(
                profile='720p',
                video_only=False,
                id='PUSH123',
                spec=components.TargetSpec(
                    url='rtmps://live.my-service.tv/channel/secretKey',
                    name='My target',
                ),
            ),
        ],
    ),
))

if res.stream is not None:
    # handle response
    pass

```
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->


