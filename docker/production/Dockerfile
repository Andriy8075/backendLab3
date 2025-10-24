FROM python:3.11.3-slim-bullseye

WORKDIR /app

COPY docker/production/requirements.txt .

RUN python -m pip install --no-cache-dir -r requirements.txt
RUN apt-get update && \
    apt-get install -y postgresql-client curl && \
    rm -rf /var/lib/apt/lists/*

COPY docker/production/env env
RUN if [ -f env/.env ]; then \
        echo ".env file found, using it"; \
    else \
        echo ".env file not found, using .env.example"; \
        mv env/.env.example env/.env; \
    fi

COPY . /app

RUN echo "PATH_TO_DOT_ENV=env/.env" > app/path_to_dot_env
