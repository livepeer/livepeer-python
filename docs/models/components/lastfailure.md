# LastFailure

failure timestamp and error message with status code


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  | Example                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `timestamp`                                                  | *Optional[float]*                                            | :heavy_minus_sign:                                           | Timestamp (in milliseconds) at which the webhook last failed | 1587667174725                                                |
| `error`                                                      | *Optional[str]*                                              | :heavy_minus_sign:                                           | Webhook failure error message                                | Error message                                                |
| `response`                                                   | *Optional[str]*                                              | :heavy_minus_sign:                                           | Webhook failure response                                     | Response body                                                |
| `status_code`                                                | *Optional[float]*                                            | :heavy_minus_sign:                                           | Webhook failure status code                                  | 500                                                          |