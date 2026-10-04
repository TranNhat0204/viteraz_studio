# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/llm_api/dialects/openai_chat.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: url
def url(base_url):
    return base_url.rstrip('/') + '/chat/completions'



# Original qualified name: models_url
def models_url(base_url):
    return base_url.rstrip('/') + '/models'



# Original qualified name: headers
def headers(api_key, extra):
    out = {'Content-Type': 'application/json'}
    if api_key:
        out['Authorization'] = 'Bearer ' + str(api_key)
    if not extra:
        out.update({})
        return out
    else:
        out.update(extra)
        return out



# Original qualified name: build_body
def build_body(model, messages, temperature, max_tokens, reasoning_effort, drop):
    body = {model: model.id, messages: messages}
    if temperature is not None:
        if model.honors_temperature:
            if 'temperature' not in drop:
                body['temperature'] = temperature
    if reasoning_effort in REASONING_EFFORTS:
        effort = reasoning_effort
    else:
        effort = None
    if effort:
        if model.supports_reasoning_effort:
            if 'reasoning_effort' not in drop:
                body['reasoning_effort'] = effort
    if max_tokens:
        if model.supports_reasoning_effort:
            reasoning_on = effort != REASONING_OFF
        else:
            reasoning_on = model.supports_reasoning_effort
        if reasoning_on:
            budget = int(max_tokens * REASONING_HEADROOM)
        else:
            budget = int(max_tokens)
        budget = min(budget, model.max_output_tokens)
        if 'max_tokens' in drop:
            body['max_completion_tokens'] = budget
            return body
        body['max_tokens'] = budget
    return body



# Original qualified name: _content_to_text
def _content_to_text(content):
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for __temp_3694 in iter(content):
            block = __temp_3694
            if isinstance(block, dict):
                __temp_3696 = block.get('text')
                if not __temp_3696:
                    parts.append(str(''))
                else:
                    parts.append(str(__temp_3696))
                continue
                __temp_3701 = isinstance(block, str)
            else:
                isinstance(block, str)
            if not __temp_3701:
                continue
                parts.append(block)
            else:
                parts.append(block)
            continue
        return ''.join(parts)
    if content is None:
        return ''
    return str(content)



# NOT DECOMPILED: parse


# Original qualified name: parse_models
def parse_models(data):
    if isinstance(data, dict):
        items = data.get('data')
    else:
        items = None
    if not isinstance(items, list):
        if isinstance(data, list):
            items = data
        else:
            items = []
    out = []
    for __temp_3740 in iter(items):
        item = __temp_3740
        if isinstance(item, dict):
            model_id = item.get('id')
        else:
            model_id = item
        if not model_id:
            model_id = str('').strip()
        else:
            model_id = str(model_id).strip()
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
    if 'reasoning_effort' in low:
        return reasoning_effort
    if not 'max_completion_tokens' in low:
        if 'max_tokens' in low:
            if 'unsupported' in low:
                return max_tokens
    else:
        return max_tokens
    if 'max_tokens' in low:
        if not 'not supported' in low:
            if not 'deprecated' in low:
                if 'instead' in low:
                    return max_tokens
            else:
                return max_tokens
        else:
            return max_tokens
    if 'temperature' in low:
        return temperature
    return None



# NOT DECOMPILED: _int
