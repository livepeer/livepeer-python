# StorageStatus


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          | Example                                              |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `phase`                                              | [components.Phase](../../models/components/phase.md) | :heavy_check_mark:                                   | Phase of the asset storage                           | ready                                                |
| `progress`                                           | *Optional[float]*                                    | :heavy_minus_sign:                                   | Current progress of the task updating the storage.   | 0.5                                                  |
| `error_message`                                      | *Optional[str]*                                      | :heavy_minus_sign:                                   | Error message if the last storage changed failed.    | Failed to export to IPFS                             |
| `tasks`                                              | [components.Tasks](../../models/components/tasks.md) | :heavy_check_mark:                                   | N/A                                                  |                                                      |