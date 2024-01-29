# IpfsFileInfo


## Fields

| Field                                               | Type                                                | Required                                            | Description                                         |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| `cid`                                               | *str*                                               | :heavy_check_mark:                                  | CID of the file on IPFS                             |
| `url`                                               | *Optional[str]*                                     | :heavy_minus_sign:                                  | URL with IPFS scheme for the file                   |
| `gateway_url`                                       | *Optional[str]*                                     | :heavy_minus_sign:                                  | URL to access file via HTTP through an IPFS gateway |