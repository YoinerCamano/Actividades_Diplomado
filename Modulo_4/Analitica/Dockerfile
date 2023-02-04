FROM python:3.9.16

WORKDIR /app 

RUN apt-get update 

RUN apt-get -y install python3-aiohttp

RUN pip install influx-client==1.36

RUN pip install pika 

COPY Modulo_4/Analitica/main.py /app/main.py

CMD ["python","/app/main.py"]