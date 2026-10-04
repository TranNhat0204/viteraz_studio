# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/pipeline/steps/chatgpt_failover.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: ChatGPTFailover.__init__
def __init__(self):
    self.tried = set()
    self.multi = False
    self.account_id = None
    self.label = 'mặc định'
    self.exhausted = False
    with SessionLocal() as __temp_228903:
        db = __temp_228903
        if chatgpt_acct.list_accounts(db):
            self.multi = True
            acc = self._next_with_credentials(db)
            if acc is not None:
                self._adopt(acc)
                chatgpt_acct.mark_used(db, acc.partition_id)
            else:
                self.exhausted = True
        if not self.apply_credentials():
            if self.multi:
                self.exhausted = True
                return None
            return None
        return None



# NOT DECOMPILED: ChatGPTFailover._next_with_credentials


# Original qualified name: ChatGPTFailover._adopt
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



# Original qualified name: ChatGPTFailover.exhausted_all
def exhausted_all(self):
    if self.multi:
        return self.exhausted
    return False



# NOT DECOMPILED: ChatGPTFailover.apply_credentials


# Original qualified name: ChatGPTFailover._switch
def _switch(self, mark_quota):
    if not self.multi:
        return False
    with SessionLocal() as __temp_254324:
        db = __temp_254324
        if self.account_id:
            if mark_quota:
                chatgpt_acct.mark_exhausted(db, self.account_id)
                self.tried.add(self.account_id)
                nxt = self._next_with_credentials(db)
            else:
                self.tried.add(self.account_id)
                nxt = self._next_with_credentials(db)
        else:
            nxt = self._next_with_credentials(db)
        if nxt is None:
            self.exhausted = True
            return False
        self._adopt(nxt)
        chatgpt_acct.mark_used(db, nxt.partition_id)
        return self.apply_credentials()



# Original qualified name: ChatGPTFailover.on_quota
def on_quota(self):
    return self._switch(mark_quota=True)



# Original qualified name: ChatGPTFailover.on_rate_limit
def on_rate_limit(self):
    return self._switch(mark_quota=False)



# Original qualified name: ChatGPTFailover.on_auth
def on_auth(self):
    return self._switch(mark_quota=False)



# NOT DECOMPILED: ChatGPTFailover.sync_credentials_from_disk
