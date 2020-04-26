FROM python:3.7
MAINTAINER Dan Hormachea IngDevops
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["gunicorn"]
CMD ["-b 0.0.0.0:8000","--log-level=debug","app:app"]