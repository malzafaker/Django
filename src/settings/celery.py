from __future__ import absolute_import, unicode_literals

import os
from datetime import timedelta

from celery import Celery
from celery.task import periodic_task

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.base')


app = Celery('project')


app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


@periodic_task(run_every=timedelta(seconds=60))
def clear_task_state():
    from django_celery_monitor.models import TaskState
    TaskState.objects.filter(name='sett[.]its_works').delete()
    TaskState.objects.filter(name='run_rates').delete()
    TaskState.objects.filter(name='debit').delete()
    TaskState.objects.filter(name='settings.new_cel[.]clear_task_state').delete()
    TaskState.objects.filter(name='run_auto_payment').delete()


@periodic_task(run_every=timedelta(seconds=300))
def its_works():
    print("is works!")

