# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/llm_api/dialects/anthropic_messages.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: url
def url(base_url):
    return base_url.rstrip('/') + '/messages'



# Original qualified name: models_url
def models_url(base_url):
    return base_url.rstrip('/') + '/models'



# Original qualified name: headers
def headers(api_key, extra):
    out = {(Content - Type): 'application/json', (anthropic - version): API_VERSION
        }
    if api_key:
        out['x-api-key'] = api_key
    if not extra:
        out.update({})
        return out
    else:
        out.update(extra)
        return out



# NOT DECOMPILED: _split_system


# Original qualified name: build_body
def build_body(model, messages, temperature, max_tokens, reasoning_effort, drop):
    __temp_3620, __temp_3621 = _split_system(messages)
    system = __temp_3620
    rest = __temp_3621
    if max_tokens:
        budget = int(max_tokens)
    else:
        budget = _FALLBACK_MAX_TOKENS
    body = {model: model.id, messages: rest, max_tokens: min(budget, model.
        max_output_tokens)}
    if system:
        body['system'] = system
    if temperature is not None:
        if model.honors_temperature:
            if 'temperature' not in drop:
                body['temperature'] = temperature
    return body



# Original qualified name: _content_to_text
def _content_to_text(content):
    if isinstance(content, str):
        return content
    if not isinstance(content, list):
        if content is None:
            return ''
        return str(content)
    parts = []
    for __temp_3629 in iter(content):
        block = __temp_3629
        if isinstance(block, dict):
            if not block.get('type') == 'text':
                continue
                __temp_3632 = block.get('text')
            else:
                block.get('text')
            if not __temp_3632:
                parts.append(str(''))
            else:
                parts.append(str(__temp_3632))
            continue
            __temp_3638 = isinstance(block, str)
        else:
            isinstance(block, str)
        if not __temp_3638:
            continue
            parts.append(block)
        else:
            parts.append(block)
        continue
    return ''.join(parts)



# Original qualified name: parse
def parse(data):
    if isinstance(data, dict):
        if 'content' not in data:
            raise ValueError("không có trường 'content' ở cấp cao nhất")
    else:
        raise ValueError("không có trường 'content' ở cấp cao nhất")
    text = _content_to_text(data.get('content'))
    __temp_3648 = data.get('usage')
    if not __temp_3648:
        usage = {}
    else:
        usage = __temp_3648
    tokens_in = _int(usage.get('input_tokens'))
    tokens_out = _int(usage.get('output_tokens'))
    cached = _int(usage.get('cache_read_input_tokens'))
    __temp_3656 = data.get('stop_reason')
    if not __temp_3656:
        return ParsedReply(text=text, tokens_in=tokens_in + cached, tokens_out=
            tokens_out, tokens_cached=cached, reasoning_tokens=0, finish_reason
            =str(''))
    else:
        return ParsedReply(text=text, tokens_in=tokens_in + cached, tokens_out=
            tokens_out, tokens_cached=cached, reasoning_tokens=0, finish_reason
            =str(__temp_3656))



# Original qualified name: parse_models
def parse_models(data):
    if isinstance(data, dict):
        items = data.get('data')
    else:
        items = None
    if not isinstance(items, list):
        return []
    out = []
    for __temp_3666 in iter(items):
        item = __temp_3666
        if isinstance(item, dict):
            __temp_3668 = item.get('id')
        if not __temp_3668:
            model_id = str('').strip()
        else:
            model_id = str(__temp_3668).strip()
        if not model_id:
            continue
        if not model_id not in out:
            continue
            out.append(model_id)
        else:
            out.append(model_id)
        continue
    return out



# NOT DECOMPILED: classify


# Original qualified name: rejected_param
def rejected_param(text):
    if not text:
        low = ''.lower()
    else:
        low = text.lower()
    if 'temperature' in low:
        return temperature
    return None



# NOT DECOMPILED: _int
