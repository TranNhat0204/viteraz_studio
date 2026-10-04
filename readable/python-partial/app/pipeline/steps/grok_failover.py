# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/pipeline/steps/grok_failover.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: GrokFailover.__init__
def __init__(self, video_id, job_id, preferred_partition):
    self.tried = set()
    self.multi = False
    self.account_id = None
    self.label = 'mặc định'
    self.exhausted = False
    self.exhausted_reason = None
    self.video_id = video_id
    self.job_id = job_id
    self.preferred = preferred_partition
    with SessionLocal() as __temp_256010:
        db = __temp_256010
        if grok_acct.list_accounts(db):
            self.multi = True
            acc = self._next_with_credentials(db)
            if acc is not None:
                self._adopt(acc)
                grok_acct.mark_used(db, acc.partition_id)
            else:
                self.exhausted = True
                self.exhausted_reason = 'credentials'
        if not self.apply_credentials():
            if self.multi:
                self.exhausted = True
                self.exhausted_reason = 'credentials'
                return None
            return None
        return None



# NOT DECOMPILED: GrokFailover._next_with_credentials


# Original qualified name: GrokFailover._adopt
def _adopt(self, acc):
    self.account_id = acc.partition_id
    if not acc.email:
        if not acc.label:
            self.label = acc.partition_id
        else:
            self.label = acc.label
    else:
        self.label = acc.email
    return None



# Original qualified name: GrokFailover.exhausted_all
def exhausted_all(self):
    if self.multi:
        return self.exhausted
    return False



# NOT DECOMPILED: GrokFailover.apply_credentials


# Original qualified name: GrokFailover._switch
def _switch(self, mark_quota, reason):
    if not self.multi:
        return False
    with SessionLocal() as __temp_256360:
        db = __temp_256360
        if self.account_id:
            if mark_quota:
                grok_acct.mark_exhausted(db, self.account_id)
                self.tried.add(self.account_id)
                __temp_256363 = self.account_id.startswith('bp:')
            else:
                self.tried.add(self.account_id)
                self.account_id.startswith('bp:')
            if __temp_256363:
                if self.video_id:
                    app = __import__('app.services', fromlist=(
                        'browser_profile_service',), level=0)
                    browser_profile_service = app.browser_profile_service
                    bps = browser_profile_service
                    bps.release_profile_if_held(db, self.account_id[3:None],
                        self.video_id)
                    nxt = self._next_with_credentials(db)
                else:
                    nxt = self._next_with_credentials(db)
            else:
                nxt = self._next_with_credentials(db)
        else:
            nxt = self._next_with_credentials(db)
        if nxt is None:
            self.exhausted = True
            self.exhausted_reason = reason
            return False
        self._adopt(nxt)
        self.exhausted_reason = None
        grok_acct.mark_used(db, nxt.partition_id)
        return self.apply_credentials()



# Original qualified name: GrokFailover.on_quota
def on_quota(self):
    return self._switch(mark_quota=True, reason='quota')



# Original qualified name: GrokFailover.on_rate_limit
def on_rate_limit(self):
    return self._switch(mark_quota=False, reason='rate_limit')



# Original qualified name: GrokFailover.on_auth
def on_auth(self):
    return self._switch(mark_quota=False, reason='auth')



# NOT DECOMPILED: GrokFailover.sync_credentials_from_disk
