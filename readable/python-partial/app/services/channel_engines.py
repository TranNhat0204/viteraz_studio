# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/channel_engines.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _slugify
def _slugify(s):
    if not s:
        __temp_268888 = re.sub('[^a-z0-9]+', '-', ''.strip().lower()).strip('-')
    else:
        re.sub('[^a-z0-9]+', '-', s.strip().lower()).strip('-')
    if not __temp_268888:
        return 'niche'
    else:
        return __temp_268888



# NOT DECOMPILED: _norm_niches


# NOT DECOMPILED: ChannelEngine.summary


# Original qualified name: ChannelEngine.detail
def detail(self):
    __temp_269012 = {}
    __temp_269012.update(self.summary())
    __temp_269014 = __temp_269012
    __temp_269014.update({meta: self.meta, body: self.body})
    return __temp_269014



# NOT DECOMPILED: cast_policy


# NOT DECOMPILED: cast_policy.<locals>._integer


# Original qualified name: ensure_style_contract
def ensure_style_contract(prompt, engine, lang):
    if not prompt:
        text = re.sub('\\s+', ' ', str('')).strip()
    else:
        text = re.sub('\\s+', ' ', str(prompt)).strip()
    if engine is None:
        return text
    if not engine.meta:
        meta = {}
    else:
        meta = engine.meta
    legacy_fragments = meta.get('legacy_style_fragments')
    if isinstance(legacy_fragments, list):
        for __temp_269043 in iter(legacy_fragments):
            fragment = __temp_269043
            if not fragment:
                old = str('').strip()
            else:
                old = str(fragment).strip()
            if not old:
                continue
                text = re.sub(re.escape(old), ' ', text, flags=re.IGNORECASE)
            else:
                text = re.sub(re.escape(old), ' ', text, flags=re.IGNORECASE)
            continue
        legacy_replacements = meta.get('legacy_prompt_replacements')
    else:
        legacy_replacements = meta.get('legacy_prompt_replacements')
    if isinstance(legacy_replacements, dict):
        for __temp_269056 in iter(legacy_replacements.items()):
            __temp_269057, __temp_269058 = __temp_269056
            old_raw = __temp_269057
            new_raw = __temp_269058
            if not old_raw:
                old = str('').strip()
            else:
                old = str(old_raw).strip()
            if not old:
                continue
                __temp_269063 = re.escape(old)
            else:
                re.escape(old)
            if not new_raw:
                text = re.sub(__temp_269063, str('').strip(), text, flags=re.
                    IGNORECASE)
            else:
                text = re.sub(__temp_269063, str(new_raw).strip(), text, flags=
                    re.IGNORECASE)
            continue
        text = re.sub('\\s+', ' ', text).strip(' ,')
    else:
        text = re.sub('\\s+', ' ', text).strip(' ,')
    __temp_269075 = meta.get('style_anchor')
    if not __temp_269075:
        en_anchor = str('').strip()
    else:
        en_anchor = str(__temp_269075).strip()
    __temp_269080 = meta.get('style_lock')
    if not __temp_269080:
        en_lock = str('').strip()
    else:
        en_lock = str(__temp_269080).strip()
    __temp_269085 = meta.get('style_anchor_vi')
    if not __temp_269085:
        vi_anchor = str('').strip()
    else:
        vi_anchor = str(__temp_269085).strip()
    __temp_269090 = meta.get('style_lock_vi')
    if not __temp_269090:
        vi_lock = str('').strip()
    else:
        vi_lock = str(__temp_269090).strip()
    if not lang:
        is_vi = ''.lower().startswith('vi')
    else:
        is_vi = lang.lower().startswith('vi')
    if is_vi:
        if not vi_anchor:
            anchor = en_anchor
        else:
            anchor = vi_anchor
        if not vi_lock:
            lock = en_lock
        else:
            lock = vi_lock
        if vi_anchor:
            if en_anchor:
                if en_anchor.lower() in text.lower():
                    text = re.sub(re.escape(en_anchor), '', text, flags=re.
                        IGNORECASE).strip(' ,')
        if vi_lock:
            if en_lock:
                if en_lock.lower() in text.lower():
                    text = re.sub(re.escape(en_lock), '', text, flags=re.IGNORECASE
                        ).strip(' ,')
    else:
        anchor = en_anchor
        lock = en_lock
        if vi_anchor:
            if vi_anchor.lower() in text.lower():
                text = re.sub(re.escape(vi_anchor), '', text, flags=re.IGNORECASE
                    ).strip(' ,')
        if vi_lock:
            if vi_lock.lower() in text.lower():
                text = re.sub(re.escape(vi_lock), '', text, flags=re.IGNORECASE
                    ).strip(' ,')
    text = re.sub('\\s+', ' ', text).strip(' ,')
    if anchor:
        if anchor.lower() not in text.lower():
            text = str(anchor) + ' ' + str(_drop_contract_clauses(text, anchor)
                ).strip()
    if lock:
        if lock.lower() not in text.lower():
            text = str(_drop_contract_clauses(text, lock).rstrip()) + ' ' + str(
                lock).strip()
    return text



