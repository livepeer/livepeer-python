# AssetSource3


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `type`                                                                               | [components.AssetSource3Type](../../models/components/assetsource3type.md)           | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `encryption`                                                                         | [Optional[components.EncryptionOutput]](../../models/components/encryptionoutput.md) | :heavy_minus_sign:                                                                   | N/A                                                                                  |
| `source_id`                                                                          | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | ID of the asset or stream from which this asset was created.                         |
| `session_id`                                                                         | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | ID of the session from which this asset was created.                                 |
| `playback_id`                                                                        | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | Playback ID of the asset or stream from which this asset was created.                |
| `requester_id`                                                                       | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | ID of the requester from which this asset was created.                               |
| `asset_id`                                                                           | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | ID of the asset from which this asset was created.                                   |