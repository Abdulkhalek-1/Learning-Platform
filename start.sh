#!/bin/bash 

python -m pip install --upgrade pip
python ./src/manage.py makemigrations --no-input
python ./src/manage.py migrate --no-input

python ./src/manage.py runserver 0.0.0.0:8000 --insecure