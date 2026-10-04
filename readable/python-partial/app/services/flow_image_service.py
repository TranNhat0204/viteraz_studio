# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/flow_image_service.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: _dhash


# Original qualified name: _fp_file
def _fp_file():
    app = __import__('app.config', fromlist=('get_settings',), level=0)
    get_settings = app.get_settings
    return get_settings().data_dir / _FINGERPRINT_FILE



# NOT DECOMPILED: _fp_load


# NOT DECOMPILED: _fp_save


# NOT DECOMPILED: claim_asset


# NOT DECOMPILED: seed_fingerprints


# NOT DECOMPILED: usable_image


# Original qualified name: _is_hard_block
def _is_hard_block(e):
    if e.code == E.FLOW_RATE_LIMIT:
        if not e.message:
            return 'hoạt động bất thường' in ''
        else:
            return 'hoạt động bất thường' in e.message
    else:
        return e.code == E.FLOW_RATE_LIMIT



# NOT DECOMPILED: generate_flow_image


# NOT DECOMPILED: generate_flow_image.<locals>.emit


# NOT DECOMPILED: generate_flow_image.<locals>.passed_logo_gate


# NOT DECOMPILED: generate_flow_image.<locals>.accept
