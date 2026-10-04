# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/stock/pexels_client.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: PexelsClient.__init__
def __init__(self):
    self.key = get_setting('pexels_api_key')
    return None



# Original qualified name: PexelsClient.available
def available(self):
    return bool(self.key)



# NOT DECOMPILED: PexelsClient.search
