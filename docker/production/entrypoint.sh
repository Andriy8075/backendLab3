#!/bin/bash
set -e

source env/.env

export PGSSLMODE=require

until pg_isready -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USERNAME" --dbname="$DB_DATABASE"; do
  echo "Waiting for PostgreSQL at $DB_HOST:$DB_PORT..."
  sleep 2
done


gunicorn --bind 0.0.0.0:8070 --timeout 120 --workers 2 app:app