# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/core/gpu_gate.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _Holder.__init__
def __init__(self, hid, kind, label):
    self.id = hid
    self.kind = kind
    self.label = label
    self.since = time.monotonic()
    return None



# Original qualified name: GpuGate.__init__
def __init__(self, concurrency):
    self._size = max(1, concurrency)
    self._seq = itertools.count(1)
    self._holders = {}
    self._waiting = {}
    self._cond = None
    return None



# Original qualified name: GpuGate._condition
def _condition(self):
    if self._cond is None:
        self._cond = asyncio.Condition()
    return self._cond



# Original qualified name: GpuGate.size
def size(self):
    return self._size



# Original qualified name: GpuGate.active
def active(self):
    return len(self._holders)



# NOT DECOMPILED: GpuGate.resize


# NOT DECOMPILED: GpuGate.resize.<locals>._wake


# NOT DECOMPILED: GpuGate.slot


# NOT DECOMPILED: GpuGate._notify_soon


# NOT DECOMPILED: GpuGate._notify_soon.<locals>._wake


# NOT DECOMPILED: GpuGate.snapshot
