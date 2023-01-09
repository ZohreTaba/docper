FROM python:3.11.1-slim-bullseye

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.3.1

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /copy

COPY poetry.lock  /copy/
COPY pyproject.toml /copy/

# Project initialization:
RUN poetry config virtualenvs.create false
RUN poetry install --only main --no-interaction

COPY ./src /copy/src

CMD gunicorn --bind 0.0.0.0:5000 src.main:app -w 4 -k uvicorn.workers.UvicornWorker --reload --access-logfile - --error-logfile - --log-level info

