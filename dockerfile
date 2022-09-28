FROM python:3.10-alpine
WORKDIR /myshop/
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
COPY requirements.txt /myshop/
RUN pip install -r requirements.txt
COPY . /myshop/