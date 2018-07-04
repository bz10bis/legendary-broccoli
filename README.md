# Projet KAFKA Streamings

## Choix du sujet

Parmis les deux sujets proposés dans le cadre du projet de semaine thématique, nous avons choisi le second sujet, à savoir le traitement de données météorologiques.

## Workflow 

1) Le fichier CSV fourni pour le projet est lu ligne par ligne et parsé en python dans le fichier csv_managment/split_and_produce.py. Chacune des lignes est ensuite produite dans un broker local [10.33.1.131:29092].

2) Les messages sont consommés dans une étape intermédiaire, et les valeurs issues de la clé "Coordonnees" des messages sont utilisées pour la détermination des départements. Cette information complémentaire reçue, les données sont aggrégés en deux flux : Departements et Villes, contenant la température minimale et maximale, et la pression minimale et maximale de chacun des aggregats.

3) Ces deux streams sont consommés par un serveur CherryPy, qui expose les aggregats sous la forme d'une API REST.
