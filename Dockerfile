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

COPY src/requirements.txt /tmp/
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt

CMD python manage.py collectstatic --no-input; python manage.py makemigrations; python manage.py migrate; python manage.py migrate celery_monitor; python manage.py runserver 0.0.0.0:8002
