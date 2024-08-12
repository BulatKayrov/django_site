#!/bin/bash

./manage.py migrate
./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser --username=admin --email=admin@example.com --noinput
./manage.py runserver 0.0.0.0:8000
