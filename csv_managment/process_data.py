from kafka import KafkaProducer
import time

config = {
    "to": "meteo",
    "bootstrap": "10.33.1.131:29092",
    #"bootstrap": "10.33.0.248:9092",
    "zookeeper": "localhost:32181",
    "source_file": "synop-data-meteo-cleaned"
}

producer = KafkaProducer(bootstrap_servers=[config['bootstrap']])
print("Sending data")
producer.send("test", b'lorem ipsum2')
