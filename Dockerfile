FROM python:3.8-slim

RUN mkdir /src
WORKDIR /src

RUN apt-get update
RUN apt-get -y install curl gcc gnupg
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update
RUN apt-get -y install yarn

RUN pip install --upgrade pip

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

ADD timeuntil timeuntil
ADD setup.py setup.py
RUN pip install -e .

WORKDIR /src/timeuntil/static/js
RUN yarn install
WORKDIR /src

ENV FLASK_APP timeuntil/app.py
ADD uwsgi.yaml uwsgi.yaml
EXPOSE 5000

CMD uwsgi --socket 0.0.0.0:5000 --protocol=http --yaml uwsgi.yaml
