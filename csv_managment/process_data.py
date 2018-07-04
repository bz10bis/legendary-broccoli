from kafka import KafkaProducer
import time

config = {
    "to": "meteo",
    "bootstrap": "localhost:29092",
    "zookeeper": "localhost:32181",
    "source_file": "synop-data-meteo-cleaned"
}

producer = KafkaProducer(bootstrap_servers=[config['bootstrap']])

producer.send(config['to'], b'hello')
