FROM python:3.7
MAINTAINER Roberto Sanchez <robersh0@gmail.com>

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y poppler-utils tesseract-ocr

COPY ./ ./app
WORKDIR ./app

RUN pip3 install -r requirements/dev.txt

CMD flask run --host 0.0.0.0 --port 5000