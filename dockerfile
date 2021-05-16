FROM python:latest
WORKDIR /website
ADD . .
RUN pip install -r /website/requirements.txt
EXPOSE 8000
CMD gunicorn --bind 0.0.0.0:8000 server:app 