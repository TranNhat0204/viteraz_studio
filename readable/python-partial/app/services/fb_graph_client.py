# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/fb_graph_client.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _validate_scheduled_time
def _validate_scheduled_time(scheduled_time, reel):
    if scheduled_time is None:
        return None
    delta = float(scheduled_time) - time.time()
    if reel:
        max_delta = 29 * 24 * 60 * 60
    else:
        max_delta = 30 * 24 * 60 * 60
    if not delta < 600:
        if delta > max_delta:
            if reel:
                window = '29 ngày'
            else:
                window = '30 ngày'
            raise FbError('invalid_schedule', 
                'Lịch Facebook phải cách hiện tại ít nhất 10 phút và không quá ' +
                str(window) + '.')
    else:
        if reel:
            window = '29 ngày'
        else:
            window = '30 ngày'
        raise FbError('invalid_schedule', 
            'Lịch Facebook phải cách hiện tại ít nhất 10 phút và không quá ' +
            str(window) + '.')
    return None



# NOT DECOMPILED: _validate_video_media


# Original qualified name: FbGraphClient.__init__
def __init__(self, access_token, proxy, graph_api, timeout):
    self.access_token = access_token
    self.proxy = proxy
    self.graph_api = graph_api.rstrip('/')
    self.timeout = timeout
    return None



# Original qualified name: FbGraphClient._client
def _client(self):
    __temp_271758 = httpx.Timeout(self.timeout, connect=15)
    if not self.proxy:
        return httpx.AsyncClient(timeout=__temp_271758, proxy=None, headers={
            'User-Agent': 'RevoStudio/1.0 (+Graph API)'})
    else:
        return httpx.AsyncClient(timeout=__temp_271758, proxy=self.proxy,
            headers={'User-Agent': 'RevoStudio/1.0 (+Graph API)'})



# NOT DECOMPILED: FbGraphClient._request


# NOT DECOMPILED: FbGraphClient._get


# NOT DECOMPILED: FbGraphClient._post_form


# NOT DECOMPILED: FbGraphClient.get_page_stats


# NOT DECOMPILED: FbGraphClient.fetch_accounts


# NOT DECOMPILED: FbGraphClient.get_page_published_posts


# NOT DECOMPILED: FbGraphClient.get_video_views


# NOT DECOMPILED: FbGraphClient.get_video_views_batch


# NOT DECOMPILED: FbGraphClient.get_video_views_batch.<locals>.fetch_one


# NOT DECOMPILED: FbGraphClient.debug_token


# NOT DECOMPILED: FbGraphClient.post_text


# NOT DECOMPILED: FbGraphClient.post_photo


# NOT DECOMPILED: FbGraphClient.post_video


# NOT DECOMPILED: FbGraphClient._post_video_single


# NOT DECOMPILED: FbGraphClient._post_video_resumable


# NOT DECOMPILED: FbGraphClient.post_reel


# NOT DECOMPILED: FbGraphClient._video_result


# NOT DECOMPILED: post_to_page
