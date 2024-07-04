# GetRealtimeViewershipNowResponse


## Fields

| Field                                                                                            | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `http_meta`                                                                                      | [components.HTTPMetadata](../../models/components/httpmetadata.md)                               | :heavy_check_mark:                                                                               | N/A                                                                                              |
| `data`                                                                                           | List[[components.RealtimeViewershipMetric](../../models/components/realtimeviewershipmetric.md)] | :heavy_minus_sign:                                                                               | A list of Metric objects                                                                         |
| `error`                                                                                          | *Optional[errors.Error]*                                                                         | :heavy_minus_sign:                                                                               | Error                                                                                            |