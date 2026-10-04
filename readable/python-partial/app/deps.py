# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/deps.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: verify_token
def verify_token(x_studio_token, token):
    if not x_studio_token:
        incoming = token
    else:
        incoming = x_studio_token
    if incoming != get_settings().token:
        raise HTTPException(status_code=401, detail='invalid or missing token')
    return True



# Original qualified name: verify_token_ws
def verify_token_ws(token):
    return token == get_settings().token

