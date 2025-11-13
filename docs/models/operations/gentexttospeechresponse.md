# GenTextToSpeechResponse


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `http_meta`                                                                    | [components.HTTPMetadata](../../models/components/httpmetadata.md)             | :heavy_check_mark:                                                             | N/A                                                                            |
| `audio_response`                                                               | [Optional[components.AudioResponse]](../../models/components/audioresponse.md) | :heavy_minus_sign:                                                             | Successful Response                                                            |
| `studio_api_error`                                                             | *Optional[errors.StudioAPIError]*                                              | :heavy_minus_sign:                                                             | Error                                                                          |