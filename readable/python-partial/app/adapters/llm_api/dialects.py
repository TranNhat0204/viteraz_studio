# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/llm_api/dialects.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: get
def get(key):
    app = __import__('app.adapters.llm_api.dialects', fromlist=(
        'anthropic_messages', 'openai_chat'), level=0)
    anthropic_messages = app.anthropic_messages
    openai_chat = app.openai_chat
    __temp_3755 = {openai_chat.KEY: openai_chat, anthropic_messages.KEY:
        anthropic_messages, 'openai': openai_chat}
    if not key:
        return __temp_3755.get(''.strip())
    else:
        return __temp_3755.get(key.strip())



# Original qualified name: keys
def keys():
    app = __import__('app.adapters.llm_api.dialects', fromlist=(
        'anthropic_messages', 'openai_chat'), level=0)
    anthropic_messages = app.anthropic_messages
    openai_chat = app.openai_chat
    return openai_chat.KEY, anthropic_messages.KEY

