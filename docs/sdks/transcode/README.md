# Transcode
(*transcode*)

### Available Operations

* [create](#create) - Transcode a video

## create

Transcode a video

### Example Usage

```python
import sdk
from sdk.models import components

s = sdk.SDK(
    api_key="",
)

req = components.TaskInput(
    input_asset_id='09F8B46C-61A0-4254-9875-F71F4C605BC7',
    output_asset_id='09F8B46C-61A0-4254-9875-F71F4C605BC7',
    params=components.Params(
        upload=components.TaskUpload(
            url='https://cdn.livepeer.com/ABC123/filename.mp4',
            encryption=components.Encryption(
                encrypted_key='string',
            ),
            recorded_session_id='78df0075-b5f3-4683-a618-1086faca35dc',
        ),
        import_=components.Upload(
            url='https://cdn.livepeer.com/ABC123/filename.mp4',
            encryption=components.Encryption(
                encrypted_key='string',
            ),
            recorded_session_id='78df0075-b5f3-4683-a618-1086faca35dc',
        ),
        components.ExportTaskParamsSchemas1(
            custom=components.Custom(
                url='https://s3.amazonaws.com/my-bucket/path/filename.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=LLMMB',
                headers={
                    "key": 'string',
                },
            ),
        ),
        export_data=components.TaskExportData(
            content=components.Content(),
            ipfs=components.IpfsExportParams1(
                nft_metadata=components.NftMetadata(),
                components.IpfsExportParamsSchemas1(
                    jwt='string',
                ),
            ),
        ),
        transcode=components.Transcode(
            profile=components.FfmpegProfile(
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
        ),
        transcode_file=components.TranscodeFile(
            input=components.Input(
                url='https://cdn.livepeer.com/ABC123/filename.mp4',
            ),
            storage=components.TaskStorage(
                url='s3+https://accessKeyId:secretAccessKey@s3Endpoint/bucket',
            ),
            outputs=components.Outputs(
                hls=components.Hls(
                    path='/samplevideo/hls',
                ),
                mp4=components.Mp4(
                    path='/samplevideo/mp4',
                ),
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
            components.CreatorID1(
                type=components.CreatorIDType.UNVERIFIED,
                value='string',
            ),
        ),
    ),
    clip=components.Clip(
        clip_strategy=components.ClipStrategy(),
    ),
    output=components.TaskOutput(
        upload=components.TaskUploadInput(
            asset_spec=components.AssetInput(
                type=components.AssetType.VIDEO,
                playback_id='eaw4nk06ts2d0mzb',
                playback_policy=components.PlaybackPolicy(
                    type=components.Type.JWT,
                    webhook_id='3e02c844-d364-4d48-b401-24b2773b5d6c',
                    webhook_context={
                        "foo": 'string',
                    },
                ),
                components.Asset1(
                    type=components.AssetSchemasType.URL,
                    url='https://impartial-dump.com',
                    encryption=components.Encryption(
                        encrypted_key='string',
                    ),
                ),
                components.CreatorID1(
                    type=components.CreatorIDType.UNVERIFIED,
                    value='string',
                ),
                storage=components.AssetStorageInput(
                    ipfs=components.AssetIpfsInput(
                        spec=components.AssetSpec(
                            nft_metadata=components.AssetNftMetadata(),
                        ),
                        cid='bafybeihoqtemwitqajy6d654tmghqqvxmzgblddj2egst6yilplr5num6u',
                        nft_metadata=components.IpfsFileInfoInput(
                            cid='bafybeihoqtemwitqajy6d654tmghqqvxmzgblddj2egst6yilplr5num6u',
                        ),
                    ),
                ),
                name='filename.mp4',
                hash=[
                    components.Hash(
                        hash='9b560b28b85378a5004117539196ab24e21bbd75b0e9eb1a8bc7c5fd80dc5b57',
                        algorithm='sha256',
                    ),
                ],
            ),
            additional_properties={
                "key": 'string',
            },
        ),
        import_=components.UploadInput(
            asset_spec=components.AssetInput(
                type=components.AssetType.VIDEO,
                playback_id='eaw4nk06ts2d0mzb',
                playback_policy=components.PlaybackPolicy(
                    type=components.Type.WEBHOOK,
                    webhook_id='3e02c844-d364-4d48-b401-24b2773b5d6c',
                    webhook_context={
                        "foo": 'string',
                    },
                ),
                components.Asset1(
                    type=components.AssetSchemasType.URL,
                    url='http://yummy-shift.info',
                    encryption=components.Encryption(
                        encrypted_key='string',
                    ),
                ),
                components.CreatorID1(
                    type=components.CreatorIDType.UNVERIFIED,
                    value='string',
                ),
                storage=components.AssetStorageInput(
                    ipfs=components.AssetIpfsInput(
                        spec=components.AssetSpec(
                            nft_metadata=components.AssetNftMetadata(),
                        ),
                        cid='bafybeihoqtemwitqajy6d654tmghqqvxmzgblddj2egst6yilplr5num6u',
                        nft_metadata=components.IpfsFileInfoInput(
                            cid='bafybeihoqtemwitqajy6d654tmghqqvxmzgblddj2egst6yilplr5num6u',
                        ),
                    ),
                ),
                name='filename.mp4',
                hash=[
                    components.Hash(
                        hash='9b560b28b85378a5004117539196ab24e21bbd75b0e9eb1a8bc7c5fd80dc5b57',
                        algorithm='sha256',
                    ),
                ],
            ),
            additional_properties={
                "key": 'string',
            },
        ),
        export=components.TaskExport(
            ipfs=components.TaskIpfsInput(
                video_file_cid='string',
            ),
        ),
        export_data=components.TaskSchemasExportData(
            ipfs=components.TaskSchemasIpfs(
                cid='string',
            ),
        ),
        transcode=components.TaskTranscodeInput(
            asset=components.TaskAssetInput(
                asset_spec=components.AssetInput(
                    type=components.AssetType.VIDEO,
                    playback_id='eaw4nk06ts2d0mzb',
                    playback_policy=components.PlaybackPolicy(
                        type=components.Type.WEBHOOK,
                        webhook_id='3e02c844-d364-4d48-b401-24b2773b5d6c',
                        webhook_context={
                            "foo": 'string',
                        },
                    ),
                    components.Asset1(
                        type=components.AssetSchemasType.URL,
                        url='https://abandoned-incident.biz',
                        encryption=components.Encryption(
                            encrypted_key='string',
                        ),
                    ),
                    components.CreatorID1(
                        type=components.CreatorIDType.UNVERIFIED,
                        value='string',
                    ),
                    storage=components.AssetStorageInput(
                        ipfs=components.AssetIpfsInput(
                            spec=components.AssetSpec(
                                nft_metadata=components.AssetNftMetadata(),
                            ),
                            cid='bafybeihoqtemwitqajy6d654tmghqqvxmzgblddj2egst6yilplr5num6u',
                            nft_metadata=components.IpfsFileInfoInput(
                                cid='bafybeihoqtemwitqajy6d654tmghqqvxmzgblddj2egst6yilplr5num6u',
                            ),
                        ),
                    ),
                    name='filename.mp4',
                    hash=[
                        components.Hash(
                            hash='9b560b28b85378a5004117539196ab24e21bbd75b0e9eb1a8bc7c5fd80dc5b57',
                            algorithm='sha256',
                        ),
                    ],
                ),
                additional_properties={
                    "key": 'string',
                },
            ),
        ),
    ),
)

res = s.transcode.create(req)

if res.task is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `request`                                                    | [components.TaskInput](../../models/components/taskinput.md) | :heavy_check_mark:                                           | The request object to use for the request.                   |


### Response

**[operations.TranscodeResponse](../../models/operations/transcoderesponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
