# GetSigningKeyResponse


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `http_meta`                                                              | [components.HTTPMetadata](../../models/components/httpmetadata.md)       | :heavy_check_mark:                                                       | N/A                                                                      |
| `signing_key`                                                            | [Optional[components.SigningKey]](../../models/components/signingkey.md) | :heavy_minus_sign:                                                       | Success                                                                  |
| `error`                                                                  | [Optional[components.Error]](../../models/components/error.md)           | :heavy_minus_sign:                                                       | Error                                                                    |