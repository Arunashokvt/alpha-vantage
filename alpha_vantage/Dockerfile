# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
RUN apt-get update
RUN apt-get -y install redis-server
WORKDIR /alpha_vantage
COPY requirements.txt .
RUN pip install -r requirements.txt
# copy entrypoint.sh
COPY entrypoint.sh .
RUN sed -i 's/\r$//g' entrypoint.sh
RUN chmod +x entrypoint.sh
COPY . .
ENTRYPOINT ["./entrypoint.sh"]