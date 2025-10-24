set -e

until pg_isready -h db -p 5432 -U postgres; do
  echo "Waiting for PostgreSQL..."
  sleep 2
done

if [ ! -d "./app/migrations" ]; then
  echo "Migrations folder not found. Initializing migrations..."
  flask db init
  flask db migrate -m "initial migration"
fi
flask db upgrade

gunicorn --bind 0.0.0.0:8070 app:app