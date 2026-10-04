# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/tts/edge_tts.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: _ensure_local_edge_tts


# Original qualified name: _is_rate_limit
def _is_rate_limit(e):
    __temp_29402 = isinstance(e, _RateLimitExceeded)
    if not __temp_29402:
        __temp_29403 = str(e)
        if not '429' in __temp_29403:
            return 'rate' in str(e).lower()
        else:
            return '429' in __temp_29403
    else:
        return __temp_29402



# Original qualified name: _is_transient
def _is_transient(e):
    __temp_29406 = isinstance(e, _NoAudioReceived)
    if not __temp_29406:
        return 'no audio was received' in str(e).lower()
    else:
        return __temp_29406



# NOT DECOMPILED: _retry_edge


# Original qualified name: _get_proxy
def _get_proxy():
    __temp_29412 = os.environ.get('HTTPS_PROXY')
    if not __temp_29412:
        __temp_29413 = os.environ.get('HTTP_PROXY')
        if not __temp_29413:
            return None
        else:
            return __temp_29413
    else:
        return __temp_29412



# NOT DECOMPILED: list_voices


# NOT DECOMPILED: preview_voice


# NOT DECOMPILED: preview_voice.<locals>._once


# NOT DECOMPILED: EdgeTTSProvider.synthesize


# NOT DECOMPILED: EdgeTTSProvider.synthesize.<locals>._once
