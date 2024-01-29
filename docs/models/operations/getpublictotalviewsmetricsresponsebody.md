# GetPublicTotalViewsMetricsResponseBody

A simplified metric object about aggregate viewership of an
asset. Either playbackId or dStorageUrl will be set.



## Fields

| Field                                                 | Type                                                  | Required                                              | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `playback_id`                                         | *Optional[str]*                                       | :heavy_minus_sign:                                    | The playback ID associated with the metric            |
| `d_storage_url`                                       | *Optional[str]*                                       | :heavy_minus_sign:                                    | The URL of the distributed storage used for the asset |
| `view_count`                                          | *int*                                                 | :heavy_check_mark:                                    | The number of views for the asset                     |
| `playtime_mins`                                       | *float*                                               | :heavy_check_mark:                                    | The total playtime in minutes for the asset           |