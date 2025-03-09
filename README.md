# Schemathesis GitHub Action

A GitHub Action for running [Schemathesis](https://github.com/schemathesis/schemathesis) API tests. Automate your API testing to catch crashes, validate specs, and save time.

```yaml
- uses: schemathesis/action@v1
  with:
    # API schema location
    schema: 'https://example.schemathesis.io/openapi.json'
```

## Configuration

```yaml
- uses: schemathesis/action@v1
  with:
    # API schema location
    schema: 'https://example.schemathesis.io/openapi.json'
    # OPTIONAL. URL that will be used as a prefix for all API operations.
    # Useful when the API schema is maintained separately from the application.
    base-url: 'https://example.schemathesis.io/v2/'
    # OPTIONAL. List of Schemathesis checks to run. Defaults to `all`
    checks: 'not_a_server_error'
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

To add headers like `Authorization`:

```yaml
# Save access token to $GITHUB_ENV as ACCESS_TOKEN.
- name: Set access token
  run: echo "ACCESS_TOKEN=super-secret" >> $GITHUB_ENV

- uses: schemathesis/action@v1
  with:
    schema: 'http://example.com/api/openapi.json'
    args: '-H "Authorization: Bearer ${{ env.ACCESS_TOKEN }}"'
```

For more options and usage, check the [Schemathesis CLI documentation](https://schemathesis.readthedocs.io/en/stable/cli.html).

## Support

Having issues or questions? Check the [Schemathesis documentation](https://schemathesis.readthedocs.io/en/stable/), join the [Discord community](https://discord.gg/R9ASRAmHnA), or report problems on the [GitHub issue tracker](https://github.com/schemathesis/action/issues).
