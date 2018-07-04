import time
import json

file = "synop-data-meteo-cleaned.csv"

with open(file, "r") as ff:
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

		json_data = json.dumps(data)

		print(json_data)

		time.sleep(0.5)
