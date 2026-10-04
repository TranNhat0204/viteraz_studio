# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/logo_sweep_service.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: SweepReport.as_dict
def as_dict(self):
    return {scanned: self.scanned, cleaned: self.cleaned, forced: self.forced,
        already_clean: self.already_clean, skipped: self.skipped, deferred:
        self.deferred[None:50], deferred_count: len(self.deferred), failed:
        self.failed[None:50], failed_count: len(self.failed)}



# NOT DECOMPILED: _candidates


# NOT DECOMPILED: sweep_paths


# NOT DECOMPILED: sweep_video


# NOT DECOMPILED: sweep_project
