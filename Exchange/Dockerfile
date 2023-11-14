FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "Exchange.wsgi", "--bind", "0.0.0.0:8000", "--workers", "1", "--log-level", "debug", "--timeout", "300", "--graceful-timeout", "300", "--keep-alive", "300", "--max-requests", "1000", "--max-requests-jitter", "1000", "--threads", "1", "--worker-class", "gthread", "--worker-tmp-dir", "/dev/shm", "--preload", "--access-logfile", "-", "--error-logfile", "-"]