# NOT DECOMPILED: _drop_contract_clauses


# Original qualified name: portrait_aspect
def portrait_aspect(engine, chosen):
    app = __import__('app.services', fromlist=('video_format',), level=0)
    video_format = app.video_format
    vfmt = video_format
    key = vfmt.normalize(chosen)
    if key:
        return vfmt.aspect_for(key)
    if engine:
        __temp_269150 = engine.meta.get('aspect_ratio')
    if not __temp_269150:
        fallback = str('').strip()
    else:
        fallback = str(__temp_269150).strip()
    if fallback in ('16:9', '9:16'):
        return fallback
    return '16:9'



# NOT DECOMPILED: portrait_prompt


# NOT DECOMPILED: character_identity_block


# Original qualified name: _quoted_or_main
def _quoted_or_main(name):
    if not name:
        name = ''.strip()
    else:
        name = name.strip()
    if name:
        return '"' + str(name) + '"'
    return 'the main character of this video'



# NOT DECOMPILED: portrait_from_reference_prompt


# Original qualified name: _marketing_ready
def _marketing_ready(raw):
    if not isinstance(raw, dict):
        return False
    __temp_269220 = raw.get('pillars')
    if __temp_269220:
        __temp_269221 = raw.get('objectives')
        if __temp_269221:
            __temp_269222 = raw.get('formats')
            if __temp_269222:
                __temp_269224 = isinstance(raw.get('hook_bank'), dict)
                if __temp_269224:
                    return bool(raw['hook_bank'].get('types'))
                else:
                    return bool(__temp_269224)
            else:
                return bool(__temp_269222)
        else:
            return bool(__temp_269221)
    else:
        return bool(__temp_269220)



# NOT DECOMPILED: _marketing_pillars


# NOT DECOMPILED: _parse_engine_file


# NOT DECOMPILED: apply_server_overlay


# Original qualified name: clear_server_overlay
def clear_server_overlay():
    global _server_overlay
    _server_overlay = {}
    return None



# Original qualified name: _load_all
def _load_all():
    engines = {}
    if not ENGINES_DIR.is_dir():
        log.warning('[channel_engines] thư mục không tồn tại: ' + str(ENGINES_DIR))
        return engines
    for __temp_269363 in iter(sorted(ENGINES_DIR.glob('*.md'))):
        path = __temp_269363
        if path.name.startswith('_'):
            continue
            eng = _parse_engine_file(path)
        else:
            eng = _parse_engine_file(path)
        if eng is None:
            continue
        if eng.id in engines:
            log.warning("[channel_engines] trùng id '" + str(eng.id) + "' (" +
                str(path.name) + ') — ghi đè')
            engines[eng.id] = eng
        else:
            engines[eng.id] = eng
        continue
    return engines



# Original qualified name: reload
def reload():
    global _cache
    _cache = _load_all()
    return None



# Original qualified name: _engines
def _engines():
    global _cache
    if _cache is None:
        _cache = _load_all()
    if _server_overlay:
        __temp_269371 = {}
        __temp_269371.update(_cache)
        __temp_269372 = __temp_269371
        __temp_269372.update(_server_overlay)
        return __temp_269372
    return _cache



# Original qualified name: list_engines
def list_engines():
    def __temp_269375(e):
        return e.order, e.id
    
    
    return sorted(_engines().values(), key=__temp_269375)



# Original qualified name: get_engine
def get_engine(engine_id):
    __temp_269377 = _engines()
    if not engine_id:
        return __temp_269377.get(''.strip())
    else:
        return __temp_269377.get(engine_id.strip())



# Original qualified name: bundle_engine
def bundle_engine(engine_id):
    global _cache
    if _cache is None:
        _cache = _load_all()
    if not engine_id:
        return _cache.get(''.strip())
    else:
        return _cache.get(engine_id.strip())



# NOT DECOMPILED: stock_bank


# NOT DECOMPILED: content_tokens


# NOT DECOMPILED: build_stock_queries
