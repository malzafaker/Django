## Deploy Django using Nginx, Celery, Redis and Postgresql
A boilerplate to deploy Django with cool stuff. Also serves as an example project from these tutorial:
1. <a href="http://ruddra.com/2016/08/14/docker-django-nginx-postgres/">Deploy Django, Gunicorn, NGINX, Postgresql using Docker</a>
2. <a href="http://ruddra.com/2016/11/02/serve-static-files-by-nginx-from-django-using-docker/">Serve Static Files by Nginx from Django using Docker</a>
3. <a href="http://ruddra.com/2016/11/14/docker-do-stuff-using-celery-using-redis-as-broker/">Docker: Use Celery in Django(Redis as Broker)</a>

Where it is described how this boilerplate was created from scratch so that you can build your own.

### Basic Usage
1. First run `make build` inside root directory.
2. Then run `make up` to start up the project for first time.

### Commands
To use this project, run this commands:

1. `make build` to build the project.
1. `make up-non-daemon` to creating containers.
2. `make up` to build the project, starting containers and show logs in terminal
3. `make start` to start containers if project has been up already.
4. `make stop` to stop containers.
4. `make restart` to restart containers.
5. `make shell-web` to shell access web container.
6. `make shell-db` to shell access db container.
7. `make shell-nginx` to shell access nginx container.
8. `make logs-web` to log access web container.
9. `make logs-db` to log access db container.
10. `make logs-nginx` to log access nginx container.
11. `make collectstatic` to put static files in static directory.
12. `make log-web` to log access web container.
13. `make log-db` to log access db container.
14. `make log-nginx` to log access nginx container.
14. `make restart` to restart containers.
15. `make tests` to run tests.
16. `make pull` to update containers.

-----

## Installation -  MacOS

1. Install [Docker Server](https://docs.docker.com/docker-for-mac/install/#install-and-run-docker-for-mac)
2. Git clone [project](https://gitlab.ddemo.ru/vireas/wikiworks)
3. Create file `local.py`
    ```sh
    $ scp src/settings/env/local.text src/settings/env/local.py
    ```
3. Add line `127.0.0.1 admin.localhost` to file `/ets/hosts`
    ```sh
    $ sudo nano /etc/hosts
    ```
4. Run the command in the project root folder to build the project
    ```sh
    $ docker-compose build
    ```
5. Next run the command to creating containers
    ```sh
    $ docker-compose up -d
    ```
5. Next run the command to init dump for domain
    ```sh
    $ docker-compose init_dump
    ```
6. Next run the command
    ```sh
    $ docker-compose add_celery_monitor
    ```
7. Next run the command to run project
    ```sh
    $ docker-compose start
    ```
8. Open browser (chrome) and go to url 'admin.localhost:8003' 
8. Command to stop project
    ```sh
    $ docker-compose stop
    ```


## Installation -  Windows

1. Install [Docker Server](https://docs.docker.com/docker-for-windows/install/)
2. Git clone [project](https://gitlab.ddemo.ru/vireas/wikiworks)
3. Create file `local.py`
    ```sh
    $ scp src/settings/env/local.text src/settings/env/local.py
    ```
3. Add line `127.0.0.1 admin.localhost` to file `c:\Windows\System32\Drivers\etc\hosts`

4. Run the command in the project root folder to build the project
    ```sh
    $ docker-compose build
    ```
5. Next run the command to creating containers
    ```sh
    $ docker-compose up -d
    ```
5. Next run the command to init dump for domain
    ```sh
    $ docker-compose init_dump
    ```
6. Next run the command
    ```sh
    $ docker-compose add_celery_monitor
    ```
7. Next run the command to run project
    ```sh
    $ docker-compose start
    ```
8. Open browser (chrome) and go to url 'admin.localhost:8003' 
8. Command to stop project
    ```sh
    $ docker-compose stop
    ```



## Installation -  Linux

### Installation docker

1. ...
    ```sh
    $  sudo apt install apt-transport-https ca-certificates curl software-properties-common
    ```
2. ...
    ```sh
    $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    ```
4. ...
    ```sh
    $ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
    ```
5. ...
    ```sh
    $ sudo apt update
    ```
5. ...
    ```sh
    $ apt-cache policy docker-ce
    ```
6. ...
    ```sh
    $ sudo apt install docker-ce
    ```
7. ...
    ```sh
    $ sudo systemctl status docker
    ```
5. ...
    ```sh
    $ sudo apt install docker-compose
    ```
    
### Run project

1. Git clone [project](https://gitlab.ddemo.ru/vireas/wikiworks)
3. Create file `local.py`
    ```sh
    $ scp src/settings/env/local.text src/settings/env/local.py
    ```
2. Add line `127.0.0.1 admin.localhost` to file `/ets/hosts`
    ```sh
    $ sudo nano /etc/hosts
    ```
3. Run the command in the project root folder to build the project
    ```sh
    $ sudo docker-compose build
    ```
4. Next run the command to creating containers
    ```sh
    $ sudo docker-compose up -d
    ```
5. Next run the command to init dump for domain
    ```sh
    $ sudo docker-compose init_dump
    ```
6. Next run the command
    ```sh
    $ sudo docker-compose add_celery_monitor
    ```
7. Next run the command to run project
    ```sh
    $ sudo docker-compose start
    ```
8. Open browser (chrome) and go to url 'admin.localhost:8003' 
9. Command to stop project
    ```sh
    $ sudo docker-compose stop