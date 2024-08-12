FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY req.txt req.txt

RUN pip install -r req.txt

COPY . .
RUN chmod a+x /app/docker/*.sh