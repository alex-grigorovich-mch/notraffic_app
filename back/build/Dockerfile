FROM python:3.10.12 AS base

RUN pip install poetry==1.7.1


ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRTIEBYTECODE=1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=0 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY ./poetry.lock pyproject.toml ./

FROM base as local

RUN poetry install

COPY . .

ENTRYPOINT ["./build/entrypoint-debug.sh"]

FROM base as dev

RUN poetry install

COPY . .

ENTRYPOINT ["./build/entrypoint-dev.sh"]

FROM base as prod

RUN poetry install
RUN rm -rf $POETRY_CACHE_DIR

COPY . .

ENTRYPOINT ["./build/entrypoint.sh"]
