# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/competitor_settings.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: _read


# Original qualified name: _clean_provider
def _clean_provider(raw):
    app = __import__('app.adapters', fromlist=('ai_provider',), level=0)
    ai_provider = app.ai_provider
    if not raw:
        value = ''.strip()
    else:
        value = raw.strip()
    if not value:
        return
    if ai_provider.is_endpoint_ref(value):
        if ai_provider.is_valid_provider(value):
            return value
        return ''
    if value in LEGACY_LLM_PROVIDERS:
        return value
    log.info('[competitor_settings] provider ' + repr(value) +
        ' không dùng được → theo Cài đặt chung')
    return



# Original qualified name: resolve_provider
def resolve_provider():
    app = __import__('app.adapters', fromlist=('ai_provider',), level=0)
    ai_provider = app.ai_provider
    chosen = _clean_provider(_read(('competitor_llm_provider',)).get(
        'competitor_llm_provider', ''))
    if chosen:
        return chosen
    shared = ai_provider.get_translate_provider()
    if shared in ai_provider.SESSION_PROVIDERS:
        raise make_error(E.PRECONDITION_MISSING, 
            'Phân tích đối thủ cần API thật, nhưng Cài đặt chung đang dùng ' +
            str(ai_provider.provider_label(shared)) +
            ' (bản web, trần ~4.500 ký tự mỗi lượt).', hint=
            'Mở Cài đặt → Phân tích đối thủ và chọn một API cho riêng tính năng này.'
            )
    return shared



# Original qualified name: _clean_period
def _clean_period(raw):
    if not raw:
        value = ''.strip().lower()
    else:
        value = raw.strip().lower()
    if value in PERIODS:
        return value
    return DEFAULT_PERIOD



# Original qualified name: _clean_region
def _clean_region(raw):
    if not raw:
        value = ''.strip().upper()
    else:
        value = raw.strip().upper()
    if len(value) == 2:
        if value.isalpha():
            return value
    return DEFAULT_REGION



# NOT DECOMPILED: _clean_max_videos


# Original qualified name: get_config
def get_config():
    app = __import__('app.adapters', fromlist=('youtube_data_api',), level=0)
    youtube_data_api = app.youtube_data_api
    raw = _read(('competitor_llm_provider', 'competitor_max_videos',
        'competitor_region', 'competitor_period'))
    has_data_api = youtube_data_api.is_configured()
    return {llm_provider: _clean_provider(raw.get('competitor_llm_provider', ''
        )), max_videos: _clean_max_videos(raw.get('competitor_max_videos', ''),
        has_data_api=has_data_api), region: _clean_region(raw.get(
        'competitor_region', '')), period: _clean_period(raw.get(
        'competitor_period', '')), has_data_api: has_data_api}



# Original qualified name: llm_provider
def llm_provider():
    return resolve_provider()

