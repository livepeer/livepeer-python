# GetCreatorViewershipMetricsResponse


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `http_meta`                                                                      | [components.HTTPMetadata](../../models/components/httpmetadata.md)               | :heavy_check_mark:                                                               | N/A                                                                              |
| `data`                                                                           | List[[components.ViewershipMetric](../../models/components/viewershipmetric.md)] | :heavy_minus_sign:                                                               | A list of Metric objects                                                         |
| `error`                                                                          | [Optional[components.Error]](../../models/components/error.md)                   | :heavy_minus_sign:                                                               | Error                                                                            |