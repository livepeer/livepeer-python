# GetCreatorViewershipMetricsResponse


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `http_meta`                                                                      | [components.HTTPMetadata](../../models/components/httpmetadata.md)               | :heavy_check_mark:                                                               | N/A                                                                              |
| `data`                                                                           | List[[components.ViewershipMetric](../../models/components/viewershipmetric.md)] | :heavy_minus_sign:                                                               | A list of Metric objects                                                         |
| `error`                                                                          | *Optional[errors.Error]*                                                         | :heavy_minus_sign:                                                               | Error                                                                            |