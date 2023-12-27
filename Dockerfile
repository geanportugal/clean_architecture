FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

# netcat é necessário para o arquivo ./wait-for
RUN apt-get -y update && apt-get install -y \
    gcc \
    git \
    libcurl4-openssl-dev \
    postgresql-server-dev-all \
    libssl-dev \
    netcat-traditional \
    awscli \
    jq

# Cria o diretorio ssh para salvar os ssh keys
RUN mkdir -p -m 0600 ~/.ssh && ssh-keyscan github.com >> ~/.ssh/known_hosts

RUN pip install --upgrade pip && pip install pip-tools

COPY ./requirements/requirements.txt /tmp/dev.txt
RUN pip install -r /tmp/dev.txt

WORKDIR /src

EXPOSE 5000
