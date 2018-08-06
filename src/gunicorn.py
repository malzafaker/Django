from multiprocessing import cpu_count
from os import environ


def get_max_workers():
    return cpu_count() * 2 + 1


def get_max_treads():
    return cpu_count()


max_requests = 1000
worker_class = 'gevent'
workers = get_max_workers()
threads = get_max_treads()
pidfile = '/tmp/gunicorn.pid'
# bind = 'unix:/tmp/django.sock'
bind = "0.0.0.0:8000"
reload = True
errorlog = '/src/logs/error.log'
accesslog = '/src/logs/access.log'