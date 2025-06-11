import schemathesis


@schemathesis.check
def custom_check(ctx, response, case):
    # Always succeeds
    return None
