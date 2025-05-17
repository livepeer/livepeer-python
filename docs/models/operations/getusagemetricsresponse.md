# GetUsageMetricsResponse


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `http_meta`                                                                | [components.HTTPMetadata](../../models/components/httpmetadata.md)         | :heavy_check_mark:                                                         | N/A                                                                        |
| `usage_metric`                                                             | [Optional[components.UsageMetric]](../../models/components/usagemetric.md) | :heavy_minus_sign:                                                         | A Usage Metric object                                                      |
| `error`                                                                    | [Optional[components.Error]](../../models/components/error.md)             | :heavy_minus_sign:                                                         | Error                                                                      |