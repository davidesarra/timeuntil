FROM python:3.8-slim

RUN mkdir /src
WORKDIR /src

RUN apt-get update
RUN apt-get -y install gcc

RUN pip install --upgrade pip

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

ADD timeuntil timeuntil
ADD setup.py setup.py
RUN pip install -e .

ENV FLASK_APP timeuntil/app.py
ADD uwsgi.yaml uwsgi.yaml
EXPOSE 5000

CMD uwsgi --socket 0.0.0.0:5000 --protocol=http --yaml uwsgi.yaml
