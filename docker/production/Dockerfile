FROM python:3.11.3-slim-bullseye

WORKDIR /app

COPY docker/production/requirements.txt .

RUN python -m pip install --no-cache-dir -r requirements.txt
RUN apt-get update && \
    apt-get install -y curl gnupg2 lsb-release && \
    curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc | gpg --dearmor -o /usr/share/keyrings/postgresql-keyring.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/postgresql-keyring.gpg] http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list && \
    apt-get update && \
    apt-get install -y postgresql-client-15 && \
    rm -rf /var/lib/apt/lists/*

COPY docker/production/env env
RUN if [ -f env/.env ]; then \
        echo ".env file found, using it"; \
    else \
        echo ".env file not found, using .env.example"; \
        mv env/.env.example env/.env; \
    fi && \
    sed -i 's/\r$//' env/.env

COPY . /app

RUN echo "PATH_TO_DOT_ENV=env/.env" > app/path_to_dot_env

# Copy and set up entrypoint script
COPY docker/production/entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

EXPOSE 8070

ENTRYPOINT ["bash", "/app/entrypoint.sh"]
