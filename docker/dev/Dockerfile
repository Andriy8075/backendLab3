FROM python:3.11.3-slim-bullseye

RUN apt-get update && \
    apt-get install -y postgresql-client curl && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /var/www/