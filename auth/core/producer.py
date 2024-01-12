from confluent_kafka import Producer
import os

# El que envía
producer = Producer({
    'bootstrap.servers': os.environ.get('KAFKA_BOOTSTRAP_SERVER'),
    'security.protocol': os.environ.get('KAFKA_SECURITY_PROTOCOL'),
    'sasl.username': os.environ.get('KAFKA_USERNAME'),
    'sasl.password': os.environ.get('KAFKA_PASSWORD'),
    'sasl.mechanism': 'PLAIN',
})