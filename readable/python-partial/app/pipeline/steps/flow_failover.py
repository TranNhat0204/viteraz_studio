# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/pipeline/steps/flow_failover.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: FlowFailover.__init__
def __init__(self, project_key, video_model, image_model, video_id, job_id, partition_id, isolated_lease, allow_failover):
    self.tried = set()
    self.multi = False
    self.account_id = None
    self.label = 'mặc định'
    self.exhausted = False
    self.video_engine = None
    self.video_model = video_model
    self.image_model = image_model
    self.project_key = project_key
    self.video_id = video_id
    self.job_id = job_id
    self.isolated_lease = isolated_lease
    self.allow_failover = allow_failover
    self._valid = True
    self._valid_until = 0.0
    with SessionLocal() as __temp_255912:
        db = __temp_255912
        if flow_acct.list_accounts(db):
            self.multi = True
            if partition_id:
                acc = self._by_partition(db, partition_id)
            elif video_id:
                part = bps.lease_acquire_flow(db, video_id, job_id)
                if part:
                    acc = self._by_partition(db, part)
                else:
                    acc = None
            else:
                acc = flow_acct.next_available(db, exclude=bps.
                    leased_partitions(db))
            if acc is not None:
                self._adopt(acc)
                flow_acct.mark_used(db, acc.partition_id)
            else:
                self.exhausted = True
        self.client = FlowSessionClient(account_id=self.account_id, project_key
            =project_key, video_engine=self.video_engine, video_model=self.
            video_model, image_model=self.image_model)
        return None



# Original qualified name: FlowFailover._by_partition
def _by_partition(db, partition_id):
    app = __import__('app.db.models', fromlist=('FlowAccount',), level=0)
    FlowAccount = app.FlowAccount
    return db.query(FlowAccount).filter(FlowAccount.partition_id == partition_id
        ).first()



# Original qualified name: FlowFailover._adopt
def _adopt(self, acc):
    self.account_id = acc.partition_id
    if not acc.email:
        if not acc.label:
            self.label = acc.partition_id
        else:
            self.label = acc.label
    else:
        self.label = acc.email
    __temp_255926 = getattr(acc, 'video_engine', None)
    if not __temp_255926:
        self.video_engine = None
    else:
        self.video_engine = __temp_255926
    __temp_255927, __temp_255928 = True, 0.0
    self._valid = __temp_255927
    self._valid_until = __temp_255928
    bps.note_account_used(self.video_id, self.account_id)
    return None



# Original qualified name: FlowFailover.exhausted_all
def exhausted_all(self):
    if self.multi:
        return self.exhausted
    return False



# Original qualified name: FlowFailover._switch
def _switch(self, mark_quota, sick_reason, remember_tried, exhaust_when_empty):
    if not self.multi:
        return False
    if not self.allow_failover:
        if exhaust_when_empty:
            self.exhausted = True
        return False
    with SessionLocal() as __temp_255931:
        db = __temp_255931
        if self.account_id:
            if mark_quota:
                flow_acct.mark_exhausted(db, self.account_id)
            elif sick_reason:
                flow_health.mark_sick(self.account_id, sick_reason)
            if remember_tried:
                self.tried.add(self.account_id)
        if self.video_id:
            if self.isolated_lease:
                part = bps.lease_rotate_flow_worker(db, self.video_id, self.
                    account_id, self.tried, job_id=self.job_id)
            else:
                part = bps.lease_rotate_flow(db, self.video_id, self.account_id,
                    self.tried, job_id=self.job_id)
            if part:
                nxt = self._by_partition(db, part)
            else:
                nxt = None
        else:
            exclude = self.tried | bps.leased_partitions(db)
            nxt = flow_acct.next_available(db, exclude=exclude)
        if nxt is None:
            if exhaust_when_empty:
                self.exhausted = True
            return False
        self._adopt(nxt)
        flow_acct.mark_used(db, nxt.partition_id)
        self.client = FlowSessionClient(account_id=self.account_id, project_key
            =self.project_key, video_engine=self.video_engine, video_model=self
            .video_model, image_model=self.image_model)
        return True



# Original qualified name: FlowFailover.on_quota
def on_quota(self):
    return self._switch(mark_quota=True)



# NOT DECOMPILED: FlowFailover.note_rate_limit


# NOT DECOMPILED: FlowFailover.on_rate_limit


# NOT DECOMPILED: FlowFailover.on_rate_limit_async


# NOT DECOMPILED: FlowFailover.on_project_dead


# Original qualified name: FlowFailover.on_auth
def on_auth(self):
    return self._switch(mark_quota=False, sick_reason=
        'mất đăng nhập / Chrome profile không còn trên máy')



# NOT DECOMPILED: FlowFailover.still_valid


# NOT DECOMPILED: rotate_on_rate_limit


# NOT DECOMPILED: reseed_characters


# NOT DECOMPILED: rotate_on_project_dead
