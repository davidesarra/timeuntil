FROM python:3.8.2-alpine3.11 AS poetry

RUN mkdir /src
WORKDIR /src

RUN apk update
RUN apk add build-base libffi-dev openssl-dev

RUN pip install poetry==1.0.5
ADD pyproject.toml pyproject.toml
ADD poetry.lock poetry.lock
RUN poetry export -f requirements.txt -o requirements.txt



FROM python:3.8.2-alpine3.11 AS pip

RUN mkdir /src
WORKDIR /src

RUN apk update
RUN apk add build-base libffi-dev openssl-dev

COPY --from=poetry /src/requirements.txt /src/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt



FROM alpine:3.11.5 AS yarn

RUN mkdir /src
WORKDIR /src

RUN apk update
RUN apk add yarn

ADD timeuntil/static/js/package.json package.json
ADD timeuntil/static/js/yarn.lock yarn.lock
RUN yarn install



FROM python:3.8.2-alpine3.11 AS production

RUN mkdir /src
WORKDIR /src

ADD timeuntil timeuntil
ADD uwsgi.yaml uwsgi.yaml

COPY --from=pip /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY --from=pip /usr/local/bin /usr/local/bin
COPY --from=yarn /src/node_modules /src/timeuntil/static/js/node_modules

ENV FLASK_APP timeuntil/app.py
EXPOSE 5000

CMD uwsgi --socket 0.0.0.0:5000 --protocol=http --yaml uwsgi.yaml
