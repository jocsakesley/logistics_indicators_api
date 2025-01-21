FROM python:3.11-slim-buster

WORKDIR /app

COPY ./requirements.txt /app/

RUN pip --no-cache-dir install -r requirements.txt && \
    pip3 install gunicorn

COPY . /app


ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8000", \
            "--access-logfile", "-", \
            "--error-logfile", "-", \
            "--log-level", "info", \
            "src.main:app"]