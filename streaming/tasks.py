from types import SimpleNamespace

from celery import shared_task


@shared_task(bind=True)
def process_video_task(self, video_id):
    # This is intentionally lightweight and safe: the real FFmpeg conversion step
    # will be implemented in a later milestone. This keeps the app functional while
    # providing a processing hook for background jobs.
    return {"video_id": video_id, "status": "queued"}
