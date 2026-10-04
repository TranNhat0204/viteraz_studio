# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/openai_image.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _api_key
def _api_key():
    with SessionLocal() as __temp_22797:
        db = __temp_22797
        row = db.get(Setting, 'openai_api_key')
        if row:
            if row.value:
                key = row.value
            else:
                key = ''
        else:
            key = ''
        if not key:
            raise make_error(E.IMAGE_AUTH,
                'Chưa cấu hình OpenAI API key. Mở Settings để nhập.')
        return key



# Original qualified name: build_thumbnail_prompt
def build_thumbnail_prompt(hook, style_prompt, platform, aspect, extra, language):
    plat = {tiktok: 'TikTok', reels: 'Instagram Reels', shorts: 'YouTube Shorts'
        }.get(platform, 'short-form video')
    parts = ['Create a scroll-stopping, professional ' + str(plat) +
        ' thumbnail, ' + str(aspect) + ' aspect ratio, ultra high quality.',
        'Use the main subject/person from the provided reference image as the focal point — keep them clearly recognizable and place them prominently using the rule of thirds, with dramatic cinematic studio lighting, high contrast, vibrant punchy colors and a clean subtle depth-of-field background.'
        ]
    if hook:
        parts.append('Add the bold headline text "' + str(hook) +
            '" in a modern, heavy, highly legible display font — large, with a strong contrasting outline and drop shadow so it pops; position it so it does NOT cover the subject\'s face.'
            )
    if style_prompt:
        parts.append(
            'Brand/style direction (keep consistent across the whole channel): ' +
            str(style_prompt) + '.')
    if extra:
        parts.append(extra)
        parts.append(
            'Make it look like a top 1% viral creator thumbnail: emotionally compelling, premium, eye-catching, optimized for maximum click-through-rate. No watermarks, no logos, and no extra text other than the headline.'
            )
        prompt = ' '.join(parts)
    else:
        parts.append(
            'Make it look like a top 1% viral creator thumbnail: emotionally compelling, premium, eye-catching, optimized for maximum click-through-rate. No watermarks, no logos, and no extra text other than the headline.'
            )
        prompt = ' '.join(parts)
    if language:
        return with_in_image_text_policy(prompt, language)
    return prompt



# NOT DECOMPILED: generate_thumbnail
