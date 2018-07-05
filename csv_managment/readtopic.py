from kafka import KafkaConsumer
print("Connecting...")
consumer = KafkaConsumer('test', bootstrap_servers=['10.33.1.131:29092'])
print("Waiting for message")
for msg in consumer:
    print(msg)