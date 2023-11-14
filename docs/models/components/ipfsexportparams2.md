# IpfsExportParams2

Custom credentials for the Piñata service. Must have either
a JWT or an API key and an API secret.



## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `api_key`                                          | *str*                                              | :heavy_check_mark:                                 | Will be added to the pinata_api_key header.        |
| `api_secret`                                       | *str*                                              | :heavy_check_mark:                                 | Will be added to the pinata_secret_api_key header. |