This starter provides a basic setup to help quickly start prototyping a flask app with graphql.

Not intended for production use.

## Setup
Install [Docker](https://docs.docker.com/engine/install/)

Install poetry and pre-commit
```
pip install poetry
poetry install
poetry run pre-commit install
```

### db
Connect to
```postgres://localhost:5432/postgres```
and run the following query:
```
CREATE DATABASE app;
```

## Local environment
This will give you the ability to generate alembic migrations without going inside docker container.

```
export POSTGRES_USER=postgres
export POSTGRES_PASSWORD=postgres
export POSTGRES_DB=postgres
export APPLICATION_DB=app
export DB_HOSTNAME=localhost
```

Run command inside the same venv that `poetry` installs dependencies in,
useful for creating alembic revisions or running migrations.
```
poetry run <command>
```

## Run
```
docker-compose up
```
There's no need to restart containers when introducing changes to code (hot reload works),
but sometimes those changes will crash `gunicorn` server and a restart will
solve it.

### When running migrations
This command will run only the `db` service, useful when applying migrations from local environment.
```
docker-compose up db
```

### When introducing new package make sure to run
```
docker-compose build
```

## IDE
Mark `src` directory as `Sources Root` for code inspection to work properly.
