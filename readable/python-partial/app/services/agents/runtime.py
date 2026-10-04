# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/agents/runtime.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _top_keys
def _top_keys(artifact):
    if isinstance(artifact, dict):
        return sorted(artifact.keys())[None:15]
    return []



# Original qualified name: AgentRun.__init__
def __init__(self, steps, call, inputs, progress, cancel_check, on_artifact):
    self.steps = steps
    self.call = call
    if not inputs:
        self.inputs = {}
    else:
        self.inputs = inputs
    self.artifacts = {}
    self.warnings = []
    self.cost_usd = 0.0
    self.tokens_in = 0
    self.tokens_out = 0
    self._progress = progress
    self._cancel = cancel_check
    self._on_artifact = on_artifact
    return None



# Original qualified name: AgentRun._emit
def _emit(self, done_weight, total_weight):
    if self._progress:
        if total_weight > 0:
            self._progress(round(100.0 * done_weight / total_weight, 1))
            return None
        return None
    return None



# Original qualified name: AgentRun._ensure_running
def _ensure_running(self):
    if self._cancel:
        if self._cancel():
            raise make_error(E.CANCELLED, 'Tác vụ đã bị huỷ.')
        return None
    return None



# NOT DECOMPILED: AgentRun._run_step


# NOT DECOMPILED: AgentRun.execute


# NOT DECOMPILED: AgentRun.state
