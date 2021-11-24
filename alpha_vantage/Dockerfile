# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
RUN apt-get update
RUN apt-get -y install redis-server
WORKDIR /alpha_vantage
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .