# TaskExportData

Parameters for the export-data task


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `content`                                                                              | [components.Content](../../models/components/content.md)                               | :heavy_check_mark:                                                                     | File content to store into IPFS                                                        |
| `ipfs`                                                                                 | [Optional[components.IpfsExportParams1]](../../models/components/ipfsexportparams1.md) | :heavy_minus_sign:                                                                     | N/A                                                                                    |
| `type`                                                                                 | *Optional[str]*                                                                        | :heavy_minus_sign:                                                                     | Optional type of content                                                               |
| `id`                                                                                   | *Optional[str]*                                                                        | :heavy_minus_sign:                                                                     | Optional ID of the content                                                             |