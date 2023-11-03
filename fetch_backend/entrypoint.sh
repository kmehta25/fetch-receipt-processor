#!/bin/sh

# Wait for the PostgreSQL container to be ready
while ! nc -z postgres_db 5432; do
  sleep 1
done

# Apply database migrations
python manage.py migrate

# Start the Django application
python manage.py runserver 0.0.0.0:8000
