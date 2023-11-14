# Status

status of webhook


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                | Example                                                                    |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `last_failure`                                                             | [Optional[components.LastFailure]](../../models/components/lastfailure.md) | :heavy_minus_sign:                                                         | failure timestamp and error message with status code                       |                                                                            |
| `last_triggered_at`                                                        | *Optional[float]*                                                          | :heavy_minus_sign:                                                         | Timestamp (in milliseconds) at which the webhook last was<br/>triggered<br/> | 1587667174725                                                              |