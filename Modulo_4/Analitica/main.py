
import pika
import os
import math
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

DIA_100K = 100000
DIA_5k = 5000

class Analitica():
    prom_list = []
    cont_prom = 0
    prom_end = 0
    hight_100k = 0
    low_5k = 0
    value_previus = 0
    days_consecutive = 0
    value_max = -math.inf
    value_min = math.inf
    better = -math.inf
    best_run = 0
    influx_bucket = 'rabbit'
    influx_token = 'TOKEN_SECRETO'
    influx_url = 'http://influxdb:8086'
    influx_org = 'org'

    def add_max(self,_medida):
        if _medida > self.value_max:
            self.value_max =_medida
            self.write("Pasos", "Maximo",_medida)

    def add_min(self, _medida):
        if _medida < self.value_min:
            self.value_min =_medida
            self.write("Pasos", "Minimo",_medida)   

    def add_prom(self, _medida):
        self.prom_list.append(_medida)
        self.cont_prom = len(self.prom_list)
        self.prom_end = (sum(self.prom_list)/(self.cont_prom))
        self.write("Pasos", "Promedio",float(self.prom_end))

    def hight_10(self, _medida):
        if _medida > 100000:
            self.hight_100k += 1
            print("Más de 100.000 {}".format(self.hight_100k), flush=True)
        self.write('Pasos', "+10.000", int(self.hight_100k))

    def low_5(self, _medida):
        if _medida < 5000:
            self.low_5k += 1
            print("Menos de 5.000 {}".format(self.low_5k), flush=True)
            self.write_db('Pasos', "-50000", int(self.low_5k))
        else:
            self.write_db('Pasos', "-50000", int(self.low_5k))

    def consecutive(self, _medida):
        if _medida >= self.value_previus:
            print("Mejora", flush=True)
            self.better = _medida
            self.days_consecutive += 1
            self.best_run = self.days_consecutive
            self.write("Pasos","")

        else:
            self.days_consecutive = 0

    def write(self,tag,key,value): 

        client = InfluxDBClient(url=self.influx_url, token=self.influx_token, org=self.influx_org)
        write_api = client.write_api(write_options=SYNCHRONOUS)

        punto = Point("Analitica").tag("Descriptivas", tag).field(key,value)
        write_api.write(bucket=self.influx_bucket, record=punto)


    
    def take_steps(self, _mensaje):
        mensaje = _mensaje.split("=")
        medida = float(mensaje[-1])
        print("medida {}".format(medida), flush=True)
        self.add_max(medida)
        self.add_min(medida)
        self.add_prom(medida)
        self.hight_10(medida)
        self.low_5(medida)
        self.consecutive(medida)
        
if __name__ == '__main__':

  analitica = Analitica()

  url = os.environ.get('AMQP_URL', 'amqp://guest:guest@rabbit:5672/%2f')
  params = pika.URLParameters(url)
  connection = pika.BlockingConnection(params)
  channel = connection.channel()


  channel.queue_declare(queue='mensajes')
  channel.queue_bind(exchange='amq.topic', queue='mensajes', routing_key='#')   

  def callback(ch, method, properties, body):
    global analitica
    mensaje = body.decode("utf-8")
    analitica.take_steps(mensaje)

  channel.basic_consume(queue='mensajes', on_message_callback=callback, auto_ack=True)
  channel.start_consuming()





