import logging
import time

from celery.signals import (
    task_prerun,
    task_postrun,
    task_failure,
    task_retry,
)

logger = logging.getLogger("celery")

_task_start_times = {}


@task_prerun.connect
def task_started(sender=None, task_id=None, task=None, **kwargs):
    """
    Called before every Celery task starts.
    """
    _task_start_times[task_id] = time.perf_counter()

    logger.info(
        "Task Started | ID=%s | Name=%s",
        task_id,
        sender.name if sender else "Unknown",
    )


@task_postrun.connect
def task_finished(sender=None, task_id=None, task=None, **kwargs):
    """
    Called after every successful task.
    """
    start = _task_start_times.pop(task_id, None)

    duration = (
        round(time.perf_counter() - start, 3)
        if start
        else 0
    )

    logger.info(
        "Task Finished | ID=%s | Name=%s | Duration=%ss",
        task_id,
        sender.name if sender else "Unknown",
        duration,
    )


@task_failure.connect
def task_failed(
    sender=None,
    task_id=None,
    exception=None,
    traceback=None,
    **kwargs,
):
    logger.exception(
        "Task Failed | ID=%s | Name=%s | Exception=%s",
        task_id,
        sender.name if sender else "Unknown",
        exception,
    )


@task_retry.connect
def task_retried(
    sender=None,
    task_id=None,
    reason=None,
    **kwargs,
):
    logger.warning(
        "Task Retry | ID=%s | Name=%s | Reason=%s",
        task_id,
        sender.name if sender else "Unknown",
        reason,
    )