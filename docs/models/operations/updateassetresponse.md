# UpdateAssetResponse


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `http_meta`                                                        | [components.HTTPMetadata](../../models/components/httpmetadata.md) | :heavy_check_mark:                                                 | N/A                                                                |
| `asset`                                                            | [Optional[components.Asset]](../../models/components/asset.md)     | :heavy_minus_sign:                                                 | Success                                                            |
| `error`                                                            | *Optional[errors.Error]*                                           | :heavy_minus_sign:                                                 | Error                                                              |