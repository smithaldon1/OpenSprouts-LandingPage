FROM python:3.10-slim-buster

RUN apt-get update \
    && apt-get install python3-dev default-libmysqlclient-dev build-essential -y

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["python3", "application.py"] 