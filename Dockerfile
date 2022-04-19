FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y sudo vim && apt-get upgrade -y

COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip -r /requirements.txt && pip install -U "watchdog[watchmedo]"

RUN mkdir /bookrecipes
WORKDIR /bookrecipes
COPY ./bookrecipes /bookrecipes

RUN adduser --disabled-password --gecos '' python
RUN adduser python sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER python
