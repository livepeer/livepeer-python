<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
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

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from livepeer import Livepeer
from livepeer.models import components

async def main():
    s = Livepeer(
        api_key="<YOUR_BEARER_TOKEN_HERE>",
    )
    res = await s.stream.create_async(request={
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

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->