# Schemathesis API testing

A GitHub Action for running [Schemathesis](https://github.com/schemathesis/schemathesis) API tests.
If you use GitHub Actions, there is a native [GitHub app](https://github.com/apps/schemathesis) that reports test results directly to your pull requests.

## Usage

Minimal:

```yaml
- uses: schemathesis/action@v1
  with:
    # API schema location
    schema: 'https://example.schemathesis.io/openapi.json'
```

All options:

```yaml
- uses: schemathesis/action@v1
  with:
    # API schema location
    schema: 'https://example.schemathesis.io/openapi.json'
    # OPTIONAL. URL that will be used as a prefix for all API operations.
    # Required if the schema is provided as a file.
    # Otherwise, inferred from the schema.
    base-url: 'https://example.schemathesis.io/v2/'
    # OPTIONAL. Your Schemathesis.io token
    token: ${{ secrets.SCHEMATHESIS_TOKEN }}
    # OPTIONAL. API name from Schemathesis.io
    api-name: 'payments-api'
    # OPTIONAL. List of Schemathesis checks to run. Defaults to `all`
    checks: 'not_a_server_error'
    # OPTIONAL. Whether you'd like to see the results in a Web UI
    # Defaults to `true`
    report: 'true'
    # OPTIONAL. Maximum time in seconds to wait on the API schema availability
    wait-for-schema: '30'
    # OPTIONAL. Maximum number of generated examples for each endpoint
    max-examples: 50
    # OPTIONAL. Specify which version of Schemathesis should be used. 
    # Defaults to `latest`
    version: 'latest'
    # OPTIONAL. Schemathesis hooks module. Available for Schemathesis >= 3.18.5 only
    hooks: 'tests.hooks'
    # OPTIONAL. Extra arguments to pass to Schemathesis
    args: '-D negative'
```
