import schemathesis


@schemathesis.check
def custom_check(response, case):
    # Always succeeds
    return None
