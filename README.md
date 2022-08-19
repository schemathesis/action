# Schemathesis API testing

A GitHub Action for running [Schemathesis](https://github.com/schemathesis/schemathesis) API tests.

## Usage

```yaml
- uses: schemathesis/action@v1
  with:
    # API schema location
    schema: 'http://127.0.0.1:5001/openapi.json'
    # OPTIONAL. URL that will be used as a prefix for all API operations.
    # Required if the schema is provided as a file.
    # Otherwise, inferred from the schema.
    base-url: 'http://127.0.0.1'
    # OPTIONAL. Your Schemathesis.io token
    token: ${{ secrets.SCHEMATHESIS_TOKEN }}
    # OPTIONAL. API name from Schemathesis.io
    api-name: 'payments-api'
    # OPTIONAL. List of Schemathesis checks to run. Defaults to `all`
    checks: 'not_a_server_error'
    # OPTIONAL. Whether you'd like to see the results in a Web UI in Schemathesis.io
    # Defaults to `true`
    report: 'true'
    # OPTIONAL. Maximum time in seconds to wait on the API schema availability
    wait-for-schema: '30'
    # OPTIONAL. Maximum number of generated examples for each endpoint
    max-examples: 50
    # OPTIONAL. Specify which version of Schemathesis should be used. Defaults to `latest`
    version: 'latest'
    # OPTIONAL. Extra arguments to pass to Schemathesis
    args: '-D negative'
```
