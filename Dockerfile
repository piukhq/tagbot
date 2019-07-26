FROM ghcr.io/binkhq/python:3.9

WORKDIR /app
ADD . .

RUN pipenv install --system --deploy --ignore-pipfile && \
    ln -s /app/main.py /usr/local/bin/tagbot
