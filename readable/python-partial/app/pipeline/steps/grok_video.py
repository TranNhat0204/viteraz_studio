# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/pipeline/steps/grok_video.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _real_file
def _real_file(path):
    __temp_256387 = bool(path)
    if __temp_256387:
        __temp_256389 = Path(path).is_file()
        if __temp_256389:
            return not is_placeholder(path)
        else:
            return __temp_256389
    else:
        return __temp_256387



# Original qualified name: scene_needs_clip
def scene_needs_clip(scene):
    if not scene.get('render_skip'):
        if scene.get('media_type') != 'video':
            return False
    else:
        return False
    __temp_256393 = scene.get('status')
    if __temp_256393 == 'done':
        __temp_256394 = scene.get('asset_kind')
        if __temp_256394 == 'video':
            return not _real_file(scene.get('asset_path'))
        else:
            return not __temp_256394 == 'video'
    else:
        return not __temp_256393 == 'done'



# Original qualified name: video_prompt_for
def video_prompt_for(scene):
    __temp_256397 = scene.get('video_prompt_en')
    if not __temp_256397:
        __temp_256398 = scene.get('image_prompt_en')
        if not __temp_256398:
            __temp_256399 = scene.get('text')
            if not __temp_256399:
                return ''.strip()
            else:
                return __temp_256399.strip()
        else:
            return __temp_256398.strip()
    else:
        return __temp_256397.strip()



# Original qualified name: keep_still
def keep_still(scene, keyframe, source, reason):
    scene['asset_path'] = str(Path(keyframe).resolve())
    scene['asset_kind'] = 'image'
    scene['status'] = 'done'
    scene['video_source'] = source
    if reason:
        scene['clip_status'] = 'failed'
        scene['clip_error'] = reason
        return None
    return None



# NOT DECOMPILED: GrokVideoStep.run


# NOT DECOMPILED: GrokVideoStep._finish


# NOT DECOMPILED: GrokVideoStep._load_scenes


# NOT DECOMPILED: GrokVideoStep._save_scenes
