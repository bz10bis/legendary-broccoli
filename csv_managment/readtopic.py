from kafka import KafkaConsumer

consumer = KafkaConsumer('test', bootstrap_servers=['10.33.1.131:29092'])

for msg in consumer:
    print(msg)