#!/bin/bash

python manage.py migrate
gunicorn config.wsgi --config ./build/gunicorn.conf.py
