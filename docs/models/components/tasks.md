# Tasks


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `pending`                                                                        | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | ID of any currently running task that is exporting this<br/>asset to IPFS.<br/>  |
| `last`                                                                           | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | ID of the last task to run successfully, that created<br/>the currently saved data.<br/> |
| `failed`                                                                         | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | ID of the last task to fail execution.                                           |