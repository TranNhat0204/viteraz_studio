# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/audio_story_service.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _fs_get
def _fs_get(path):
    url = str(FIRESTORE_BASE) + '/' + str(path) + '?key=' + str(API_KEY)
    r = requests.get(url, headers=HEADERS, timeout=15)
    r.raise_for_status()
    return r.json()



# Original qualified name: _fs_list
def _fs_list(collection_path):
    url = str(FIRESTORE_BASE) + '/' + str(collection_path) + '?key=' + str(API_KEY)
    r = requests.get(url, headers=HEADERS, timeout=30)
    r.raise_for_status()
    return r.json()



# NOT DECOMPILED: _fs_doc_to_dict


# NOT DECOMPILED: _next_flight_objects


# NOT DECOMPILED: _normalize_site_story


# Original qualified name: _stories_from_site_html
def _stories_from_site_html(page_html):
    deduped = {}
    for __temp_267390 in iter(_next_flight_objects(page_html)):
        raw = __temp_267390
        story = _normalize_site_story(raw)
        if not story:
            continue
            deduped[story['id']] = story
        else:
            deduped[story['id']] = story
        continue
    return list(deduped.values())



# NOT DECOMPILED: _fetch_site_stories


# NOT DECOMPILED: _fetch_site_story


# Original qualified name: _decode_html_entities
def _decode_html_entities(text):
    if not text:
        return
    return html.unescape(text)



# NOT DECOMPILED: clean_vietnamese_text


# NOT DECOMPILED: _repair_split_vietnamese_syllables


# NOT DECOMPILED: _repair_split_vietnamese_syllables.<locals>.replace


# Original qualified name: _clean_story_paragraphs
def _clean_story_paragraphs(values):
    cleaned = []
    seen = set()
    for __temp_267435 in iter(values):
        value = __temp_267435
        if not value:
            text = clean_vietnamese_text(str(''))
        else:
            text = clean_vietnamese_text(str(value))
        text = _WATERMARK_RE.sub(' ', text)
        text = re.sub('\\s+', ' ', text).strip()
        if not len(text) < 12:
            if 'meocammap.com' in text.lower():
                continue
                key = re.sub('\\W+', '', text, flags=re.UNICODE).lower()
            else:
                key = re.sub('\\W+', '', text, flags=re.UNICODE).lower()
        else:
            continue
            key = re.sub('\\W+', '', text, flags=re.UNICODE).lower()
        if key:
            if key in seen:
                continue
                seen.add(key)
                cleaned.append(text)
            else:
                seen.add(key)
                cleaned.append(text)
        else:
            continue
            seen.add(key)
            cleaned.append(text)
        continue
    return cleaned



# NOT DECOMPILED: _valid_chapter_content


# Original qualified name: _strip_html
def _strip_html(text):
    text = re.sub('<br\\s*/?>', '\n', text, flags=re.IGNORECASE)
    text = re.sub('<p[^>]*>', '', text, flags=re.IGNORECASE)
    text = re.sub('</p>', '\n', text)
    text = re.sub('<[^>]+>', '', text)
    text = clean_vietnamese_text(text)
    return text.strip()



# NOT DECOMPILED: _node_bridge_path


# NOT DECOMPILED: _node_call


# Original qualified name: _node_chapters
def _node_chapters(story_id):
    data = _node_call('list_chapters', story_id)
    if data:
        if data.get('ok'):
            return data.get('chapters', [])
    return []



# Original qualified name: _node_chapter_content
def _node_chapter_content(story_id, chapter_id):
    data = _node_call('get_chapter', story_id, chapter_id)
    if data:
        if not data.get('ok'):
            return None
    else:
        return None
    ch = data.get('chapter', {})
    content_html = ch.get('content', '')
    content_text = _decode_html_entities(content_html)
    content_text = _strip_html(content_text)
    paragraphs = _clean_story_paragraphs(content_text.split('\n'))
    result = {id: chapter_id, title: ch.get('title', 'Chương ' + str(ch.get(
        'no', chapter_id))), no: ch.get('no', 0), content: paragraphs,
        content_text: '\n\n'.join(paragraphs)}
    if _valid_chapter_content(result):
        return result
    return None



