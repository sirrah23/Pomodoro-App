FROM python:3.5.2

RUN mkdir /app
WORKDIR /app

ADD . /app

RUN pip install pipenv
RUN pipenv install --system

EXPOSE 5000