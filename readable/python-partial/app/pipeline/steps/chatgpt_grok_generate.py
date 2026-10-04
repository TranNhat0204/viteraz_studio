# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/pipeline/steps/chatgpt_grok_generate.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: grok_web_duration


# Original qualified name: _parse_ssim_score
def _parse_ssim_score(output):
    if not output:
        matches = re.findall('\\bAll:([0-9]+(?:\\.[0-9]+)?)', '')
    else:
        matches = re.findall('\\bAll:([0-9]+(?:\\.[0-9]+)?)', output)
    if matches:
        return float(matches[-1])
    return None



# NOT DECOMPILED: _frame_ssim


# NOT DECOMPILED: _keyframe_ssim


# NOT DECOMPILED: build_scene_references


# Original qualified name: _chatgpt_ref
def _chatgpt_ref(character):
    __temp_254403 = character.get('chatgpt_ref_path')
    if not __temp_254403:
        dedicated = str('').strip()
    else:
        dedicated = str(__temp_254403).strip()
    if dedicated:
        return dedicated
    __temp_254408 = character.get('ref_path')
    if not __temp_254408:
        legacy = str('').strip()
    else:
        legacy = str(__temp_254408).strip()
    if Path(legacy).name.lower().startswith('chatgpt_'):
        return legacy
    return ''



# NOT DECOMPILED: ChatGPTGrokGenerateStep.run


# NOT DECOMPILED: ChatGPTGrokGenerateStep.run.<locals>._gen_image


# Original qualified name: ChatGPTGrokGenerateStep.run.<locals>.refs_for
def refs_for(scene_obj, prev):
    nonlocal cast_refs
    return build_scene_references(scene_obj, cast_refs, prev)



# NOT DECOMPILED: ChatGPTGrokGenerateStep.run.<locals>.prefetch_scene_image


# Original qualified name: ChatGPTGrokGenerateStep.run.<locals>.continuity_refs
def continuity_refs():
    nonlocal previous_frame, refs_for, scene
    return refs_for(scene, previous_frame)



# Original qualified name: ChatGPTGrokGenerateStep.run.<locals>.remember_frame
def remember_frame(value):
    nonlocal previous_frame
    resolved = str(Path(value).resolve())
    previous_frame = resolved
    return None



# NOT DECOMPILED: ChatGPTGrokGenerateStep._save_scenes


# NOT DECOMPILED: ChatGPTGrokGenerateStep._save_cast
