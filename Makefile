build:
	docker-compose build

up:
	docker-compose up -d

up-non-daemon:
	docker-compose up

start:
	docker-compose start

stop:
	docker-compose stop

restart:
	docker-compose stop && docker-compose start

shell-nginx:
	docker exec -ti nginx bash

shell-web:
	docker exec -ti web bash

shell-db:
	docker exec -ti postgresql bash

log-nginx:
	docker-compose logs nginx  

log-web:
	docker-compose logs web  

log-db:
	docker-compose logs postgresql

collectstatic:
	docker exec web_project /bin/sh -c "python manage.py collectstatic --noinput"

migrate:
	docker exec web_project /bin/sh -c "python manage.py migrate"

makemigrations:
	docker exec web_project /bin/sh -c "python manage.py makemigrations"
