#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py makemigrations
python manage.py migrate
python manage.py migrate --run-syncdb
service redis-server start --daemonize yes
celery -A alpha_vantage worker --loglevel=info --detach
exec "$@"