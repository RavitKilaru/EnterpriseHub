from celery import shared_task


@shared_task
def add(a: int, b: int):
    return a + b