# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/news_import_service.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _extract_images_from_html
def _extract_images_from_html(html_content):
    if not html_content:
        return []
    total_len = max(1, len(html_content))
    images = []
    figure_pattern = re.compile('<figure[^>]*>(.*?)</figure>', re.DOTALL | re.
        IGNORECASE)
    img_pattern = re.compile(
        '<img[^>]*\\bsrc=["\\\']([^"\\\']+)["\\\'][^>]*/?\\s*>', re.IGNORECASE)
    caption_pattern = re.compile('<figcaption[^>]*>(.*?)</figcaption>', re.
        DOTALL | re.IGNORECASE)
    for __temp_275788 in iter(figure_pattern.finditer(html_content)):
        match = __temp_275788
        figure_html = match.group(1)
        figure_pos = match.start()
        img_match = img_pattern.search(figure_html)
        if not img_match:
            continue
            url = img_match.group(1).strip()
        else:
            url = img_match.group(1).strip()
        if url:
            if url.startswith('data:'):
                continue
                cap_match = caption_pattern.search(figure_html)
            else:
                cap_match = caption_pattern.search(figure_html)
        else:
            continue
            cap_match = caption_pattern.search(figure_html)
        caption = ''
        if cap_match:
            caption = re.sub('<[^>]+>', '', cap_match.group(1)).strip()
        context = _extract_surrounding_text(html_content, figure_pos, radius=300)
        images.append({url: url, caption: caption, context: context, index: len
            (images), pos_ratio: round(figure_pos / total_len, 4)})
        continue
    if not images:
        for __temp_275809 in iter(img_pattern.finditer(html_content)):
            match = __temp_275809
            url = match.group(1).strip()
            if url:
                if not url.startswith('data:'):
                    if not 'icon' in url.lower():
                        if 'logo' in url.lower():
                            continue
                            alt_match = re.search('alt=["\\\']([^"\\\']*)["\\\']',
                                match.group(0), re.IGNORECASE)
                        else:
                            alt_match = re.search('alt=["\\\']([^"\\\']*)["\\\']',
                                match.group(0), re.IGNORECASE)
                    else:
                        continue
                        alt_match = re.search('alt=["\\\']([^"\\\']*)["\\\']',
                            match.group(0), re.IGNORECASE)
                else:
                    continue
                    alt_match = re.search('alt=["\\\']([^"\\\']*)["\\\']',
                        match.group(0), re.IGNORECASE)
            else:
                continue
                alt_match = re.search('alt=["\\\']([^"\\\']*)["\\\']', match.
                    group(0), re.IGNORECASE)
            if alt_match:
                caption = alt_match.group(1).strip()
            else:
                caption = ''
            context = _extract_surrounding_text(html_content, match.start(),
                radius=300)
            images.append({url: url, caption: caption, context: context, index:
                len(images), pos_ratio: round(match.start() / total_len, 4)})
            continue
        return images
    else:
        return images



# Original qualified name: _extract_surrounding_text
def _extract_surrounding_text(html, pos, radius):
    start = max(0, pos - radius)
    end = min(len(html), pos + radius)
    chunk = html[start:end]
    text = re.sub('<[^>]+>', ' ', chunk)
    text = re.sub('\\s+', ' ', text).strip()
    return text[None:400]



# NOT DECOMPILED: _usable_image_size


# NOT DECOMPILED: _download_article_images


# Original qualified name: _strip_html_to_text
def _strip_html_to_text(html_content):
    if not html_content:
        return
    text = re.sub('<figcaption[^>]*>(.*?)</figcaption>', '\\n[Caption: \\1]\\n',
        html_content, flags=re.DOTALL)
    text = re.sub('<img[^>]*alt="([^"]*)"[^>]*/?\\s*>', '\\n[Image: \\1]\\n', text)
    text = re.sub('<h[1-6][^>]*>(.*?)</h[1-6]>', '\\n## \\1\\n', text, flags=re
        .DOTALL)
    text = re.sub('</p>', '\n', text)
    text = re.sub('<br\\s*/?>', '\n', text)
    text = re.sub('<[^>]+>', '', text)
    text = re.sub('\\n{3,}', '\n\n', text).strip()
    return text



# NOT DECOMPILED: _build_news_idea_prompt


# NOT DECOMPILED: import_article_to_channel


# Original qualified name: import_article_to_channel.<locals>.checkpoint
def checkpoint(percent):
    nonlocal cancel_check, progress
    if cancel_check:
        if cancel_check():
            raise StudioError(E.CANCELLED, 'Đã huỷ import bài báo.')
    if progress:
        progress(percent)
        return None
    return None

