#base image
FROM python:3.8.3-slim

ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends make libpq-dev gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


WORKDIR /app


COPY  requirements.txt /app/

RUN pip install -r requirements.txt 


COPY . /app
