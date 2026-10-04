# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/flow_session.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: FlowSessionClient.__init__
def __init__(self, bridge_url, token, account_id, project_key, video_engine, video_model, image_model):
    st = get_settings()
    if not bridge_url:
        if not st.flow_bridge_url:
            self.bridge_url = ''.rstrip('/')
        else:
            self.bridge_url = st.flow_bridge_url.rstrip('/')
    else:
        self.bridge_url = bridge_url.rstrip('/')
    if not token:
        self.token = st.token
    else:
        self.token = token
    self.account_id = account_id
    self.project_key = project_key
    self.video_engine = video_engine
    self.video_model = video_model
    self.image_model = image_model
    return None



# Original qualified name: FlowSessionClient.available
def available(self):
    return bool(self.bridge_url)



# Original qualified name: FlowSessionClient._headers
def _headers(self):
    return {(X - Studio - Token): self.token, (Content - Type): 'application/json'}



# NOT DECOMPILED: FlowSessionClient.get_status


# NOT DECOMPILED: FlowSessionClient.get_credits


# NOT DECOMPILED: FlowSessionClient._record_usage


# Original qualified name: FlowSessionClient._pace_state
def _pace_state(self):
    if not self.account_id:
        __temp_3157 = 'default'.strip()
    else:
        self.account_id.strip()
    if not __temp_3157:
        key = 'default'
    else:
        key = __temp_3157
    return _FLOW_PACE.setdefault(key, _FlowPaceState())



# Original qualified name: FlowSessionClient._min_gap
def _min_gap(kind):
    if kind == 'video':
        return FLOW_VIDEO_MIN_GAP
    if kind == 'character':
        return FLOW_CHARACTER_MIN_GAP
    return FLOW_IMAGE_MIN_GAP



# NOT DECOMPILED: FlowSessionClient._paced_submit


# NOT DECOMPILED: FlowSessionClient._post


# NOT DECOMPILED: FlowSessionClient.cancel


# NOT DECOMPILED: FlowSessionClient.close_chrome


# NOT DECOMPILED: FlowSessionClient.rotate_project


# NOT DECOMPILED: FlowSessionClient.submit_image


# NOT DECOMPILED: FlowSessionClient.submit_video


# NOT DECOMPILED: FlowSessionClient.create_character


# NOT DECOMPILED: FlowSessionClient.poll


# NOT DECOMPILED: FlowSessionClient.download_asset


# NOT DECOMPILED: FlowSessionClient._await_operation


# NOT DECOMPILED: FlowSessionClient.generate_image


# NOT DECOMPILED: FlowSessionClient.resume_operation


# NOT DECOMPILED: FlowSessionClient.generate_video
