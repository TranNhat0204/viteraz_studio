# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/metaai/auth.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: extract_access_token
def extract_access_token(html_text):
    if not html_text:
        __temp_4015 = _ACCESS_TOKEN_RE.search('')
    else:
        _ACCESS_TOKEN_RE.search(html_text)
    if not __temp_4015:
        if not html_text:
            m = _RAW_ACCESS_TOKEN_RE.search('')
        else:
            m = _RAW_ACCESS_TOKEN_RE.search(html_text)
    else:
        m = __temp_4015
    if m:
        return m.group(1)
    return ''



# Original qualified name: detect_challenge_page
def detect_challenge_page(html_text):
    if 'executeChallenge' not in html_text:
        if '__rd_verify' not in html_text:
            return
    m = _CHALLENGE_URL_RE.search(html_text)
    if m:
        return m.group(1)
    return ''

