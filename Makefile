PYTHON := docker-compose run -u $(USERID):$(GROUPID) --rm web python
CELERY := docker-compose run -u $(USERID):$(GROUPID) --rm celery python

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
