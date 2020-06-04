FROM python:3.7-slim
LABEL maintainer="s8901489@gmail.com"

WORKDIR /root

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean \
    && pip install --upgrade pip \
    && pip install --no-cache-dir uwsgi gevent flask boto3 pytest simplejson\
    && rm -rf /tmp/* \
    && apt-get remove -y gcc

