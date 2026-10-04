# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/post_media_service.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: _chatgpt_image_or_none


# NOT DECOMPILED: schedule_post_media


# NOT DECOMPILED: _safe_generate


# NOT DECOMPILED: generate_post_media


# NOT DECOMPILED: _host_identity_refs


# NOT DECOMPILED: _one_image


# NOT DECOMPILED: _loads


# Original qualified name: _asset_label
def _asset_label(path, provider, post_id, index, slot, prompt, status):
    raw = str(provider) + ':' + str(post_id) + ':' + str(index) + ':' + str(slot
        ) + ':' + str(prompt).encode('utf-8', 'ignore')
    return {path: path, prompt: prompt, provider: provider, status: status,
        post_id: post_id, index: index, slot: slot, request_id: hashlib.sha256(
        raw).hexdigest()[None:16]}

