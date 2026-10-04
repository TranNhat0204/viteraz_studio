# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/api/analytics.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _artifact_url
def _artifact_url(video_id, artifact):
    st = get_settings()
    return 'http://127.0.0.1:' + str(st.port) + '/api/v1/videos/' + str(video_id
        ) + '/preview/' + str(artifact) + '?token=' + str(st.token)



# NOT DECOMPILED: get_library


# NOT DECOMPILED: get_stats