# Original qualified name: list_sources
def list_sources():
    return [{id: 'truyenchutm', name: 'Truyện Chữ TM', description:
        'Kho truyện chữ phong phú từ meocammap.com / truyenchutm.com', url:
        SITE_BASE}]



# NOT DECOMPILED: list_stories


# Original qualified name: parse_story_id
def parse_story_id(url_or_id):
    url = url_or_id.strip()
    if not '/' in url:
        if 'http' in url:
            m = re.search('/read/([\\w-]+)/([\\w-]+)', url)
            if m:
                return m.group(1), m.group(2)
            m = re.search('/stories/([\\w-]+)', url)
            if m:
                return m.group(1), None
            m = re.search('/story/([\\w-]+)', url)
            if m:
                return m.group(1), None
    else:
        m = re.search('/read/([\\w-]+)/([\\w-]+)', url)
        if m:
            return m.group(1), m.group(2)
        m = re.search('/stories/([\\w-]+)', url)
        if m:
            return m.group(1), None
        m = re.search('/story/([\\w-]+)', url)
        if m:
            return m.group(1), None
    return url, None



# NOT DECOMPILED: preview_story


# NOT DECOMPILED: get_chapter_content


# Original qualified name: _node_chapters_batch
def _node_chapters_batch(story_id, chapter_ids):
    timeout = min(300, max(90, 25 * len(chapter_ids) + 30))
    __temp_267663 = ['get_chapters_batch', story_id]
    __temp_267663.extend(chapter_ids)
    data = _node_call(*tuple(__temp_267663), **{'timeout': timeout})
    if data:
        if not data.get('ok'):
            return []
    else:
        return []
    out = []
    for __temp_267672 in iter(data.get('chapters', [])):
        ch = __temp_267672
        paragraphs = ch.get('paragraphs')
        if not paragraphs:
            content_html = ch.get('content', '')
            content_text = _decode_html_entities(content_html)
            content_text = _strip_html(content_text)
            paragraphs = content_text.split('\n')
        if not paragraphs:
            paragraphs = _clean_story_paragraphs([])
        else:
            paragraphs = _clean_story_paragraphs(paragraphs)
        result = {id: ch.get('id'), title: ch.get('title', 'Chương'), no: ch.
            get('no', 0), content: paragraphs, content_text: '\n\n'.join(
            paragraphs)}
        if not _valid_chapter_content(result):
            continue
            out.append(result)
        else:
            out.append(result)
        continue
    return out



# NOT DECOMPILED: _load_selected_chapters


# NOT DECOMPILED: _compose_chapter_source


# NOT DECOMPILED: _near_duplicate_chapter_pairs


# NOT DECOMPILED: _chapter_number


# Original qualified name: _chapter_heading
def _chapter_heading(chapter, index):
    number = _chapter_number(chapter, index)
    __temp_267766 = chapter.get('title')
    if not __temp_267766:
        title = clean_vietnamese_text('')
    else:
        title = clean_vietnamese_text(__temp_267766)
    if title:
        if re.fullmatch('chương\\s*0*' + str(number), title, flags=re.IGNORECASE):
            return 'Chương ' + str(number)
    else:
        return 'Chương ' + str(number)
    title = re.sub('^chương\\s*0*' + str(number) + '\\s*[:.\\-–—]?\\s*', '',
        title, flags=re.IGNORECASE).strip()
    if title:
        return 'Chương ' + str(number) + ': ' + str(title)
    return 'Chương ' + str(number)



# NOT DECOMPILED: _assemble_structured_summary


# NOT DECOMPILED: _summary_is_usable


