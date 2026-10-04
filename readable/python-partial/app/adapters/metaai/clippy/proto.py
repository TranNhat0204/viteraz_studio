# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/metaai/clippy/proto.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: encode_varint


# Original qualified name: encode_tag
def encode_tag(dst, field, wire_type):
    return encode_varint(dst, field << 3 | wire_type)



# Original qualified name: encode_string
def encode_string(dst, field, s):
    b = s.encode('utf-8')
    dst = encode_tag(dst, field, 2)
    dst = encode_varint(dst, len(b))
    return dst + b



# Original qualified name: encode_bytes
def encode_bytes(dst, field, b):
    dst = encode_tag(dst, field, 2)
    dst = encode_varint(dst, len(b))
    return dst + b



# Original qualified name: encode_message
def encode_message(dst, field, msg):
    if msg is None:
        msg = b''
    dst = encode_tag(dst, field, 2)
    dst = encode_varint(dst, len(msg))
    return dst + msg



# Original qualified name: encode_varint_field
def encode_varint_field(dst, field, v):
    dst = encode_tag(dst, field, 0)
    return encode_varint(dst, v)



# Original qualified name: append_fixed32
def append_fixed32(dst, field, v):
    dst = encode_tag(dst, field, 5)
    return dst + struct.pack('<I', v & 4294967295)



# Original qualified name: pack_connect_header
def pack_connect_header(payload_len):
    return b'\x0f' + struct.pack('<H', 0) + struct.pack('<H', payload_len
        ) + b'\x00'



# Original qualified name: pack_chat_header
def pack_chat_header(payload_len, sub_type):
    return b'\r' + struct.pack('<H', 0) + struct.pack('<H', payload_len) + bytes([
        0, sub_type & 255, 128])



# NOT DECOMPILED: read_varint
