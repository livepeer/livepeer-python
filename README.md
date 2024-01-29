# Livepeer Python Library

The Livepeer Python library provides convenient access to the Livepeer Studio API from
applications written in Python

## Documentation

For full documentation and examples, please visit [docs.livepeer.org](https://docs.livepeer.org/sdks/javascript/).

## Installation

Install the package:

```bash
pip install livepeer
```

## Usage

The library needs to be configured with your Livepeer Studio account's API key, which is available in the [Studio Dashboard](httpss://livepeer.studio)

```python
import livepeer
from livepeer.models import operations

lpClient = livepeer.SDK(
    api_key="",
)


res = lpClient.stream.get_all()

if res.data is not None:
    # handle response
    pass
```

## Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:

```python
import livepeer
from livepeer.models import operations

lpClient = livepeer.SDK(
    server_url="https://livepeer.studio/api",
    api_key="",
)


res = lpClient.stream.get_all()

if res.data is not None:
    # handle response
    pass
```

## Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library. In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:

```python
import livepeer
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
lpClient = livepeer.SDK(client: http_client)
```

## Available Resources and Operations

### [stream](docs/sdks/stream/README.md)

- [get_all](docs/sdks/stream/README.md#get_all) - Retrieve streams
- [create](docs/sdks/stream/README.md#create) - Create a stream
- [delete](docs/sdks/stream/README.md#delete) - Delete a stream
- [get](docs/sdks/stream/README.md#get) - Retrieve a stream
- [update](docs/sdks/stream/README.md#update) - Update a stream
- [create_clip](docs/sdks/stream/README.md#create_clip) - Create a clip
- [get_all_clips](docs/sdks/stream/README.md#get_all_clips) - Retrieve clips of a livestream

### [multistream_target](docs/sdks/multistreamtarget/README.md)

- [get_all](docs/sdks/multistreamtarget/README.md#get_all) - Retrieve Multistream Targets
- [create](docs/sdks/multistreamtarget/README.md#create) - Create a multistream target
- [delete](docs/sdks/multistreamtarget/README.md#delete) - Delete a multistream target
- [get](docs/sdks/multistreamtarget/README.md#get) - Retrieve a multistream target
- [update](docs/sdks/multistreamtarget/README.md#update) - Update Multistream Target

### [webhook](docs/sdks/webhook/README.md)

- [get_all](docs/sdks/webhook/README.md#get_all) - Retrieve a Webhook
- [create](docs/sdks/webhook/README.md#create) - Create a webhook
- [delete](docs/sdks/webhook/README.md#delete) - Delete a webhook
- [get](docs/sdks/webhook/README.md#get) - Retrieve a webhook
- [update](docs/sdks/webhook/README.md#update) - Update a webhook

### [asset](docs/sdks/asset/README.md)

- [get_all](docs/sdks/asset/README.md#get_all) - Retrieve assets
- [create](docs/sdks/asset/README.md#create) - Upload an asset
- [create_via_url](docs/sdks/asset/README.md#create_via_url) - Upload asset via URL
- [delete](docs/sdks/asset/README.md#delete) - Delete an asset
- [get](docs/sdks/asset/README.md#get) - Retrieves an asset
- [update](docs/sdks/asset/README.md#update) - Update an asset

### [metrics](docs/sdks/metrics/README.md)

- [get_viewership](docs/sdks/metrics/README.md#get_viewership) - Query viewership metrics
- [get_creator_viewership](docs/sdks/metrics/README.md#get_creator_viewership) - Query creator viewership metrics
- [get_public_total_views](docs/sdks/metrics/README.md#get_public_total_views) - Query public total views metrics
- [get_usage](docs/sdks/metrics/README.md#get_usage) - Query usage metrics

### [session](docs/sdks/session/README.md)

- [get_all](docs/sdks/session/README.md#get_all) - Retrieve sessions
- [get](docs/sdks/session/README.md#get) - Retrieve a session
- [get_recorded](docs/sdks/session/README.md#get_recorded) - Retrieve Recorded Sessions
- [get_all_clips](docs/sdks/session/README.md#get_all_clips) - Retrieve clips of a session

### [access_control](docs/sdks/accesscontrol/README.md)

- [get_signing_keys](docs/sdks/accesscontrol/README.md#get_signing_keys) - Retrieves signing keys
- [create_signing_key](docs/sdks/accesscontrol/README.md#create_signing_key) - Create a signing key
- [delete_signing_key](docs/sdks/accesscontrol/README.md#delete_signing_key) - Delete Signing Key
- [get_signing_key](docs/sdks/accesscontrol/README.md#get_signing_key) - Retrieves a signing key
- [update_signing_key](docs/sdks/accesscontrol/README.md#update_signing_key) - Update a signing key

### [task](docs/sdks/task/README.md)

- [get_all](docs/sdks/task/README.md#get_all) - Retrieve Tasks
- [get](docs/sdks/task/README.md#get) - Retrieve a Task

### [transcode](docs/sdks/transcode/README.md)

- [create](docs/sdks/transcode/README.md#create) - Transcode a video

### [playback](docs/sdks/playback/README.md)

- [get](docs/sdks/playback/README.md#get) - Retrieve Playback Info

<!-- No SDK Installation -->
<!-- No SDK Example Usage -->
<!-- No SDK Available Operations -->


<!-- Start Error Handling -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 404              | application/json |
| errors.SDKError  | 400-600          | */*              |

### Example

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    api_key="",
)


res = None
try:
    res = s.playback.get(id='string')
except (errors.Error) as e:
    print(e) # handle exception

except (errors.SDKError) as e:
    print(e) # handle exception


if res.playback_info is not None:
    # handle response
    pass
```
<!-- End Error Handling -->



<!-- Start Server Selection -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://livepeer.studio/api` | None |

#### Example

```python
import sdk

s = sdk.SDK(
    server_idx=0,
    api_key="",
)


res = s.get_all()

if res.classes is not None:
    # handle response
    pass
```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import sdk

s = sdk.SDK(
    server_url="https://livepeer.studio/api",
    api_key="",
)


res = s.get_all()

if res.classes is not None:
    # handle response
    pass
```
<!-- End Server Selection -->



<!-- Start Custom HTTP Client -->
## Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import sdk
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = sdk.SDK(client: http_client)
```
<!-- End Custom HTTP Client -->



<!-- Start Authentication -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name        | Type        | Scheme      |
| ----------- | ----------- | ----------- |
| `api_key`   | http        | HTTP Bearer |

To authenticate with the API the `api_key` parameter must be set when initializing the SDK client instance. For example:
```python
import sdk

s = sdk.SDK(
    api_key="",
)


res = s.get_all()

if res.classes is not None:
    # handle response
    pass
```
<!-- End Authentication -->

<!-- Placeholder for Future Speakeasy SDK Sections -->


