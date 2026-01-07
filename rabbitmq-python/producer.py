#!/usr/bin/env python
# coding=utf-8
import pika

RABBITMQ_HOST = "192.168.41.133"
credentials = pika.PlainCredentials('admin', 'admin')

connection = pika.BlockingConnection(
    pika.ConnectionParameters(RABBITMQ_HOST, credentials=credentials)
)
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='', routing_key='hello', body='Hello Netology!')
connection.close()

print(" [x] Message sent")
