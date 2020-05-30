FROM python:3.7
LABEL maintainer="s8901489@gmail.com"

WORKDIR /root

RUN apt-get update \
    && apt-get install -y netcat \
    && pip install --upgrade pip \
    && pip install --no-cache-dir uwsgi gevent flask boto3 pytest\
    && rm -rf /tmp/*
