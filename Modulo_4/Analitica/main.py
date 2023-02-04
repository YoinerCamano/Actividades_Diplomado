
import pika, sys, os

if __name__ == '__main__':

    url = 'mqp://guest:guest@rabbit:5672/%2f'
    params = pika.ConnectionParameters(host= url)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()

    channel.queue_declare(queue= 'mensajes')
    channel.queue_bind(exchange= 'amq.topic',queue= 'mensaje', routing_key= '#') 

    def callback(ch, method, properties, body):
        mensaje = body.decode("utf-8")
        print(" mensaje ".format(mensaje),flush= True)

    channel.basic_consume(queue='mensajes', on_message_callback=callback, auto_ack=True)

    channel.start_consuming()
