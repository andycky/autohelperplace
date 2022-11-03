FROM python:3.9.13-slim-buster
ARG port

USER root
COPY . /autohelper2
WORKDIR /autohelper2

ENV PORT=$port

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils \
    && apt-get -y install curl \
    && apt-get install libgomp1

RUN chgrp -R 0 /autohelper2 \
    && chmod -R g=u /autohelper2 \
    && pip install pip --upgrade \
    && pip install -r requirements.txt
EXPOSE $PORT

CMD gunicorn app:server --bind 0.0.0.0:$PORT --preload
