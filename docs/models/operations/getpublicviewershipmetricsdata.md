# GetPublicViewershipMetricsData

A simplified metric object about aggregate viewership of an
asset. Either playbackId or dStorageUrl will be set.



## Fields

| Field                                                 | Type                                                  | Required                                              | Description                                           | Example                                               |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `playback_id`                                         | *Optional[str]*                                       | :heavy_minus_sign:                                    | The playback ID associated with the metric.           | 1bde4o2i6xycudoy                                      |
| `d_storage_url`                                       | *Optional[str]*                                       | :heavy_minus_sign:                                    | The URL of the distributed storage used for the asset | ipfs://QmZ4                                           |
| `view_count`                                          | *Optional[int]*                                       | :heavy_minus_sign:                                    | The number of views for the stream/asset.             | 100                                                   |
| `playtime_mins`                                       | *Optional[float]*                                     | :heavy_minus_sign:                                    | The total playtime in minutes for the stream/asset.   | 10                                                    |