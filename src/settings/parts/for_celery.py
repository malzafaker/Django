
# Отправлять оповещение о проблемах выполнения тасков на E-mail (берутся адреса из settings.ADMINS)
# CELERND_TASK_ERROR_EMAILS = True
# Адрес броекра. Мы указываем протокол (redis://), адрес сервера (redis), порт (6379) и номер БД (0)
BROKER_URL = 'redis://redis:6379/1'
BROKER_POOL_LIMIT = None
# Тип бекенда Celery для хранения результатов выполнения заданий
# храним результаты выполнения задач так же в redis.
CELERY_BROKER_URL = 'redis://redis:6379/1'
CELERY_RESULT_BACKEND = 'redis://redis:6379/1'
# # Адрес Redis-сервера
CELERY_REDIS_HOST = "redis"
CELERY_SEND_EVENTS = True
CELERY_TASK_RESULT_EXPIRES = 1*86400  # 1 days
CELERY_TIMEZONE = 'Europe/Moscow'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']
