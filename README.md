# Livepeer Python Library

The Livepeer Python library provides convenient access to the Livepeer Studio API from
applications written in Python

## Documentation

For full documentation and examples, please visit [docs.livepeer.org](https://docs.livepeer.org/sdks/python/).

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with *uv*, *pip*, or *poetry* package managers.

### uv

*uv* is a fast Python package installer and resolver, designed as a drop-in replacement for pip and pip-tools. It's recommended for its speed and modern Python tooling capabilities.

```bash
uv add livepeer
```

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install livepeer
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add livepeer
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from livepeer python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "livepeer",
# ]
# ///

from livepeer import Livepeer

sdk = Livepeer(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- No SDK Example Usage [usage] -->
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

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [AccessControl](docs/sdks/accesscontrol/README.md)

* [create](docs/sdks/accesscontrol/README.md#create) - Create a signing key
* [get_all](docs/sdks/accesscontrol/README.md#get_all) - Retrieves signing keys
* [delete](docs/sdks/accesscontrol/README.md#delete) - Delete Signing Key
* [get](docs/sdks/accesscontrol/README.md#get) - Retrieves a signing key
* [update](docs/sdks/accesscontrol/README.md#update) - Update a signing key

### [Asset](docs/sdks/asset/README.md)

* [get_all](docs/sdks/asset/README.md#get_all) - Retrieve assets
* [create](docs/sdks/asset/README.md#create) - Upload an asset
* [create_via_url](docs/sdks/asset/README.md#create_via_url) - Upload asset via URL
* [get](docs/sdks/asset/README.md#get) - Retrieves an asset
* [update](docs/sdks/asset/README.md#update) - Patch an asset
* [delete](docs/sdks/asset/README.md#delete) - Delete an asset

### [Generate](docs/sdks/generate/README.md)

* [text_to_image](docs/sdks/generate/README.md#text_to_image) - Text To Image
* [image_to_image](docs/sdks/generate/README.md#image_to_image) - Image To Image
* [image_to_video](docs/sdks/generate/README.md#image_to_video) - Image To Video
* [upscale](docs/sdks/generate/README.md#upscale) - Upscale
* [audio_to_text](docs/sdks/generate/README.md#audio_to_text) - Audio To Text
* [segment_anything2](docs/sdks/generate/README.md#segment_anything2) - Segment Anything 2
* [llm](docs/sdks/generate/README.md#llm) - LLM
* [image_to_text](docs/sdks/generate/README.md#image_to_text) - Image To Text
* [live_video_to_video](docs/sdks/generate/README.md#live_video_to_video) - Live Video To Video
* [text_to_speech](docs/sdks/generate/README.md#text_to_speech) - Text To Speech

### [Metrics](docs/sdks/metrics/README.md)

* [get_realtime_viewership](docs/sdks/metrics/README.md#get_realtime_viewership) - Query realtime viewership
* [get_viewership](docs/sdks/metrics/README.md#get_viewership) - Query viewership metrics
* [get_creator_viewership](docs/sdks/metrics/README.md#get_creator_viewership) - Query creator viewership metrics
* [get_public_viewership](docs/sdks/metrics/README.md#get_public_viewership) - Query public total views metrics
* [get_usage](docs/sdks/metrics/README.md#get_usage) - Query usage metrics

### [Multistream](docs/sdks/multistream/README.md)

* [get_all](docs/sdks/multistream/README.md#get_all) - Retrieve Multistream Targets
* [create](docs/sdks/multistream/README.md#create) - Create a multistream target
* [get](docs/sdks/multistream/README.md#get) - Retrieve a multistream target
* [update](docs/sdks/multistream/README.md#update) - Update Multistream Target
* [delete](docs/sdks/multistream/README.md#delete) - Delete a multistream target

### [Playback](docs/sdks/playback/README.md)

* [get](docs/sdks/playback/README.md#get) - Retrieve Playback Info

### [~~Room~~](docs/sdks/room/README.md)

* [~~create~~](docs/sdks/room/README.md#create) - Create a room :warning: **Deprecated**
* [~~get~~](docs/sdks/room/README.md#get) - Retrieve a room :warning: **Deprecated**
* [~~delete~~](docs/sdks/room/README.md#delete) - Delete a room :warning: **Deprecated**
* [~~start_egress~~](docs/sdks/room/README.md#start_egress) - Start room RTMP egress :warning: **Deprecated**
* [~~stop_egress~~](docs/sdks/room/README.md#stop_egress) - Stop room RTMP egress :warning: **Deprecated**
* [~~create_user~~](docs/sdks/room/README.md#create_user) - Create a room user :warning: **Deprecated**
* [~~get_user~~](docs/sdks/room/README.md#get_user) - Get user details :warning: **Deprecated**
* [~~update_user~~](docs/sdks/room/README.md#update_user) - Update a room user :warning: **Deprecated**
* [~~delete_user~~](docs/sdks/room/README.md#delete_user) - Remove a user from the room :warning: **Deprecated**

### [Session](docs/sdks/session/README.md)

* [get_clips](docs/sdks/session/README.md#get_clips) - Retrieve clips of a session
* [get_all](docs/sdks/session/README.md#get_all) - Retrieve sessions
* [get](docs/sdks/session/README.md#get) - Retrieve a session
* [get_recorded](docs/sdks/session/README.md#get_recorded) - Retrieve Recorded Sessions

### [Stream](docs/sdks/stream/README.md)

* [create](docs/sdks/stream/README.md#create) - Create a stream
* [get_all](docs/sdks/stream/README.md#get_all) - Retrieve streams
* [get](docs/sdks/stream/README.md#get) - Retrieve a stream
* [update](docs/sdks/stream/README.md#update) - Update a stream
* [delete](docs/sdks/stream/README.md#delete) - Delete a stream
* [terminate](docs/sdks/stream/README.md#terminate) - Terminates a live stream
* [start_pull](docs/sdks/stream/README.md#start_pull) - Start ingest for a pull stream
* [create_clip](docs/sdks/stream/README.md#create_clip) - Create a clip
* [get_clips](docs/sdks/stream/README.md#get_clips) - Retrieve clips of a livestream
* [add_multistream_target](docs/sdks/stream/README.md#add_multistream_target) - Add a multistream target
* [remove_multistream_target](docs/sdks/stream/README.md#remove_multistream_target) - Remove a multistream target

### [Task](docs/sdks/task/README.md)

* [get_all](docs/sdks/task/README.md#get_all) - Retrieve Tasks
* [get](docs/sdks/task/README.md#get) - Retrieve a Task

### [Transcode](docs/sdks/transcode/README.md)

* [create](docs/sdks/transcode/README.md#create) - Transcode a video

### [Webhook](docs/sdks/webhook/README.md)

* [get_all](docs/sdks/webhook/README.md#get_all) - Retrieve a Webhook
* [create](docs/sdks/webhook/README.md#create) - Create a webhook
* [get](docs/sdks/webhook/README.md#get) - Retrieve a webhook
* [update](docs/sdks/webhook/README.md#update) - Update a webhook
* [delete](docs/sdks/webhook/README.md#delete) - Delete a webhook
* [get_logs](docs/sdks/webhook/README.md#get_logs) - Retrieve webhook logs
* [get_log](docs/sdks/webhook/README.md#get_log) - Retrieve a webhook log
* [resend_log](docs/sdks/webhook/README.md#resend_log) - Resend a webhook

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start File uploads [file-upload] -->
## File uploads

Certain SDK methods accept file objects as part of a request body or multi-part request. It is possible and typically recommended to upload files as a stream rather than reading the entire contents into memory. This avoids excessive memory consumption and potentially crashing with out-of-memory errors when working with very large files. The following example demonstrates how to attach a file stream to a request.

> [!TIP]
>
> For endpoints that handle file uploads bytes arrays can also be used. However, using streams is recommended for large files.
>

```python
from livepeer import Livepeer


with Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as l_client:

    res = l_client.generate.image_to_image(request={
        "prompt": "<value>",
        "image": {
            "file_name": "example.file",
            "content": open("example.file", "rb"),
        },
    })

    assert res.image_response is not None

    # Handle response
    print(res.image_response)

```
<!-- End File uploads [file-upload] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from livepeer import Livepeer
from livepeer.models import components
from livepeer.utils import BackoffStrategy, RetryConfig


with Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as l_client:

    res = l_client.stream.create(request={
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
                    "width": 1280,
                    "name": "720p",
                    "height": 720,
                    "bitrate": 3000000,
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
                    "id": "PUSH123",
                },
            ],
        },
    },
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    assert res.stream is not None

    # Handle response
    print(res.stream)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from livepeer import Livepeer
from livepeer.models import components
from livepeer.utils import BackoffStrategy, RetryConfig


with Livepeer(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as l_client:

    res = l_client.stream.create(request={
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
                    "width": 1280,
                    "name": "720p",
                    "height": 720,
                    "bitrate": 3000000,
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
                    "id": "PUSH123",
                },
            ],
        },
    })

    assert res.stream is not None

    # Handle response
    print(res.stream)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`LivepeerError`](./src/livepeer/models/errors/livepeererror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](#error-classes). |

### Example
```python
from livepeer import Livepeer
from livepeer.models import errors


with Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as l_client:
    res = None
    try:

        res = l_client.playback.get(id="<id>")

        assert res.playback_info is not None

        # Handle response
        print(res.playback_info)


    except errors.LivepeerError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

        # Depending on the method different errors may be thrown
        if isinstance(e, errors.Error):
            print(e.data.errors)  # Optional[List[str]]
```

### Error Classes
**Primary error:**
* [`LivepeerError`](./src/livepeer/models/errors/livepeererror.py): The base class for HTTP error responses.

<details><summary>Less common errors (9)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`LivepeerError`](./src/livepeer/models/errors/livepeererror.py)**:
* [`StudioAPIError`](./src/livepeer/models/errors/studioapierror.py): Applicable to 10 of 67 methods.*
* [`HTTPError`](./src/livepeer/models/errors/httperror.py): HTTP error response model. Applicable to 10 of 67 methods.*
* [`HTTPValidationError`](./src/livepeer/models/errors/httpvalidationerror.py): Validation Error. Status code `422`. Applicable to 10 of 67 methods.*
* [`Error`](./src/livepeer/models/errors/error.py): Playback not found. Status code `404`. Applicable to 1 of 67 methods.*
* [`ResponseValidationError`](./src/livepeer/models/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>

\* Check [the method documentation](#available-resources-and-operations) to see if the error is applicable.
<!-- End Error Handling [errors] -->

<!-- No Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from livepeer import Livepeer
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Livepeer(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from livepeer import Livepeer
from livepeer.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Livepeer(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name      | Type | Scheme      |
| --------- | ---- | ----------- |
| `api_key` | http | HTTP Bearer |

To authenticate with the API the `api_key` parameter must be set when initializing the SDK client instance. For example:
```python
from livepeer import Livepeer
from livepeer.models import components


with Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as l_client:

    res = l_client.stream.create(request={
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
                    "width": 1280,
                    "name": "720p",
                    "height": 720,
                    "bitrate": 3000000,
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
                    "id": "PUSH123",
                },
            ],
        },
    })

    assert res.stream is not None

    # Handle response
    print(res.stream)

```
<!-- End Authentication [security] -->

<!-- Start Summary [summary] -->
## Summary

Livepeer API Reference: Welcome to the Livepeer API reference docs. Here you will find all the
endpoints exposed on the standard Livepeer API, learn how to use them and
what they return.
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [Livepeer Python Library](#livepeer-python-library)
  * [Documentation](#documentation)
  * [SDK Installation](#sdk-installation)
  * [SDK Example Usage](#sdk-example-usage)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [File uploads](#file-uploads)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Custom HTTP Client](#custom-http-client)
  * [Authentication](#authentication)
  * [IDE Support](#ide-support)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)

<!-- End Table of Contents [toc] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `Livepeer` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from livepeer import Livepeer
def main():

    with Livepeer(
        api_key="<YOUR_BEARER_TOKEN_HERE>",
    ) as l_client:
        # Rest of application here...


# Or when using async:
async def amain():

    async with Livepeer(
        api_key="<YOUR_BEARER_TOKEN_HERE>",
    ) as l_client:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from livepeer import Livepeer
import logging

logging.basicConfig(level=logging.DEBUG)
s = Livepeer(debug_logger=logging.getLogger("livepeer"))
```
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->


