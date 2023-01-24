FROM docker.io/python:3.11-alpine

WORKDIR /app
ADD main.py .

RUN pip install requests click && \
    ln -s /app/main.py /usr/local/bin/tagbot
