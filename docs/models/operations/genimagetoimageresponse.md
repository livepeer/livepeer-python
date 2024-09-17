# GenImageToImageResponse


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `http_meta`                                                                    | [components.HTTPMetadata](../../models/components/httpmetadata.md)             | :heavy_check_mark:                                                             | N/A                                                                            |
| `image_response`                                                               | [Optional[components.ImageResponse]](../../models/components/imageresponse.md) | :heavy_minus_sign:                                                             | Successful Response                                                            |
| `studio_api_error`                                                             | *Optional[errors.StudioAPIError]*                                              | :heavy_minus_sign:                                                             | Error                                                                          |