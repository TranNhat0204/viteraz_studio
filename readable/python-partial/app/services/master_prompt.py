# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/master_prompt.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: resolve
def resolve(config):
    if not isinstance(config, dict):
        return
    raw = config.get('script_master_prompt')
    if isinstance(raw, str):
        return raw.strip()
    return ''



# Original qualified name: build_source_packet
def build_source_packet(news_source, facts_block, idea, competitor_brief, audience_read):
    parts = []
    has_doc = False
    if not news_source:
        article = ''.strip()
    else:
        article = news_source.strip()
    if article:
        has_doc = True
        parts.append(
            '=== SOURCE DOCUMENT (published reporting — established fact) ===\n' +
            article)
    if not facts_block:
        facts = ''.strip()
    else:
        facts = facts_block.strip()
    if facts:
        has_doc = True
        parts.append('=== VERIFIED RESEARCH RECORD (established fact) ===\n' +
            facts)
        third_party = _competitor_brief_block(competitor_brief)
    else:
        third_party = _competitor_brief_block(competitor_brief)
    if third_party:
        parts.append(third_party)
        audience = _audience_read_block(audience_read)
    else:
        audience = _audience_read_block(audience_read)
    if audience:
        parts.append(audience)
        brief = _idea_brief(idea)
    else:
        brief = _idea_brief(idea)
    if brief:
        parts.append(
            """=== EPISODE BRIEF (the commission — WHICH episode to write) ===
    This brief is NOT a source of fact. It tells you which subject and angle this episode covers. Treat any proper noun, number or detail appearing ONLY here as the subject of the commission, never as a verified detail you may state on air.
    """
             + brief)
        return '\n\n'.join(parts).strip(), has_doc
    else:
        return '\n\n'.join(parts).strip(), has_doc



# NOT DECOMPILED: _audience_read_block


# NOT DECOMPILED: _competitor_brief_block


# NOT DECOMPILED: _idea_brief


# NOT DECOMPILED: render


# NOT DECOMPILED: render.<locals>._sub


# NOT DECOMPILED: parse_output


# Original qualified name: clean_script_body
def clean_script_body(script):
    app = __import__('app.core.text', fromlist=('strip_thinking_blocks',), level=0)
    strip_thinking_blocks = app.strip_thinking_blocks
    if not script:
        text = strip_thinking_blocks('')
    else:
        text = strip_thinking_blocks(script)
    out = []
    for __temp_275210 in iter(text.replace('\r', '\n').split('\n')):
        line = __temp_275210
        s = line.strip()
        if not s:
            continue
            __temp_275212 = _FENCE_LINE_RE.match(s)
        else:
            _FENCE_LINE_RE.match(s)
        if not __temp_275212:
            if not _HEADING_LINE_RE.match(s):
                if _BOLD_HEADING_RE.match(s):
                    continue
                    __temp_275216 = _STAGE_DIR_RE.match(s)
                else:
                    _STAGE_DIR_RE.match(s)
            else:
                continue
                _STAGE_DIR_RE.match(s)
        else:
            continue
            _STAGE_DIR_RE.match(s)
        if not __temp_275216:
            if s.startswith(':::'):
                continue
                s = _TIMESTAMP_RE.sub('', s).strip()
            else:
                s = _TIMESTAMP_RE.sub('', s).strip()
        else:
            continue
            s = _TIMESTAMP_RE.sub('', s).strip()
        s = _LIST_MARKER_RE.sub('', s).strip()
        s = re.sub('^\\*\\*(.*?)\\*\\*$', '\\1', s).strip()
        if not s:
            continue
            out.append(s)
        else:
            out.append(s)
        continue
    return '\n'.join(out).strip()



# Original qualified name: _clean_title
def _clean_title(s):
    if not s:
        t = ''.strip().strip('*_').strip()
    else:
        t = s.strip().strip('*_').strip()
    t = re.sub('^["“](.*)["”]$', '\\1', t).strip()
    t = re.sub('^\\[(.*)\\]$', '\\1', t).strip()
    return t



