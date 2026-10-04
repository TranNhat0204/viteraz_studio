# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/export_service.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: lang_folder
def lang_folder(lang):
    if not lang:
        code = ''.lower()
    else:
        code = lang.lower()
    if not lang:
        return _LANG_FOLDER.get(code, 'xx'.upper())
    else:
        return _LANG_FOLDER.get(code, lang.upper())



# NOT DECOMPILED: _transcript_text


# NOT DECOMPILED: ensure_seo


# Original qualified name: folder_name
def folder_name(seo, v):
    __temp_271357 = seo.get('titles')
    if not __temp_271357:
        titles = []
    else:
        titles = __temp_271357
    name = ''
    if titles:
        __temp_271359 = seo.get('chosen_title_index')
        if not __temp_271359:
            idx = 0
        else:
            idx = __temp_271359
        if isinstance(idx, int):
            if 0 <= idx:
                if not idx < len(titles):
                    idx = 0
            else:
                idx = 0
        else:
            idx = 0
        if not titles[idx]:
            name = ''.strip()
        else:
            name = titles[idx].strip()
    if not name:
        if not v.title:
            __temp_271364 = ''.strip()
        else:
            v.title.strip()
        if not __temp_271364:
            name = 'video_' + str(v.id[None:8])
        else:
            name = __temp_271364
    __temp_271370 = safe_name(name.replace('\n', ' ').strip())[None:_MAX_NAME
        ].strip().rstrip('.')
    if not __temp_271370:
        return 'video_' + str(v.id[None:8])
    else:
        return __temp_271370



# NOT DECOMPILED: resolve_dest


# NOT DECOMPILED: write_seo_files


# NOT DECOMPILED: ai_thumbnail_path


# NOT DECOMPILED: copy_thumbnails


# Original qualified name: cleanup_working
def cleanup_working(fs, vid):
    work = fs.find_video_dir(vid)
    if work is not None:
        if work.exists():
            shutil.rmtree(work, ignore_errors=True)
            return None
        return None
    return None

