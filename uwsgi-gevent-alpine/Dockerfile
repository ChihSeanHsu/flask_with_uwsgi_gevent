FROM python:3.7-alpine
LABEL maintainer="s8901489@gmail.com"

WORKDIR /root
COPY requirements.txt /tmp/

RUN apk update && apk add \
    build-base \
    libuuid \
    pcre \
    mailcap \
    gcc \
    libc-dev \
    linux-headers \
    pcre-dev \
    curl \
    bash \
    libffi-dev \
    python3-dev \ 
    && pip install --upgrade pip \
    && pip install --no-cache-dir uwsgi gevent flask\
    && apk del \
    gcc \
    libc-dev \
    linux-headers \
    && rm -rf /tmp/*


COPY src /root
