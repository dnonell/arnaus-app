FROM python:alpine AS base

RUN apk add --update --no-cache curl

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

FROM base AS dev

COPY ./dev-requirements.txt /code/dev-requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/dev-requirements.txt

COPY . /code

CMD ["fastapi", "dev", "app/main.py", "--port", "8080"]

FROM base AS prod

COPY ./app /code/app

CMD ["fastapi", "run", "app/main.py", "--port", "8080"]
