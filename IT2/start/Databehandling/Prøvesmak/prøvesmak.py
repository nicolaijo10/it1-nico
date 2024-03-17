import csv
import matplotlib.pyplot as plt
from datetime import datetime

filnavn = "IT2/start/Databehandling/Prøvesmak/run.csv"

with open(filnavn, 'r', encoding="utf-8") as file:
    reader = csv.reader(file, delimiter = ',')
    header = next(reader) 
    data = list(reader)
    print(header)

countries = []

for row in data:
    land = row[7]

    countries.append(land) 


countriesMengde = {}

for mengde in countries:
    if mengde in countriesMengde:
        countriesMengde[mengde] += 1
    else:
        countriesMengde[mengde] = 1

for country in countriesMengde:
    countriesMengde[country] /= 52

sortert = sorted(countriesMengde.items(), key=lambda item: item[1])

høyeste = sortert[-3:]

laveste = sortert[:3]

print(høyeste)

print(laveste) 