# Original qualified name: _fallback_story_script
def _fallback_story_script(chapters, story_title, target_words):
    intro = 'Sau đây là phần tóm tắt theo từng chương của truyện ' + str(
        story_title
        ) + '. Các diễn biến được kể lại theo đúng thứ tự của nguyên tác.'
    char_budget = max(800, int(target_words * 7 / max(1, len(chapters))))
    sections = []
    for __temp_267840 in iter(enumerate(chapters)):
        __temp_267841, __temp_267842 = __temp_267840
        index = __temp_267841
        chapter = __temp_267842
        __temp_267843 = chapter.get('content')
        if not __temp_267843:
            body = ' '.join(_clean_story_paragraphs([]))
        else:
            body = ' '.join(_clean_story_paragraphs(__temp_267843))
        clipped = body[None:char_budget].rsplit(' ', 1)[0].strip()
        sections.append(str(_chapter_heading(chapter, index)) + ':\n' + str(
            clipped))
        continue
    outro = (
        'Phần truyện của tập này kết thúc tại đây. Những diễn biến tiếp theo sẽ được tiếp tục ở tập sau.'
        )
    __temp_267854 = [intro]
    __temp_267854.extend(sections)
    __temp_267854.append('Kết tập:\n' + str(outro))
    return '\n\n'.join(__temp_267854)



