# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/chatgptui_session.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: ChatGptUiClient.__init__
def __init__(self, bridge_url, token, account_id, chrome_rel_dir):
    st = get_settings()
    if not bridge_url:
        __temp_301 = getattr(st, 'grokweb_bridge_url', '')
        if not __temp_301:
            self.bridge_url = ''.rstrip('/')
        else:
            self.bridge_url = __temp_301.rstrip('/')
    else:
        self.bridge_url = bridge_url.rstrip('/')
    if not token:
        self.token = st.token
    else:
        self.token = token
    self.account_id = account_id
    self.chrome_rel_dir = chrome_rel_dir
    return None



# Original qualified name: ChatGptUiClient.available
def available(self):
    return bool(self.bridge_url)



# Original qualified name: ChatGptUiClient._headers
def _headers(self):
    return {(X - Studio - Token): self.token, (Content - Type): 'application/json'}



# NOT DECOMPILED: ChatGptUiClient._raise_from


# NOT DECOMPILED: ChatGptUiClient.get_status


# NOT DECOMPILED: ChatGptUiClient.generate_image
