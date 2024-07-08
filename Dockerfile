# syntax=docker/dockerfile:1
FROM python:3.12.2-bookworm
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5005
COPY . .
# CMD ["flask","--app","test_app" ,"run", "--debug" ]
CMD ["flask","--app","test_app","run", "--host=0.0.0.0","--port=5005"]