# Original qualified name: _strip_stray_markers
def _strip_stray_markers(script):
    kept = []
    if not script:
        __temp_275247 = ''.replace('\r', '\n').split('\n')
    else:
        script.replace('\r', '\n').split('\n')
    for __temp_275250 in iter(__temp_275247):
        line = __temp_275250
        s = line.strip()
        if not s:
            kept.append('')
            continue
            __temp_275253 = _END_RE.match(s)
        else:
            _END_RE.match(s)
        if not __temp_275253:
            if not _ND_RE.match(s):
                if not _TITLE_RE.match(s):
                    if _SCRIPT_RE.match(s):
                        continue
                        __temp_275258 = _REJECT_RE.match(s)
                    else:
                        _REJECT_RE.match(s)
                else:
                    continue
                    _REJECT_RE.match(s)
            else:
                continue
                _REJECT_RE.match(s)
        else:
            continue
            _REJECT_RE.match(s)
        if not __temp_275258:
            if _REASON_RE.match(s):
                continue
                kept.append(line)
            else:
                kept.append(line)
        else:
            continue
            kept.append(line)
        continue
    return '\n'.join(kept).strip()



# NOT DECOMPILED: _channel_identity


# Original qualified name: build_user_message
def build_user_message(source_packet, has_documented_source, attach_source, language, target_sec, is_short, channel_niche, channel_brief, channel_orientation, niche_angle, channel_hook, has_competitor_brief, cast_block):
    parts = [
        """TASK: Execute your PRODUCTION MASTER PROMPT above on the material supplied in it, and return the result in your STRICT OUTPUT FORMAT — nothing else.
    """
        ]
    if attach_source:
        if not source_packet:
            __temp_275284 = ''.strip()
        else:
            source_packet.strip()
        if not __temp_275284:
            parts.append('=== MATERIAL START ===\n' +
                '(no source material was supplied)' + """
    === MATERIAL END ===
    """)
            identity = _channel_identity(channel_niche, channel_brief,
                channel_orientation, niche_angle)
        else:
            parts.append('=== MATERIAL START ===\n' + __temp_275284 +
                '\n=== MATERIAL END ===\n')
            identity = _channel_identity(channel_niche, channel_brief,
                channel_orientation, niche_angle)
    else:
        identity = _channel_identity(channel_niche, channel_brief,
            channel_orientation, niche_angle)
    if identity:
        parts.append(identity)
    if not cast_block:
        __temp_275292 = ''.strip()
    else:
        cast_block.strip()
    if __temp_275292:
        parts.append(cast_block)
    if not has_documented_source:
        if has_competitor_brief:
            parts.append(
                """SOURCE NOTE: no primary document was supplied. What you have is a TOPIC RECORD taken from another creator's video — unverified. Write the episode, but hold this line: any specific you cannot stand behind must be attributed ('theo hồ sơ được công bố…', 'các bản tin thời điểm đó cho biết…') or left out. Prefer a shorter, narrower episode you can defend over a full-length one padded with unverified specifics. Never present an unconfirmed name, date or figure as settled fact.
    """
                )
        elif not has_documented_source:
            parts.append(
                """SOURCE NOTE: no published document or verified research record was supplied for this episode — only the commission brief. Apply your own source gate honestly: if your instructions require documented material and none is present, REJECT rather than inventing material to fill the runtime.
    """
                )
    elif not has_documented_source:
        parts.append(
            """SOURCE NOTE: no published document or verified research record was supplied for this episode — only the commission brief. Apply your own source gate honestly: if your instructions require documented material and none is present, REJECT rather than inventing material to fill the runtime.
    """
            )
    if not language:
        lang_code = 'en'.strip()
    else:
        lang_code = language.strip()
    parts.append(
        "OUTPUT LANGUAGE: write TITLE, SCRIPT and NARRATION DIRECTION entirely in language code '"
         + str(lang_code) + "'.\n")
    if target_sec:
        minutes = max(1, round(target_sec / 60))
        words = int(target_sec * 2.5)
        parts.append(
            "RUNTIME LENGTH TARGET (set by this channel's owner — this SUPERSEDES the target length stated in your instructions above): about "
             + str(minutes) + ' minute(s) spoken, roughly ' + str(words) +
            """ words. Keep every other rule — beat architecture, brand placement, fact discipline and the final audit — exactly as written; compress or expand the beats to fit this runtime, and never pad with invented material to reach it.
    """
            )
        if is_short:
            parts.append(
                """This channel is producing a SHORT vertical video at that runtime. Your instructions are written for long form: keep the register, the fact discipline and the signature beat, but deliver ONE idea with a single-line hook and a resolved ending.
    """
                )
    if not channel_hook:
        hook = ''.strip()
    else:
        hook = channel_hook.strip()
    if hook:
        parts.append(
            """CHANNEL SIGNATURE LINE (fixed branding line — reproduce it VERBATIM once, placed according to the brand-placement rules in your instructions above; never in the opening seconds if those rules forbid it):
    \""""
             + str(hook) + '"\n')
        parts.append(
            """NARRATION IS READ ALOUD BY A TTS ENGINE: spell every number, currency amount, percentage and symbol out in full words in the output language. Never emit raw digits or the characters $ % € £ & / in the SCRIPT section.
    """
            )
        return '\n'.join(parts)
    else:
        parts.append(
            """NARRATION IS READ ALOUD BY A TTS ENGINE: spell every number, currency amount, percentage and symbol out in full words in the output language. Never emit raw digits or the characters $ % € £ & / in the SCRIPT section.
    """
            )
        return '\n'.join(parts)



