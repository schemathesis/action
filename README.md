# Schemathesis GitHub Action

GitHub Action for running [Schemathesis](https://github.com/schemathesis/schemathesis) property-based API tests against OpenAPI and GraphQL schemas.

```yaml
- uses: schemathesis/action@v3
  with:
    # API schema location
    schema: 'https://example.schemathesis.io/openapi.json'
```

## Configuration

```yaml
- uses: schemathesis/action@v3
  with:
    # API schema location (URL or file path)
    schema: 'https://example.schemathesis.io/openapi.json'
    # Override base URL
    base-url: 'https://example.schemathesis.io/v2/'
    # Validation checks to run (default: all)
    checks: 'not_a_server_error'
    # Schema availability timeout in seconds
    wait-for-schema: '30'
    # Test cases per API operation
    max-examples: 50
    # Schemathesis version (default: latest)
    version: 'latest'
    # Python module path for hooks
    hooks: 'tests.hooks'
    # Path to a `schemathesis.toml` configuration file
    config-file: 'tests/schemathesis-config.yaml'
    # Authorization header value
    authorization: 'Bearer ${{ secrets.API_TOKEN }}'
    # Additional CLI arguments
    args: '--report-junit-path=/tmp/junit.xml'
    # Schema coverage (default: true)
    coverage: 'true'
    coverage-report: 'true'
    coverage-report-path: 'schema-coverage.html'
    coverage-artifact-name: 'schema-coverage-report'
    coverage-pr-comment: 'true'
    # Write coverage summary to the workflow step summary
    # set to false when using the action multiple times in one job
    coverage-step-summary: 'true'
```

To authenticate requests:

```yaml
- name: Run with authentication
  uses: schemathesis/action@v3
  with:
    schema: 'http://example.com/api/openapi.json'
    authorization: 'Bearer ${{ secrets.API_TOKEN }}'
```

For other schemes (Basic, custom):

```yaml
    authorization: 'Basic ${{ secrets.ENCODED_CREDENTIALS }}'
```

For additional options, see the [Schemathesis CLI reference](https://schemathesis.readthedocs.io/en/stable/reference/cli/).

## Coverage reports

Schema coverage is powered by [tracecov](https://docs.tracecov.sh) and enabled by default. Each run generates:
- A summary in the Actions step summary
- An HTML report uploaded as a workflow artifact (default name: `schema-coverage-report`)
- A PR comment with the coverage summary (pull requests only)

<img width="2236" height="1894" alt="report-demo" src="https://github.com/user-attachments/assets/85c4f138-64f0-434a-938f-e156115853c0" />

Coverage reports are generated even when schemathesis finds failures.

PR comments require `pull-requests: write` in your workflow:

```yaml
jobs:
  test:
    permissions:
      pull-requests: write
    steps:
      - uses: schemathesis/action@v3
        with:
          schema: 'http://example.com/api/openapi.json'
```

If you run the action more than once in a single workflow, set distinct artifact names to avoid conflicts:

```yaml
- uses: schemathesis/action@v3
  with:
    schema: 'http://example.com/api/v1/openapi.json'
    coverage-artifact-name: 'coverage-v1'

- uses: schemathesis/action@v3
  with:
    schema: 'http://example.com/api/v2/openapi.json'
    coverage-artifact-name: 'coverage-v2'
```

To disable coverage entirely:

```yaml
    coverage: 'false'
```

## Resources

- [Documentation](https://schemathesis.readthedocs.io/en/stable/)
- [CLI Reference](https://schemathesis.readthedocs.io/en/stable/reference/cli/)
- [GitHub Issues](https://github.com/schemathesis/schemathesis/issues)
- [Discord](https://discord.gg/R9ASRAmHnA)

