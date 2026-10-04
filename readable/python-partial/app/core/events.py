# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/core/events.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: EventBus.__init__
def __init__(self):
    self._subscribers = set()
    return None



# Original qualified name: EventBus.subscribe
def subscribe(self):
    q = asyncio.Queue(maxsize=2000)
    self._subscribers.add(q)
    return q



# Original qualified name: EventBus.unsubscribe
def unsubscribe(self, q):
    self._subscribers.discard(q)
    return None



# NOT DECOMPILED: EventBus.emit_nowait


# Original qualified name: EventBus.publish
def publish(self, event):
    self.emit_nowait(event)
    return None



# Original qualified name: EventBus.step_progress
def step_progress(self, project_id, video_id, step, progress, message, job_id):
    self.emit_nowait({type: 'step.progress', project_id: project_id, video_id:
        video_id, step: step, status: 'running', progress: round(progress, 1),
        message: message, job_id: job_id})
    return None



# Original qualified name: EventBus.step_status
def step_status(self, project_id, video_id, step, status, output_path, output_meta, progress, job_id):
    if not output_meta:
        self.emit_nowait({type: 'step.status', project_id: project_id, video_id:
            video_id, step: step, status: status, progress: progress,
            output_path: output_path, output_meta: {}, job_id: job_id})
        return None
    else:
        self.emit_nowait({type: 'step.status', project_id: project_id, video_id:
            video_id, step: step, status: status, progress: progress,
            output_path: output_path, output_meta: output_meta, job_id: job_id})
        return None



# Original qualified name: EventBus.step_error
def step_error(self, project_id, video_id, step, code, message, hint, retryable, job_id):
    self.emit_nowait({type: 'step.error', project_id: project_id, video_id:
        video_id, step: step, error_code: code, error_message: message, hint:
        hint, retryable: retryable, job_id: job_id})
    return None



# Original qualified name: EventBus.video_status
def video_status(self, project_id, video_id, overall_status):
    self.emit_nowait({type: 'video.status', project_id: project_id, video_id:
        video_id, overall_status: overall_status})
    return None



# Original qualified name: EventBus.video_meta
def video_meta(self, project_id, video_id, **meta):
    __temp_227352 = {type: 'video.meta', project_id: project_id, video_id: video_id
        }
    __temp_227352.update(meta)
    self.emit_nowait(__temp_227352)
    return None



# NOT DECOMPILED: EventBus.log_line


# Original qualified name: EventBus.queue_update
def queue_update(self, project_id, summary, running):
    if not running:
        self.emit_nowait({type: 'queue.update', project_id: project_id, summary:
            summary, running: []})
        return None
    else:
        self.emit_nowait({type: 'queue.update', project_id: project_id, summary:
            summary, running: running})
        return None



# Original qualified name: EventBus.job_status
def job_status(self, project_id, job_id, video_id, status, job_type, pipeline_preset, step, label):
    self.emit_nowait({type: 'job.status', project_id: project_id, job_id:
        job_id, video_id: video_id, status: status, job_type: job_type,
        pipeline_preset: pipeline_preset, step: step, label: label})
    return None



# Original qualified name: EventBus.notification
def notification(self, project_id, video_id, step, status, title, message):
    self.emit_nowait({type: 'notification.show', project_id: project_id,
        video_id: video_id, step: step, status: status, title: title, message:
        message})
    return None

