# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/pipeline/steps/meta_failover.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: MetaFailover.__init__
def __init__(self, project_key):
    self.tried = set()
    self.multi = False
    self.account_id = None
    self.label = 'mặc định'
    self.exhausted = False
    self.project_key = project_key
    with SessionLocal() as __temp_256483:
        db = __temp_256483
        if meta_acct.list_accounts(db):
            self.multi = True
            acc = meta_acct.next_available(db)
            if acc is not None:
                self._adopt(acc)
                meta_acct.mark_used(db, acc.partition_id)
            else:
                self.exhausted = True
        self.client = MetaSessionClient(account_id=self.account_id, project_key
            =project_key)
        return None



# Original qualified name: MetaFailover._adopt
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



# Original qualified name: MetaFailover.exhausted_all
def exhausted_all(self):
    if self.multi:
        return self.exhausted
    return False



# Original qualified name: MetaFailover._switch
def _switch(self, mark_quota):
    if not self.multi:
        return False
    with SessionLocal() as __temp_256491:
        db = __temp_256491
        if self.account_id:
            if mark_quota:
                meta_acct.mark_exhausted(db, self.account_id)
                self.tried.add(self.account_id)
                nxt = meta_acct.next_available(db, exclude=self.tried)
            else:
                self.tried.add(self.account_id)
                nxt = meta_acct.next_available(db, exclude=self.tried)
        else:
            nxt = meta_acct.next_available(db, exclude=self.tried)
        if nxt is None:
            self.exhausted = True
            return False
        self._adopt(nxt)
        meta_acct.mark_used(db, nxt.partition_id)
        self.client = MetaSessionClient(account_id=self.account_id, project_key
            =self.project_key)
        return True



# Original qualified name: MetaFailover.on_quota
def on_quota(self):
    return self._switch(mark_quota=True)



# Original qualified name: MetaFailover.on_rate_limit
def on_rate_limit(self):
    return self._switch(mark_quota=False)



# Original qualified name: MetaFailover.on_auth
def on_auth(self):
    return self._switch(mark_quota=False)

