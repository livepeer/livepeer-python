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

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an error. If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object    | Status Code | Content Type     |
| --------------- | ----------- | ---------------- |
| errors.Error    | 404         | application/json |
| errors.SDKError | 4xx-5xx     | _/_              |

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
