FROM python:3.8

WORKDIR /usr/srs/app

COPY requisite.txt ./

RUN pip install --no-cache-dir -r requisite.txt 

EXPOSE 8000

COPY . . 

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]

