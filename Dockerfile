FROM ubuntu
RUN apt-get update -y
RUN apt-get install python3 python3-pip -y
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
CMD ["uvicorn", "app.main:app", "--port", "8080"]
