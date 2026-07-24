#!/bin/sh

echo "-------------------------------------"
echo "EnterpriseHub Container Starting..."
echo "-------------------------------------"

python manage.py migrate

python manage.py collectstatic --noinput

echo "-------------------------------------"
echo "Starting Gunicorn..."
echo "-------------------------------------"

exec gunicorn \
    --config gunicorn.conf.py \
    config.wsgi:application