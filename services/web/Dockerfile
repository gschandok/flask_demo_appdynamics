# pull official base image
FROM python:3.8.1-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
COPY startup.sh /startup.sh

COPY ./appdynamics.cfg /usr/src/app/appdynamics.cfg

# copy project
COPY . /usr/src/app/

RUN chmod +x /startup.sh

# run entrypoint.sh
ENTRYPOINT ["/startup.sh"]