import time
import json
from kafka import KafkaProducer

in_file = "../datasets/synop-data-meteo-cleaned.csv"

## Definition de l'adresse du broker
broker_adr = "10.33.1.131:29092" # remote
# broker_adr = "10.33.2.217:9092" # local
target_topic = 'raw_station_test'

## definition du producer, sur lequel vont etre envoyés les données
producer = KafkaProducer(bootstrap_servers=[broker_adr])

# producer.send('test', b"test")

## ouverture du fichier, et parsing des différentes données
with open(in_file, "r") as ff:
	print("Launching process")
	for idx, line in enumerate(ff):

		if idx == 0:
			continue

		if idx > 11:
			exit(0)

		data = {}
		split = line.split(";")

		IDOMMstation = split[0].strip()
		Dateprelevement = split[1].strip()
		Pressionauniveaumer = split[2].strip()
		Temperature = split[3].strip()
		Pointderosee = split[4].strip()
		Humidite = split[5].strip()
		Coordonnees = split[6].strip()
		Nom = split[7].strip()

		try:
			new_temp = "%.3f" % (float(Temperature)/10)
		except Exception as e:
			print(e)
			new_temp = ""

		data['IDOMMstation'] = IDOMMstation
		data['Dateprelevement'] = Dateprelevement
		data['Pressionauniveaumer'] = Pressionauniveaumer
		data['Temperature'] = str(new_temp)
		data['Pointderosee'] = Pointderosee
		data['Humidite'] = Humidite
		data['Coordonnees'] = Coordonnees
		data['Nom'] = Nom

		## generation d'un json contenant les données de la ligne
		json_data = json.dumps(data)

		## envoi des données au producer, dans le topic "raw_station_data"
		producer.send(target_topic, json_data.encode("utf-8"))

		## definition de la fréquence d'envoi des données
		time.sleep(0.5)
