# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/ima2_client.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: _cleanup_gateway


# NOT DECOMPILED: _size


# NOT DECOMPILED: _walk_media


# NOT DECOMPILED: _decode_image


# Original qualified name: _looks_like_image
def _looks_like_image(data):
    return data.startswith((b'\x89PNG\r\n\x1a\n', b'\xff\xd8\xff', b'RIFF'))



# NOT DECOMPILED: _local_image_path


# NOT DECOMPILED: _reference_payload


# Original qualified name: _grok_video_inputs
def _grok_video_inputs(prompt, source_image, references):
    if source_image:
        locked = (
            """[THE ATTACHED IMAGE IS THE APPROVED FIRST FRAME — ANIMATE IT, DO NOT REPLACE IT]
    Rewrite the line below into a motion description for that exact frame only: camera move, subject motion, micro-expressions. Keep the same characters, faces, clothing, illustration style, composition, props, palette and location as the attached frame. Do not invent a new location, do not switch to photorealism, and never substitute symbolic stock imagery (no lighthouses, mountains, oceans, sunsets or metaphors) for the scene.
    
    """
             + prompt)
        return locked, []
    return prompt, _reference_payload(references)



# NOT DECOMPILED: _gateway_error


# Original qualified name: Ima2Client.__init__
def __init__(self, base_url, token):
    settings = get_settings()
    if not base_url:
        __temp_3502 = getattr(settings, 'ima2_url', '')
        if not __temp_3502:
            self.base_url = 'http://127.0.0.1:3333'.rstrip('/')
        else:
            self.base_url = __temp_3502.rstrip('/')
    else:
        self.base_url = base_url.rstrip('/')
    if not token:
        __temp_3506 = getattr(settings, 'ima2_token', '')
        if not __temp_3506:
            self.token = ''
        else:
            self.token = __temp_3506
    else:
        self.token = token
    return None



# Original qualified name: Ima2Client.available
def available(self):
    return bool(self.base_url)



# Original qualified name: Ima2Client._headers
def _headers(self, accept):
    if not accept:
        headers = {'Accept': 'application/json'}
    else:
        headers = {'Accept': accept}
    if self.token:
        headers['Authorization'] = 'Bearer ' + str(self.token)
    return headers



# NOT DECOMPILED: Ima2Client.get_status


# NOT DECOMPILED: Ima2Client.restart_gateway


# NOT DECOMPILED: Ima2Client._ensure_gateway


# NOT DECOMPILED: Ima2Client.get_provider_status


# NOT DECOMPILED: Ima2Client.generate_image


# NOT DECOMPILED: Ima2Client.generate_video
