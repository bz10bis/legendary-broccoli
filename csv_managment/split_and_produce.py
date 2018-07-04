import time
import json
from kafka import KafkaProducer

source_file = "../datasets/synop-data-meteo-cleaned.csv"

broker_adr = "localhost:29092"
producer = KafkaProducer(bootstrap_servers=[broker_adr])

with open(source_file, "rb") as ff:
	for idx, line in enumerate(ff):

		if idx == 0:
			continue

		data = {}
		split = line.split(b";")

		IDOMMstation = split[0].strip()
		Date = split[1].strip()
		Pressionauniveaumer = split[2].strip()
		Temperature = split[3].strip()
		Pointderosee = split[4].strip()
		Humidite = split[5].strip()
		Coordonnees = split[6].strip()
		Nom = split[7].strip()

		data[b'IDOMMstation'] = IDOMMstation
		data[b'Date'] = Date
		data[b'Pressionauniveaumer'] = Pressionauniveaumer
		data[b'Temperature'] = Temperature
		data[b'Pointderosee'] = Pointderosee
		data[b'Humidite'] = Humidite
		data[b'Coordonnees'] = Coordonnees
		data[b'Nom'] = Nom

		# json_data = json.dumps(data)
		# json_data = json.dumps(data)

		producer.send('meteo', data)
		print(data)

		time.sleep(0.5)
