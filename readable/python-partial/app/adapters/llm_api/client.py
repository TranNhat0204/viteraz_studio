# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/llm_api/client.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: _is_local_host


# NOT DECOMPILED: estimate_tokens


# Original qualified name: ApiClient.__init__
def __init__(self, provider, model, api_key, timeout):
    self.provider = provider
    self.model = model
    self.api_key = api_key
    self.timeout = timeout
    self._transport = None
    self._dropped = frozenset()
    self.max_retries = MAX_RETRIES
    return None



# Original qualified name: ApiClient.dialect
def dialect(self):
    module = dialects.get(self.provider.dialect)
    if module is None:
        raise make_error(E.LLM_API_BAD_RESPONSE, 'Định dạng API ' + repr(self.
            provider.dialect) + ' của ' + str(self.provider.label) +
            ' chưa hỗ trợ. Đang có: ' + str(', '.join(dialects.keys())) + '.')
    return module



# Original qualified name: ApiClient._guard_price_cliff
def _guard_price_cliff(self, messages):
    cliff = self.provider.price_cliff
    if cliff is None:
        return None
    estimated = estimate_tokens(messages)
    if estimated > cliff.input_tokens:
        raise make_error(E.LLM_API_CONTEXT_TOO_LONG, 'Prompt ước tính ' +
            format(estimated, ',') + ' token, vượt ngưỡng ' + format(cliff.
            input_tokens, ',') + ' của ' + str(self.provider.label) +
            '. Vượt ngưỡng này thì CẢ request bị tính giá ' + str(cliff.mult_in
            ) + 'x vào / ' + str(cliff.mult_out) + 'x ra. Hãy nén bớt đầu vào.')
    return None



# Original qualified name: ApiClient._guard_context
def _guard_context(self, messages):
    estimated = estimate_tokens(messages)
    if estimated > self.model.max_input_tokens:
        raise make_error(E.LLM_API_CONTEXT_TOO_LONG, 'Prompt ước tính ' +
            format(estimated, ',') + ' token, vượt context ' + format(self.
            model.max_input_tokens, ',') + ' của model ' + str(self.model.id) + '.'
            )
    return None



# NOT DECOMPILED: ApiClient._parse


# NOT DECOMPILED: ApiClient._post


# NOT DECOMPILED: ApiClient._post_with_degrade


# NOT DECOMPILED: ApiClient.complete
