#!/bin/bash

python manage.py migrate
python -m debugpy --listen 0.0.0.0:3001 manage.py runserver 0.0.0.0:8000
