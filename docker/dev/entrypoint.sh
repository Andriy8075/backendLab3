set -e

pip install -r docker/dev/requirements.txt

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

flask --app app run --host 0.0.0.0 --port 8080 --reload