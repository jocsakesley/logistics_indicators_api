FROM python:3.11-slim

WORKDIR /app

COPY ./requirements.txt /app/

RUN pip3 --no-cache-dir install -r requirements.txt

COPY . /app


ENTRYPOINT [ "gunicorn", "--bind", "0.0.0.0:8000", "src.main:app" ]