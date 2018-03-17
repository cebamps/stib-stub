# STIB stub

This small Flask server stubs the [STIB-MIVB
API](https://opendata.stib-mivb.be/).


## Endpoints

### Supported:

  - `/token`: stubs the OAuth2 Client Credentials token endpoint, returns a
    Bearer token.
  - `/OperationMonitoring/1.0/VehiclePositionByLine/<ids>` *(incomplete)*:
    returns a JSON file containing *only* `pointId` values for the *first* id
    requested in the comma-separated list. The other keys are not returned. The
    `pointId` values change over time at a regular interval.

### Not supported:

  - `/OperationMonitoring/1.0/PassingTimeByPoint/<ids>`
  - `/Files/2.0/Gtfs`
  - `/Files/2.0/Shapefiles`


## OAuth2 compliance

### Authentication This stub completely disregards authentication:

  - The token endpoint ignores the provided client credentials and always
    outputs the same token
  - The other API endpoints ignore the presence and validity of the attached
    tokens.

### Security
This stub server is not protected by TLS. This can be a problem with compliant
OAuth2 client implementations, as the standard states that client credentials
and access tokens must not be transmitted in the clear.

With oauthlib, setting the environment variable `OAUTHLIB_INSECURE_TRANSPORT=1`
relaxes this security requirement.
