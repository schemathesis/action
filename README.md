# Schemathesis GitHub Action

GitHub Action for running [Schemathesis](https://github.com/schemathesis/schemathesis) property-based API tests against OpenAPI and GraphQL schemas.

```yaml
- uses: schemathesis/action@v2
  with:
    # API schema location
    schema: 'https://example.schemathesis.io/openapi.json'
```

## Configuration

```yaml
- uses: schemathesis/action@v2
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
    # Additional CLI arguments
    args: '--report-junit-path=/tmp/junit.xml'
```

To add headers like `Authorization`:

```yaml
- name: Run with authentication
  uses: schemathesis/action@v2
  with:
    schema: 'http://example.com/api/openapi.json'
    args: '-H "Authorization: Bearer ${{ secrets.API_TOKEN }}"'
```

For additional options, see the [Schemathesis CLI reference](https://schemathesis.readthedocs.io/en/stable/reference/cli/).

## Resources

- [Documentation](https://schemathesis.readthedocs.io/en/stable/)
- [CLI Reference](https://schemathesis.readthedocs.io/en/stable/reference/cli/)
- [GitHub Issues](https://github.com/schemathesis/schemathesis/issues)
- [Discord](https://discord.gg/R9ASRAmHnA)

