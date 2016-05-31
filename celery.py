from __future__ import absolute_import

from celery import Celery

app = Celery('proj',
             broker='redis://127.0.0.1:6379',
             backend='redis://127.0.0.1:6379',
             include=['hitwicket.tasks'])

app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=18000,
)

if __name__ == '__main__':
    app.start()