# Original qualified name: debug_summary
def debug_summary(rendered, has_documented_source):
    payload = {chars: len(rendered.prompt), source_slot: rendered.
        source_injected, name_slots: rendered.channel_name_slots,
        documented_source: has_documented_source}
    if rendered.extra_source_slots:
        payload['extra_source_slots'] = rendered.extra_source_slots
    return json.dumps(payload, ensure_ascii=False)



# NOT DECOMPILED: skill_text


# NOT DECOMPILED: _channel_facts


# NOT DECOMPILED: build_generate_messages


# Original qualified name: build_refine_messages
def build_refine_messages(current, instruction, language):
    if not language:
        system = (
            """Bạn là biên tập viên PRODUCTION MASTER PROMPT. Người dùng đưa bạn một master prompt đang chạy và một yêu cầu sửa. Sửa ĐÚNG phần được yêu cầu, giữ nguyên mọi phần khác.
    
    VÙNG CẤM SỬA — giữ nguyên từng ký tự, kể cả khi yêu cầu là 'rút ngắn' hay 'gọn lại':
    - Vùng nhận nguồn: {{CHANNEL_NAME}}, {{SOURCE_MATERIAL}} và hai marker '=== SOURCE START ===' / '=== SOURCE END ==='.
    - Mục STRICT OUTPUT FORMAT với đủ bốn dòng: 'TITLE:', 'SCRIPT:', '--- END OF SCRIPT ---', 'NARRATION DIRECTION:'.
    - Luật đọc thành tiếng (số viết thành chữ, không ký hiệu, SCRIPT chỉ có lời đọc).
    Đây là hợp đồng kỹ thuật với phần mềm; xoá là hỏng cả dây chuyền.
    
    Trả về DUY NHẤT master prompt đã sửa, bằng ngôn ngữ """
             + str('vi') +
            '. Không lời dẫn, không giải thích, không bọc trong khối code.')
    else:
        system = (
            """Bạn là biên tập viên PRODUCTION MASTER PROMPT. Người dùng đưa bạn một master prompt đang chạy và một yêu cầu sửa. Sửa ĐÚNG phần được yêu cầu, giữ nguyên mọi phần khác.
    
    VÙNG CẤM SỬA — giữ nguyên từng ký tự, kể cả khi yêu cầu là 'rút ngắn' hay 'gọn lại':
    - Vùng nhận nguồn: {{CHANNEL_NAME}}, {{SOURCE_MATERIAL}} và hai marker '=== SOURCE START ===' / '=== SOURCE END ==='.
    - Mục STRICT OUTPUT FORMAT với đủ bốn dòng: 'TITLE:', 'SCRIPT:', '--- END OF SCRIPT ---', 'NARRATION DIRECTION:'.
    - Luật đọc thành tiếng (số viết thành chữ, không ký hiệu, SCRIPT chỉ có lời đọc).
    Đây là hợp đồng kỹ thuật với phần mềm; xoá là hỏng cả dây chuyền.
    
    Trả về DUY NHẤT master prompt đã sửa, bằng ngôn ngữ """
             + str(language) +
            '. Không lời dẫn, không giải thích, không bọc trong khối code.')
    if not instruction:
        __temp_275355 = ''.strip()
    else:
        instruction.strip()
    if not current:
        user = ('YÊU CẦU SỬA:\n' + __temp_275355 +
            '\n\n=== MASTER PROMPT HIỆN TẠI ===\n' + ''.strip() + '\n=== HẾT ===')
    else:
        user = ('YÊU CẦU SỬA:\n' + __temp_275355 +
            '\n\n=== MASTER PROMPT HIỆN TẠI ===\n' + current.strip() +
            '\n=== HẾT ===')
    return system, user



