# GetUsageMetricsResponse


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `http_meta`                                                                | [components.HTTPMetadata](../../models/components/httpmetadata.md)         | :heavy_check_mark:                                                         | N/A                                                                        |
| `usage_metric`                                                             | [Optional[components.UsageMetric]](../../models/components/usagemetric.md) | :heavy_minus_sign:                                                         | A Usage Metric object                                                      |
| `error`                                                                    | *Optional[errors.Error]*                                                   | :heavy_minus_sign:                                                         | Error                                                                      |