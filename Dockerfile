FROM python:3.12-alpine3.22

COPY requirements.txt /temp/requirements.txt
COPY meetings /meetings
WORKDIR /meetings
EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password meet-user

USER meet-user