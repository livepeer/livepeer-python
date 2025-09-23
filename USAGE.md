<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
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

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from livepeer import Livepeer
from livepeer.models import components

async def main():

    async with Livepeer(
        api_key="<YOUR_BEARER_TOKEN_HERE>",
    ) as l_client:

        res = await l_client.stream.create_async(request={
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

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->