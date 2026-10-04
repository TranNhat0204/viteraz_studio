# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/metaai/graphql.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: graphql_request


# Original qualified name: _truncate
def _truncate(s, n):
    if len(s) <= n:
        return s
    return s[None:n] + '…'

