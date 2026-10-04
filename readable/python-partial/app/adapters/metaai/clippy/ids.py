# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/metaai/clippy/ids.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: v4
def v4():
    b = bytearray(secrets.token_bytes(16))
    b[6] = b[6] & 15 | 64
    b[8] = b[8] & 63 | 128
    h = b.hex()
    return str(h[0:8]) + '-' + str(h[8:12]) + '-' + str(h[12:16]) + '-' + str(h
        [16:20]) + '-' + str(h[20:32])



# Original qualified name: numeric_string
def numeric_string(digits):
    if digits <= 0:
        return
    limit = 10 ** digits
    n = secrets.randbelow(limit)
    s = str(n)
    if len(s) < digits:
        s = s.rjust(digits, '0')
        return s
    if len(s) > digits:
        s = s[None:digits]
    return s



# NOT DECOMPILED: numeric_id


# NOT DECOMPILED: rand_id_suffix


# Original qualified name: offline_threading_id
def offline_threading_id():
    ts = int(time.time() * 1000)
    mask22 = 4194303
    max64 = 18446744073709551615
    r = int.from_bytes(secrets.token_bytes(8), 'little')
    return str((ts << 22 | r & mask22) & max64)



# Original qualified name: uuid_func
def uuid_func():
    return v4()



# Original qualified name: debug_enabled
def debug_enabled():
    return os.environ.get('META_AI_DEBUG') in ('1', 'true')

