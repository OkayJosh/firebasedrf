FROM python:3.8-slim

ENV PROJECT_ROOT /app
WORKDIR $PROJECT_ROOT

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app
