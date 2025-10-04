FROM python:3.11.3-slim-bullseye

WORKDIR /app

COPY docker/production/requirements.txt .

RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8070

CMD ["gunicorn", "--bind", "0.0.0.0:8070", "app:app"]