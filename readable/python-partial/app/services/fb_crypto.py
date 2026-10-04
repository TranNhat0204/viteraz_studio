# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/fb_crypto.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: _get_fernet


# Original qualified name: encrypt_secret
def encrypt_secret(plain):
    if not plain:
        return
    return _get_fernet().encrypt(plain.encode()).decode()



# NOT DECOMPILED: decrypt_secret
