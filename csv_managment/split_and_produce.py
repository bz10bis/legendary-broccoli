import time
import json
from kafka import KafkaProducer

<<<<<<< HEAD
in_file = "synop-data-meteo-cleaned.csv"


## Definition de l'adresse du broker
broker_adr = "10.33.1.131:29092" # remote
# broker_adr = "10.33.2.217:9092" # local

## definition du producer, sur lequel vont etre envoyés les données
producer = KafkaProducer(bootstrap_servers=[broker_adr])

## ouverture du fichier, et parsing des différentes données
with open(in_file, "r") as ff:
=======
source_file = "../datasets/synop-data-meteo-cleaned.csv"

broker_adr = "localhost:29092"
producer = KafkaProducer(bootstrap_servers=[broker_adr])

with open(source_file, "rb") as ff:
>>>>>>> 1e8c6f85efbf643bc79060dfe23692831a0cff3d
	for idx, line in enumerate(ff):

		if idx == 0:
			continue

		data = {}
		split = line.split(";")

		IDOMMstation = split[0].strip()
		Date = split[1].strip()
		Pressionauniveaumer = split[2].strip()
		Temperature = split[3].strip()
		Pointderosee = split[4].strip()
		Humidite = split[5].strip()
		Coordonnees = split[6].strip()
		Nom = split[7].strip()

		data['IDOMMstation'] = IDOMMstation
		data['Date'] = Date
		data['Pressionauniveaumer'] = Pressionauniveaumer
		data['Temperature'] = Temperature
		data['Pointderosee'] = Pointderosee
		data['Humidite'] = Humidite
		data['Coordonnees'] = Coordonnees
		data['Nom'] = Nom

		## generation d'un json contenant les données de la ligne
		json_data = json.dumps(data)

		## envoi des données au producer
		producer.send('meteo', json_data.encode("utf-8"))

		## definition du temps de latence d'envoi des données
		time.sleep(0.1)
