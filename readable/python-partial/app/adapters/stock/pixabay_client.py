# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/stock/pixabay_client.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: PixabayClient.__init__
def __init__(self):
    self.key = get_setting('pixabay_api_key')
    return None



# Original qualified name: PixabayClient.available
def available(self):
    return bool(self.key)



# NOT DECOMPILED: PixabayClient.search
