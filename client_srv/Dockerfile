FROM python:3.11-slim

COPY ./client_srv /home/app

WORKDIR /home/app

RUN pip3.11 install --upgrade pip
RUN pip3.11 install poetry
RUN poetry install --only main

ENTRYPOINT [ "poetry", "run", "python", "./main.py" ]