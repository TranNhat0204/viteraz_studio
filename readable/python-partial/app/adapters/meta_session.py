# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/meta_session.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _map_error
def _map_error(e):
    if isinstance(e, StudioError):
        return e
    if isinstance(e, (ErrNotAuthenticated, ErrAccessTokenMissing, ErrRegionBlocked)
        ):
        return make_error(E.META_AUTH, str(e))
    if isinstance(e, ErrRateLimited):
        return make_error(E.META_RATE_LIMIT, str(e))
    if isinstance(e, ErrQuotaExceeded):
        return make_error(E.META_QUOTA, str(e))
    if isinstance(e, ErrTimeout):
        return make_error(E.META_TIMEOUT, str(e))
    if isinstance(e, ErrCancelled):
        return make_error(E.CANCELLED, 'Đã huỷ khi Meta AI đang tạo nội dung.')
    if isinstance(e, (ErrGraphQLValidation, ErrBadResponse)):
        return make_error(E.META_BAD_RESPONSE, str(e))
    if isinstance(e, ErrNetwork):
        return make_error(E.META_NETWORK, str(e))
    if isinstance(e, MetaAIError):
        return make_error(E.META_NETWORK, str(e))
    return make_error(E.META_NETWORK, str(e))



# Original qualified name: MetaSessionClient.__init__
def __init__(self, bridge_url, token, account_id, project_key):
    self.account_id = account_id
    self.project_key = project_key
    creds = meta_credentials.get_credentials(account_id)
    self._cookies = creds['cookies']
    self._access_token = creds['access_token']
    __temp_3975 = creds.get('user_agent')
    if not __temp_3975:
        self._user_agent = ''
    else:
        self._user_agent = __temp_3975
    self._sdk = None
    return None



# Original qualified name: MetaSessionClient.available
def available(self):
    __temp_3976 = bool(self._cookies)
    if not __temp_3976:
        return bool(self._access_token)
    else:
        return __temp_3976



# Original qualified name: MetaSessionClient._client
def _client(self):
    if self._sdk is None:
        self._sdk = MetaAIClient(cookies=self._cookies, access_token=self.
            _access_token, user_agent=self._user_agent)
    return self._sdk



# NOT DECOMPILED: MetaSessionClient.get_status


# NOT DECOMPILED: MetaSessionClient.generate_image


# NOT DECOMPILED: MetaSessionClient._normalize_aspect


# NOT DECOMPILED: MetaSessionClient.generate_video


# NOT DECOMPILED: MetaSessionClient._download_first


# NOT DECOMPILED: MetaSessionClient.download_asset