# Original qualified name: validate_generated
def validate_generated(text):
    if not text:
        body = ''.strip()
    else:
        body = text.strip()
    issues = []
    if len(body) < MIN_MASTER_CHARS:
        issues.append('quá ngắn (' + str(len(body)) +
            ' ký tự) — không giống một master prompt sản xuất')
    for __temp_275365 in iter(_REQUIRED_MARKERS):
        marker = __temp_275365
        if not marker not in body:
            continue
            issues.append('thiếu marker hợp đồng output: ' + repr(marker))
        else:
            issues.append('thiếu marker hợp đồng output: ' + repr(marker))
        continue
    for __temp_275368 in iter(_REQUIRED_PLACEHOLDERS):
        ph = __temp_275368
        if not ph not in body:
            continue
            issues.append('thiếu placeholder ' + str(ph) +
                ' — phần mềm không điền được tên kênh')
        else:
            issues.append('thiếu placeholder ' + str(ph) +
                ' — phần mềm không điền được tên kênh')
        continue
    if not _PLACEHOLDER_RE.search(body.replace('{{CHANNEL_NAME}}', '')):
        issues.append(
            'thiếu placeholder nguồn (vd {{SOURCE_MATERIAL}}) — không có chỗ nhận bài báo/hồ sơ'
            )
        return issues
    else:
        return issues



# NOT DECOMPILED: strip_wrapper


# NOT DECOMPILED: run_generate_job


# Original qualified name: run_generate_job.<locals>.checkpoint
def checkpoint(pct):
    nonlocal E, StudioError, cancel_check, progress
    if cancel_check:
        if cancel_check():
            raise StudioError(E.CANCELLED, 'Đã huỷ tạo master prompt.')
    if progress:
        progress(pct)
        return None
    return None



# Original qualified name: undo
def undo(db, project_id):
    app = __import__('app.core.errors', fromlist=('StudioError', 'E'), level=0)
    StudioError = app.StudioError
    E = app.E
    app = __import__('app.services', fromlist=('ai_studio_service',), level=0)
    ai_studio_service = app.ai_studio_service
    cfg = ai_studio_service.get_or_create_config(db, project_id)
    profile = ai_studio_service._loads(cfg.channel_profile_json, {})
    __temp_275460 = profile.get('script_master_prompt_prev')
    if not __temp_275460:
        prev = str('').strip()
    else:
        prev = str(__temp_275460).strip()
    if not prev:
        raise StudioError(E.PRECONDITION_MISSING,
            'Không có bản trước để hoàn tác.', status_code=409)
    __temp_275466 = profile.get('script_master_prompt')
    if not __temp_275466:
        profile['script_master_prompt_prev'] = str('').strip()
    else:
        profile['script_master_prompt_prev'] = str(__temp_275466).strip()
    profile['script_master_prompt'] = prev
    cfg.channel_profile_json = json.dumps(profile, ensure_ascii=False)
    db.commit()
    return {script_master_prompt: prev, chars: len(prev)}

