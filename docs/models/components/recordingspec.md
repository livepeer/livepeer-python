# RecordingSpec

Configuration for recording the stream. This can only be set if
`record` is true.



## Fields

| Field                                                                                                                                                                                       | Type                                                                                                                                                                                        | Required                                                                                                                                                                                    | Description                                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `profiles`                                                                                                                                                                                  | List[[components.FfmpegProfile](../../models/components/ffmpegprofile.md)]                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                          | Profiles to record the stream in. If not specified, the stream<br/>will be recorded in the same profiles as the stream itself. Keep<br/>in mind that the source rendition will always be recorded.<br/> |