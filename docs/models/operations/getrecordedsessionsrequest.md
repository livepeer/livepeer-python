# GetRecordedSessionsRequest


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            | Example                                                                |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `parent_id`                                                            | *str*                                                                  | :heavy_check_mark:                                                     | ID of the parent stream                                                |                                                                        |
| `record`                                                               | [Optional[operations.Record]](../../models/operations/record.md)       | :heavy_minus_sign:                                                     | Flag indicating if the response should only include recorded<br/>sessions<br/> | true                                                                   |