# Original qualified name: _chapter_source_excerpt
def _chapter_source_excerpt(chapter, max_chars):
    __temp_267856 = chapter.get('content')
    if not __temp_267856:
        body = '\n\n'.join(_clean_story_paragraphs([]))
    else:
        body = '\n\n'.join(_clean_story_paragraphs(__temp_267856))
    if len(body) <= max_chars:
        return body
    head_size = int(max_chars * 0.42)
    middle_size = int(max_chars * 0.16)
    tail_size = max_chars - head_size - middle_size
    middle_at = max(head_size, len(body) // 2 - middle_size // 2)
    return body[None:head_size].rsplit(' ', 1)[0].strip(
        ) + """
    
    [... phần chuyển tiếp giữa chương đã được rút gọn ...]
    
    """ + body[
        middle_at:middle_at + middle_size].strip(
        ) + """
    
    [... phần chuyển tiếp cuối chương đã được rút gọn ...]
    
    """ + body[
        -tail_size:None].lstrip().split(' ', 1)[-1].strip()



# NOT DECOMPILED: _chapter_word_budgets


# Original qualified name: _episode_summary_brief
def _episode_summary_brief(chapter_summaries, max_chars):
    if not chapter_summaries:
        return
    per_chapter = max(220, max_chars // len(chapter_summaries))
    blocks = []
    for __temp_267887 in iter(chapter_summaries):
        section = __temp_267887
        __temp_267888 = section.get('narration')
        if not __temp_267888:
            narration = clean_vietnamese_text(str(''))
        else:
            narration = clean_vietnamese_text(str(__temp_267888))
        if len(narration) > per_chapter:
            half = max(100, per_chapter // 2)
            narration = narration[None:half].rsplit(' ', 1)[0
                ] + ' ... ' + narration[-half:None].split(' ', 1)[-1]
        blocks.append('Chương ' + str(section.get('chapter_no')) + ': ' + str(
            narration))
        continue
    return '\n\n'.join(blocks)



# NOT DECOMPILED: _character_name_key


# NOT DECOMPILED: _clean_character_entry


# NOT DECOMPILED: _extract_chapter_characters


# NOT DECOMPILED: _merge_character_bible_fallback


# NOT DECOMPILED: _build_character_bible


# NOT DECOMPILED: _character_bible_prompt


# Original qualified name: _canonicalize_character_names
def _canonicalize_character_names(text, bible):
    result = text
    replacements = []
    for __temp_268016 in iter(bible):
        character = __temp_268016
        __temp_268017 = character.get('name')
        if not __temp_268017:
            canonical = str('').strip()
        else:
            canonical = str(__temp_268017).strip()
        if not character.get('aliases'):
            __temp_268023 = []
        for __temp_268024 in iter(__temp_268023):
            alias = __temp_268024
            if not alias:
                continue
                __temp_268025 = _character_name_key(alias)
                __temp_268026 = _character_name_key(canonical)
            else:
                _character_name_key(alias)
                _character_name_key(canonical)
            if not __temp_268025 != __temp_268026:
                continue
                replacements.append((str(alias), canonical))
            else:
                replacements.append((str(alias), canonical))
            continue
        continue
    
    
    def __temp_268033(pair):
        return len(pair[0])
    
    
    for __temp_268036 in iter(sorted(replacements, key=__temp_268033, reverse=True)
        ):
        __temp_268037, __temp_268038 = __temp_268036
        alias = __temp_268037
        canonical = __temp_268038
        result = re.sub('(?<!\\w)' + str(re.escape(alias)) + '(?!\\w)',
            canonical, result, flags=re.IGNORECASE)
        continue
    return result



# NOT DECOMPILED: _story_cast_for_payload


# Original qualified name: _character_name_lookup
def _character_name_lookup(bible):
    lookup = {}
    for __temp_268077 in iter(bible):
        character = __temp_268077
        __temp_268078 = character.get('name')
        if not __temp_268078:
            canonical = str('').strip()
        else:
            canonical = str(__temp_268078).strip()
        __temp_268083 = [canonical]
        __temp_268084 = character.get('aliases')
        if not __temp_268084:
            __temp_268086 = __temp_268083
            __temp_268086.extend([])
        else:
            __temp_268083.extend(__temp_268084)
        for __temp_268088 in iter(__temp_268086):
            value = __temp_268088
            if not value:
                continue
                lookup[_character_name_key(str(value))] = canonical
            else:
                lookup[_character_name_key(str(value))] = canonical
            continue
        continue
    return lookup



# Original qualified name: _canonical_character_list
def _canonical_character_list(values, bible, heading):
    lookup = _character_name_lookup(bible)
    present = []
    unknown = []
    for __temp_268096 in iter(values):
        raw_name = __temp_268096
        if not raw_name:
            raw_name = clean_vietnamese_text(str(''))
        else:
            raw_name = clean_vietnamese_text(str(raw_name))
        if not raw_name:
            continue
            canonical = lookup.get(_character_name_key(raw_name))
        else:
            canonical = lookup.get(_character_name_key(raw_name))
        if not canonical:
            unknown.append(raw_name)
            continue
        if not canonical not in present:
            continue
            present.append(canonical)
        else:
            present.append(canonical)
        continue
    if unknown:
        raise ValueError(str(heading) +
            ' dùng nhân vật ngoài Character Bible: ' + str(unknown))
    return present



# NOT DECOMPILED: _plan_remix_chapter


# NOT DECOMPILED: _build_remix_blueprint


# NOT DECOMPILED: _remix_prose_issues


# NOT DECOMPILED: _has_long_source_phrase


# Original qualified name: _has_long_source_phrase.<locals>.tokens
def tokens(value):
    return re.findall('\\w+', clean_vietnamese_text(value).lower(), flags=re.
        UNICODE)



# NOT DECOMPILED: _write_remix_story_chapter


# NOT DECOMPILED: _summarize_story_chapter


# NOT DECOMPILED: _continuity_polish_chapters


# NOT DECOMPILED: _build_episode_frame


# NOT DECOMPILED: _build_story_thumbnail_fields


# NOT DECOMPILED: _run_background_summarize_impl


# Original qualified name: _run_background_summarize_impl.<locals>.checkpoint
def checkpoint(percent):
    nonlocal action_label, cancel_check, progress
    if cancel_check:
        if cancel_check():
            raise StudioError(E.CANCELLED, 'Đã huỷ tác vụ ' + str(action_label) +
                ' truyện.')
    if progress:
        progress(percent)
        return None
    return None



# NOT DECOMPILED: _run_background_summarize_impl.<locals>.extract_cast_one


# NOT DECOMPILED: _run_background_summarize_impl.<locals>.plan_one


# NOT DECOMPILED: _run_background_summarize_impl.<locals>.summarize_one


# NOT DECOMPILED: run_queued_audio_story_summary


# NOT DECOMPILED: summarize_and_import
