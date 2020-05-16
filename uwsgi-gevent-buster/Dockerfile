FROM python:3.7
LABEL maintainer="s8901489@gmail.com"

WORKDIR /root

RUN pip install --upgrade pip \
    && pip install --no-cache-dir uwsgi gevent flask\
    && rm -rf /tmp/*
