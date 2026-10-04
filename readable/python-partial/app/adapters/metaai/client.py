# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/metaai/client.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: _media_node_has_url


# Original qualified name: _media_node_urls
def _media_node_urls(value):
    found = []
    
    
    def __temp_4040(v):
        nonlocal found, walk
        if isinstance(v, str):
            if v.startswith(('http://', 'https://')):
                if v not in found:
                    found.append(v)
                    return None
                else:
                    return None
            else:
                return None
        if isinstance(v, dict):
            for __temp_4046 in iter(v.values()):
                item = __temp_4046
                walk(item)
                continue
            return None
        if isinstance(v, list):
            for __temp_4049 in iter(v):
                item = __temp_4049
                walk(item)
                continue
            return None
        return None
    
    
    walk = __temp_4040
    walk(value)
    return tuple(found)



# Original qualified name: _media_node_urls.<locals>.walk
def walk(v):
    nonlocal found, walk
    if isinstance(v, str):
        if v.startswith(('http://', 'https://')):
            if v not in found:
                found.append(v)
                return None
            else:
                return None
        else:
            return None
    if isinstance(v, dict):
        for __temp_4058 in iter(v.values()):
            item = __temp_4058
            walk(item)
            continue
        return None
    if isinstance(v, list):
        for __temp_4061 in iter(v):
            item = __temp_4061
            walk(item)
            continue
        return None
    return None



# Original qualified name: _media_node_id
def _media_node_id(node):
    if not isinstance(node, dict):
        return
    __temp_4064 = node.get('id')
    if not __temp_4064:
        __temp_4065 = node.get('media_id')
        if not __temp_4065:
            __temp_4066 = node.get('mediaId')
            if not __temp_4066:
                __temp_4067 = node.get('assetId')
                if not __temp_4067:
                    __temp_4068 = node.get('uuid')
                    if not __temp_4068:
                        return ''
                    else:
                        return __temp_4068
                else:
                    return __temp_4067
            else:
                return __temp_4066
        else:
            return __temp_4065
    else:
        return __temp_4064



# Original qualified name: MetaAIClient.__init__
def __init__(self, cookies, access_token, proxy_url, user_agent):
    if not cookies:
        self.cookies = dict({})
    else:
        self.cookies = dict(cookies)
    if not access_token:
        self.access_token = ''
    else:
        self.access_token = access_token
    if not user_agent:
        self.user_agent = C.DEFAULT_USER_AGENT
    else:
        self.user_agent = user_agent
    if not proxy_url:
        self._proxy_url = None
    else:
        self._proxy_url = proxy_url
    __temp_4072 = bool(self.cookies)
    if not __temp_4072:
        self.is_authed = bool(self.access_token)
    else:
        self.is_authed = __temp_4072
    self._ws = None
    self._ws_conv_id = ''
    self._ws_lock = asyncio.Lock()
    self._claimed_ids = set()
    self._claimed_urls = set()
    return None



# Original qualified name: MetaAIClient._new_http
def _new_http(self):
    kwargs = {'timeout': 60.0}
    if self._proxy_url:
        kwargs['proxies'] = self._proxy_url
    __temp_4079 = {}
    __temp_4079.update(kwargs)
    return httpx.AsyncClient(*(), **__temp_4079)



# Original qualified name: MetaAIClient.cookie_header
def cookie_header(self):
    return _cookie_header(self.cookies)



# NOT DECOMPILED: MetaAIClient.ensure_access_token


# NOT DECOMPILED: MetaAIClient._scrape_access_token


# NOT DECOMPILED: MetaAIClient.get_status


# NOT DECOMPILED: MetaAIClient._dial_clippy


# NOT DECOMPILED: MetaAIClient._close_ws


# NOT DECOMPILED: MetaAIClient.close


# NOT DECOMPILED: MetaAIClient.generate_image


# NOT DECOMPILED: MetaAIClient.generate_video


# NOT DECOMPILED: MetaAIClient.extend_video


# NOT DECOMPILED: MetaAIClient._generate


# NOT DECOMPILED: MetaAIClient._generate_content


# NOT DECOMPILED: MetaAIClient._send_generation_prompt


# NOT DECOMPILED: MetaAIClient._wait_for_new_media_item


# NOT DECOMPILED: MetaAIClient._latest_media_library_item


# NOT DECOMPILED: MetaAIClient._latest_media_library_items


# NOT DECOMPILED: MetaAIClient.upload_image
