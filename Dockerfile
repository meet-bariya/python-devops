FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY ./src /app/src

COPY main.py /app/

EXPOSE 8000

CMD ["main.py"]

ENTRYPOINT [ "python" ]