FROM python:3.6
ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true
RUN mkdir /src
RUN mkdir /static
WORKDIR /src
ADD ./src /src
RUN rm -f /src/celeryev.pid

RUN apt-get update
RUN apt-get install -y build-essential python-all-dev
RUN apt install -y gdal-bin python-gdal

#RUN echo 'deb http://www.rabbitmq.com/debian/ testing main' > /etc/apt/sources.list.d/rabbitmq.list
#RUN wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | apt-key add -
#RUN apt-get update && apt-get install -y --no-install-recommends rabbitmq-server && rm -rf /var/lib/apt/lists/*
#
#RUN service rabbitmq-server start
#RUN service rabbitmq-server status
#RUN rabbitmqctl add_user django django
#RUN rabbitmqctl add_vhost django_vhost
#RUN rabbitmqctl set_permissions -p django_vhost wikiworks ".*" ".*" ".*"

COPY src/requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt


#CMD python manage.py collectstatic --no-input; python manage.py migrate; python manage.py migrate celery_monitor, gunicorn wsgi --log-level debug -b 0.0.0.0:8000  --reload; celery -A settings.celery worker -l info -B -E --loglevel=debug --concurrency=4; celery -A settings.celery events -l info --camera django_celery_monitor.camera.Camera --frequency=2.0
#CMD python manage.py collectstatic --no-input; python manage.py migrate; gunicorn --config=gunicorn.py wsgi.application --log-level debug
CMD python manage.py collectstatic --no-input; python manage.py makemigrations; python manage.py migrate;  python manage.py runserver 0.0.0.0:8001
