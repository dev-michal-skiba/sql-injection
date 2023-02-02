FROM python:3.11.1
ENV PYTHONUNBUFFERED 1
COPY sql_injection /code
WORKDIR /code
RUN pip install -r requirements.txt
