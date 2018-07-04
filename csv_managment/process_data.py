from kafka import KafkaProducer
import time

config = {
    "to": "meteo",
    "bootstrap": "localhost:29092",
    "zookeeper": "localhost:32181",
    "source_file": "synop-data-meteo-cleaned"
}

producer = KafkaProducer(boostrap_servers=[config['boostrap']])

def main():
    print("##### CSV PARSER #####")

if __name__ == '__main__':
    main()