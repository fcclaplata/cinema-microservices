FROM python:3.6

ENV PYTHONUNBUFFERED 1

WORKDIR /code

ADD requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /code/src

ADD ./src .

EXPOSE 8080

CMD ["apistar", "run", "--host", "0.0.0.0", "--port", "8080"]

