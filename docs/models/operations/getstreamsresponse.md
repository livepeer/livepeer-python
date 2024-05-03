# GetStreamsResponse


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `http_meta`                                                        | [components.HTTPMetadata](../../models/components/httpmetadata.md) | :heavy_check_mark:                                                 | N/A                                                                |
| `data`                                                             | List[[components.Stream](../../models/components/stream.md)]       | :heavy_minus_sign:                                                 | Success                                                            |
| `error`                                                            | *Optional[errors.Error]*                                           | :heavy_minus_sign:                                                 | Error                                                              |