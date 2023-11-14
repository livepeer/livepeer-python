# ClipPayload


## Fields

| Field                                      | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `playback_id`                              | *str*                                      | :heavy_check_mark:                         | Playback ID of the stream or asset to clip |
| `start_time`                               | *float*                                    | :heavy_check_mark:                         | Start time of the clip in milliseconds     |
| `end_time`                                 | *Optional[float]*                          | :heavy_minus_sign:                         | End time of the clip in milliseconds       |
| `name`                                     | *Optional[str]*                            | :heavy_minus_sign:                         | Name of the clip                           |
| `session_id`                               | *Optional[str]*                            | :heavy_minus_sign:                         | Session ID of the stream to clip           |