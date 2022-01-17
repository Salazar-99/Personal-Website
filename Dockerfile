FROM python:3.8.2

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /app
COPY ./app /app
COPY .env /app/.env

ENV ENVIRONMENT=production

CMD gunicorn --bind 0.0.0.0:5000 --access-logfile - --error-logfile - --reload "app:create_app('production')"