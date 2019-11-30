#!/usr/bin/env sh

# Check database connection
echo "Waiting for database..."
while ! nc -z $DB_HOST 5432; do
  echo "Database connection failed, retrying in 3 secs..."
  sleep 3s
done

python manage.py migrate
python manage.py collectstatic --no-input --clear -v 0

exec "$@"
