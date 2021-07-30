# pull official base image
FROM python:3.9-slim-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH="$PYTHONPATH:/app"

# install dependencies
RUN pip install --upgrade pip
RUN pip install poetry
COPY ./src/poetry.lock ./src/pyproject.toml /app/

# set working directory
WORKDIR /app

RUN poetry install --no-dev

# copy project
COPY ./src/ /app/
