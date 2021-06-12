PYTHON := docker-compose run -u $(USERID):$(GROUPID) --rm web python

up:
	docker-compose up

down:
	docker-compose down

build:
	docker-compose build

build-no-cache:
	docker-compose build --no-cache

makemigrations:
	$(PYTHON) manage.py makemigrations ${app}

migrate:
	$(PYTHON) manage.py migrate ${app}

createsuperuser:
	$(PYTHON) manage.py createsuperuser

shell:
	$(PYTHON) manage.py shell_plus
