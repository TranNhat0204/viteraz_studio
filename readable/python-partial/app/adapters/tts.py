# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/tts.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: default_provider
def default_provider():
    saved = get_setting_value('tts_provider_default')
    if saved in _RETIRED_PROVIDERS:
        return DEFAULT_PROVIDER
    if saved in PROVIDER_IDS:
        return saved
    return DEFAULT_PROVIDER



# Original qualified name: normalize_provider
def normalize_provider(name):
    if not name:
        return default_provider()
    key = name.strip().lower()
    key = _ALIASES.get(key, key)
    if key not in PROVIDER_IDS:
        raise make_error(E.TTS_PROVIDER_INVALID, 
            'Nhà cung cấp TTS không hợp lệ: ' + str(name))
    return key



# Original qualified name: _module
def _module(provider_id):
    if provider_id == 'revo-voice':
        app = __import__('app.adapters.tts', fromlist=('revo_voice',), level=0)
        revo_voice = app.revo_voice
        mod = revo_voice
        return mod
    if provider_id == 'edge-tts':
        app = __import__('app.adapters.tts', fromlist=('edge_tts',), level=0)
        edge_tts = app.edge_tts
        mod = edge_tts
        return mod
    if provider_id == 'azure-tts':
        app = __import__('app.adapters.tts', fromlist=('azure_tts',), level=0)
        azure_tts = app.azure_tts
        mod = azure_tts
        return mod
    if provider_id == 'kokoro':
        app = __import__('app.adapters.tts', fromlist=('kokoro_tts',), level=0)
        kokoro_tts = app.kokoro_tts
        mod = kokoro_tts
        return mod
    if provider_id == 'kokoro_vi':
        app = __import__('app.adapters.tts', fromlist=('kokoro_vi_tts',), level=0)
        kokoro_vi_tts = app.kokoro_vi_tts
        mod = kokoro_vi_tts
        return mod
    if provider_id == 'omnivoice':
        app = __import__('app.adapters.tts', fromlist=('omnivoice_tts',), level=0)
        omnivoice_tts = app.omnivoice_tts
        mod = omnivoice_tts
        return mod
    if provider_id == 'gemini-tts':
        app = __import__('app.adapters.tts', fromlist=('gemini_tts',), level=0)
        gemini_tts = app.gemini_tts
        mod = gemini_tts
        return mod
    if provider_id == 'capcut-tts':
        app = __import__('app.adapters.tts', fromlist=('capcut_tts',), level=0)
        capcut_tts = app.capcut_tts
        mod = capcut_tts
        return mod
    if provider_id == 'vbee-tts':
        app = __import__('app.adapters.tts', fromlist=('vbee_tts',), level=0)
        vbee_tts = app.vbee_tts
        mod = vbee_tts
        return mod
    if provider_id == 'resona-tts':
        app = __import__('app.adapters.tts', fromlist=('resona_tts',), level=0)
        resona_tts = app.resona_tts
        mod = resona_tts
        return mod
    if provider_id == 'gcloud-tts':
        app = __import__('app.adapters.tts', fromlist=('gcloud_tts',), level=0)
        gcloud_tts = app.gcloud_tts
        mod = gcloud_tts
        return mod
    if provider_id == 'ai33-tts':
        app = __import__('app.adapters.tts', fromlist=('ai33_tts',), level=0)
        ai33_tts = app.ai33_tts
        mod = ai33_tts
        return mod
    app = __import__('app.adapters.tts', fromlist=('elevenlabs_tts',), level=0)
    elevenlabs_tts = app.elevenlabs_tts
    mod = elevenlabs_tts
    return mod



# Original qualified name: get_provider
def get_provider(name):
    pid = normalize_provider(name)
    if pid == 'revo-voice':
        app = __import__('app.adapters.tts.revo_voice', fromlist=(
            'RevoVoiceProvider',), level=0)
        RevoVoiceProvider = app.RevoVoiceProvider
        return RevoVoiceProvider()
    if pid == 'edge-tts':
        app = __import__('app.adapters.tts.edge_tts', fromlist=(
            'EdgeTTSProvider',), level=0)
        EdgeTTSProvider = app.EdgeTTSProvider
        return EdgeTTSProvider()
    if pid == 'azure-tts':
        app = __import__('app.adapters.tts.azure_tts', fromlist=(
            'AzureTTSProvider',), level=0)
        AzureTTSProvider = app.AzureTTSProvider
        return AzureTTSProvider()
    if pid == 'kokoro':
        app = __import__('app.adapters.tts.kokoro_tts', fromlist=(
            'KokoroTTSProvider',), level=0)
        KokoroTTSProvider = app.KokoroTTSProvider
        return KokoroTTSProvider()
    if pid == 'kokoro_vi':
        app = __import__('app.adapters.tts.kokoro_vi_tts', fromlist=(
            'KokoroViTTSProvider',), level=0)
        KokoroViTTSProvider = app.KokoroViTTSProvider
        return KokoroViTTSProvider()
    if pid == 'omnivoice':
        app = __import__('app.adapters.tts.omnivoice_tts', fromlist=(
            'OmniVoiceProvider',), level=0)
        OmniVoiceProvider = app.OmniVoiceProvider
        return OmniVoiceProvider()
    if pid == 'gemini-tts':
        app = __import__('app.adapters.tts.gemini_tts', fromlist=(
            'GeminiTTSProvider',), level=0)
        GeminiTTSProvider = app.GeminiTTSProvider
        return GeminiTTSProvider()
    if pid == 'capcut-tts':
        app = __import__('app.adapters.tts.capcut_tts', fromlist=(
            'CapCutTTSProvider',), level=0)
        CapCutTTSProvider = app.CapCutTTSProvider
        return CapCutTTSProvider()
    if pid == 'vbee-tts':
        app = __import__('app.adapters.tts.vbee_tts', fromlist=(
            'VbeeTTSProvider',), level=0)
        VbeeTTSProvider = app.VbeeTTSProvider
        return VbeeTTSProvider()
    if pid == 'resona-tts':
        app = __import__('app.adapters.tts.resona_tts', fromlist=(
            'ResonaTTSProvider',), level=0)
        ResonaTTSProvider = app.ResonaTTSProvider
        return ResonaTTSProvider()
    if pid == 'gcloud-tts':
        app = __import__('app.adapters.tts.gcloud_tts', fromlist=(
            'GoogleCloudTTSProvider',), level=0)
        GoogleCloudTTSProvider = app.GoogleCloudTTSProvider
        return GoogleCloudTTSProvider()
    if pid == 'ai33-tts':
        app = __import__('app.adapters.tts.ai33_tts', fromlist=(
            'AI33TTSProvider',), level=0)
        AI33TTSProvider = app.AI33TTSProvider
        return AI33TTSProvider()
    app = __import__('app.adapters.tts.elevenlabs_tts', fromlist=(
        'ElevenLabsProvider',), level=0)
    ElevenLabsProvider = app.ElevenLabsProvider
    return ElevenLabsProvider()



# NOT DECOMPILED: list_voices


# NOT DECOMPILED: preview_voice
