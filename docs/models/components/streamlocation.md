# StreamLocation

Approximate location of the pull source. The location is used to
determine the closest Livepeer region to pull the stream from.


## Fields

| Field                                                                         | Type                                                                          | Required                                                                      | Description                                                                   | Example                                                                       |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `lat`                                                                         | *float*                                                                       | :heavy_check_mark:                                                            | Latitude of the pull source in degrees. North is positive,<br/>south is negative. | 39.739                                                                        |
| `lon`                                                                         | *float*                                                                       | :heavy_check_mark:                                                            | Longitude of the pull source in degrees. East is positive,<br/>west is negative. | -104.988                                                                      |