# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/grokweb_session.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: GrokWebClient.__init__
def __init__(self, bridge_url, token, account_id):
    st = get_settings()
    if not bridge_url:
        __temp_3323 = getattr(st, 'grokweb_bridge_url', '')
        if not __temp_3323:
            self.bridge_url = ''.rstrip('/')
        else:
            self.bridge_url = __temp_3323.rstrip('/')
    else:
        self.bridge_url = bridge_url.rstrip('/')
    if not token:
        self.token = st.token
    else:
        self.token = token
    self.account_id = account_id
    return None



# Original qualified name: GrokWebClient.available
def available(self):
    return bool(self.bridge_url)



# Original qualified name: GrokWebClient._headers
def _headers(self):
    return {(X - Studio - Token): self.token, (Content - Type): 'application/json'}



# NOT DECOMPILED: GrokWebClient._raise_from


# NOT DECOMPILED: GrokWebClient.get_status


# NOT DECOMPILED: GrokWebClient.login


# NOT DECOMPILED: GrokWebClient.generate_video
