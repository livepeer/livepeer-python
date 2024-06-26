<!-- Start SDK Example Usage [usage] -->
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
    recording_spec=components.NewStreamPayloadRecordingSpec(
        profiles=[
            components.TranscodeProfile(
                bitrate=3000000,
                width=1280,
                name='720p',
                quality=23,
                fps=30,
                fps_den=1,
                gop='2',
                profile=components.TranscodeProfileProfile.H264_BASELINE,
                encoder=components.TranscodeProfileEncoder.H_264,
            ),
        ],
    ),
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
<!-- End SDK Example Usage [usage] -->