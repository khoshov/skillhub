PYTHON := docker-compose run -u $(USERID):$(GROUPID) --rm django python
CELERY := docker-compose run -u $(USERID):$(GROUPID) --rm celery python
NPM := docker-compose run -u $(USERID):$(GROUPID) --rm node npm

up:
	docker-compose up

down:
	docker-compose down

build:
	docker-compose build

build-no-cache:
	docker-compose build --no-cache

collectstatic:
	$(PYTHON) manage.py collectstatic --noi

makemigrations:
	$(PYTHON) manage.py makemigrations ${app}

migrate:
	$(PYTHON) manage.py migrate ${app}

createsuperuser:
	$(PYTHON) manage.py createsuperuser

shell:
	$(PYTHON) manage.py shell_plus

celery:
	$(CELERY) manage.py shell_plus

reset_db:
	$(PYTHON) manage.py reset_db

npm_install_dev:
	$(NPM) i ${package} --save-dev
