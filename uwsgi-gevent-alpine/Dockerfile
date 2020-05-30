FROM python:3.7-alpine
LABEL maintainer="s8901489@gmail.com"

WORKDIR /root

RUN apk update && apk add \
    build-base \
    libffi-dev \
    bash \
    && pip install --upgrade pip \
    && pip install --no-cache-dir uwsgi gevent flask boto3\
    && apk del \
    build-base \
    libffi-dev \
    && rm -rf /tmp/*
