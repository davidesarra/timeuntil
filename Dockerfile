FROM python:3.8-slim

RUN mkdir /src
WORKDIR /src

RUN pip install --upgrade pip

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

ADD timeuntil timeuntil
ADD setup.py setup.py
RUN pip install -e .

ENV FLASK_APP timeuntil/app.py

EXPOSE 5000
CMD [ "flask", "run", "--host=0.0.0.0" ]
