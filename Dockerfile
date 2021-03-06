FROM python:3.8.2

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /app
COPY ./app /app