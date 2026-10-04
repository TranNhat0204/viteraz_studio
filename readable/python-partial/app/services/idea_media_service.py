# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/idea_media_service.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _now_iso
def _now_iso():
    return datetime.now(timezone.utc).isoformat()



# NOT DECOMPILED: is_generating


# NOT DECOMPILED: clear_stale_generating


# Original qualified name: _slug
def _slug(s, n):
    return _slugify(s, n, default='x')



# Original qualified name: _norm_name
def _norm_name(s):
    if not s:
        return ''.strip().lower()
    else:
        return s.strip().lower()



# Original qualified name: _reuse_existing_portrait
def _reuse_existing_portrait(existing, force, is_host, source):
    if existing:
        if not Path(existing).is_file():
            return False
    else:
        return False
    if is_placeholder(existing):
        return False
    if not is_host:
        if not source:
            locked_identity = ''.strip().lower() in frozenset({'uploaded',
                'import', 'user'})
        else:
            locked_identity = source.strip().lower() in frozenset({'uploaded',
                'import', 'user'})
    else:
        locked_identity = is_host
    if not not force:
        return locked_identity
    else:
        return not force



# Original qualified name: _with_host_identity
def _with_host_identity(prompt, host_info):
    if not host_info:
        return prompt
    __temp_273219 = host_info.get('name')
    if not __temp_273219:
        __temp_273221 = str('Host').strip()
    else:
        str(__temp_273219).strip()
    if not __temp_273221:
        name = 'Host'
    else:
        name = __temp_273221
    __temp_273224 = host_info.get('description')
    if not __temp_273224:
        host_desc = str('').strip()
    else:
        host_desc = str(__temp_273224).strip()
    if host_desc:
        identity = " The host's locked appearance is: " + str(host_desc) + '.'
    else:
        identity = ''
    return 'IDENTITY LOCK: the attached reference image is ' + str(name
        ) + ', the channel host. Preserve the same recognizable face, facial geometry, hair, skin tone, body proportions and signature outfit; do not replace, redesign, silhouette, mask, or anonymize this person. Feature ' + str(
        name) + ' as the large, clear foreground subject.' + str(identity
        ) + ' ' + prompt



# NOT DECOMPILED: _thumbnail_character_refs


# NOT DECOMPILED: _prompt_misses_anyone


# NOT DECOMPILED: _recompose_thumbnail_prompt


# NOT DECOMPILED: _with_cast_identity


# NOT DECOMPILED: schedule_idea_media


# Original qualified name: is_inflight
def is_inflight(idea_id):
    task = _INFLIGHT.get(idea_id)
    if task is not None:
        return not task.done()
    else:
        return task is not None



# NOT DECOMPILED: _set_generating


# NOT DECOMPILED: _safe_generate


# NOT DECOMPILED: generate_idea_media


# NOT DECOMPILED: _one_image


# NOT DECOMPILED: generate_portrait_image


# NOT DECOMPILED: _loads


# Original qualified name: _asset_label
def _asset_label(path, provider, entity_id, entity_key, slot, prompt, extra):
    raw = str(provider) + ':' + str(entity_id) + ':' + str(slot) + ':' + str(prompt
        ).encode('utf-8', 'ignore')
    label = {'path': path, 'provider': provider, entity_key: entity_id, 'slot':
        slot, 'request_id': hashlib.sha256(raw).hexdigest()[None:16]}
    if extra:
        label.update(extra)
        return label
    else:
        return label

