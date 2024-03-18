
#Denne koden finner ut hvor mange utøver som kommer fra forksjellige land og viser de 3 landene med flest og de 3 landene med færrest 
'''
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

'''




#Denne koden delen atletene inn i aldergruppoer og finner ut hvor mange det er i hver aldergruppe, dne finner også ut hjennomsnttlig distanse og hvor lang tid som ble trent per gruppe.

'''
import csv
import matplotlib.pyplot as plt

filnavn = "IT2/start/Databehandling/Prøvesmak/run.csv"

with open(filnavn, 'r', encoding="utf-8") as fil:
    leser = csv.DictReader(fil)
    data = list(leser)

unge_utøvere = []
middelaldrende_utøvere = []
eldre_utøvere = []

for rad in data:
    aldersgruppe = rad['age_group']
    if '18 - 34' in aldersgruppe:
        unge_utøvere.append(rad)
    elif '35 - 54' in aldersgruppe:
        middelaldrende_utøvere.append(rad)
    elif '55 +' in aldersgruppe:
        eldre_utøvere.append(rad)


def analyser_treningsmønstre(utøvere, gruppe_navn):
    distanser = [float(rad['distance']) for rad in utøvere]
    varigheter = [float(rad['duration']) for rad in utøvere]
    if len(distanser) > 0:
        gjennomsnittlig_distanse = sum(distanser) / len(distanser)
        gjennomsnittlig_varighet = sum(varigheter) / len(varigheter)
        print(f"Gjennomsnittlig distanse for {gruppe_navn}: {gjennomsnittlig_distanse:.2f} km")
        print(f"Gjennomsnittlig varighet for {gruppe_navn}: {gjennomsnittlig_varighet:.2f} minutter")
    else:
        print(f"Ingen utøvere i gruppen {gruppe_navn}.")


analyser_treningsmønstre(unge_utøvere, 'unge utøvere')
analyser_treningsmønstre(middelaldrende_utøvere, 'middelaldrende utøvere')
analyser_treningsmønstre(eldre_utøvere, 'eldre utøvere')

antall_unge_utøvere = len(unge_utøvere)
antall_middelaldrende_utøvere = len(middelaldrende_utøvere)
antall_eldre_utøvere = len(eldre_utøvere)

etiketter = ['Unge Utøvere', 'Middelaldrende Utøvere', 'Eldre Utøvere']
antall_utøvere = [antall_unge_utøvere, antall_middelaldrende_utøvere, antall_eldre_utøvere]

antall_unge_utøvere_per_uke = antall_unge_utøvere / 52
antall_middelaldrende_utøvere_per_uke = antall_middelaldrende_utøvere / 52
antall_eldre_utøvere_per_uke = antall_eldre_utøvere / 52

plt.bar(range(len(etiketter)), [antall_unge_utøvere_per_uke, antall_middelaldrende_utøvere_per_uke, antall_eldre_utøvere_per_uke])
plt.title('Antall Utøvere i Hver Aldersgruppe')
plt.xlabel('Aldersgruppe')
plt.ylabel('Antall Utøvere')

plt.xticks(range(len(etiketter)), etiketter)

for i, num in enumerate([antall_unge_utøvere_per_uke, antall_middelaldrende_utøvere_per_uke, antall_eldre_utøvere_per_uke]):
    plt.text(i, num + 0.5, f'{num:.2f}', ha='center')

plt.show()

'''

#Denne koden deler atletene inn i Kjønn og finner ut hvor mange det er i hver Kjønnsgruppe, dne finner også ut hjennomsnttlig distanse og hvor lang tid som ble trent per gruppe.

'''
import csv
import matplotlib.pyplot as plt

filnavn = "IT2/start/Databehandling/Prøvesmak/run.csv"

with open(filnavn, 'r', encoding="utf-8") as fil:
    leser = csv.DictReader(fil)
    data = list(leser)

mannlige_utøvere = []
kvinnelige_utøvere = []

for rad in data:
    kjønn = rad['gender']
    if 'M' in kjønn:
        mannlige_utøvere.append(rad)
    elif 'F' in kjønn:
        kvinnelige_utøvere.append(rad)


def analyser_treningsmønstre(utøvere, gruppe_navn):
    distanser = [float(rad['distance']) for rad in utøvere]
    varigheter = [float(rad['duration']) for rad in utøvere]
    if len(distanser) > 0:
        gjennomsnittlig_distanse = sum(distanser) / len(distanser)
        gjennomsnittlig_varighet = sum(varigheter) / len(varigheter)
        print(f"Gjennomsnittlig distanse for {gruppe_navn}: {gjennomsnittlig_distanse:.2f} km")
        print(f"Gjennomsnittlig varighet for {gruppe_navn}: {gjennomsnittlig_varighet:.2f} minutter")
    else:
        print(f"Ingen utøvere i gruppen {gruppe_navn}.")


analyser_treningsmønstre(mannlige_utøvere, 'menn')
analyser_treningsmønstre(kvinnelige_utøvere, 'kvinner')

antall_mannlige_utøvere = len(mannlige_utøvere)
antall_kvinnelige_utøvere = len(kvinnelige_utøvere)

etiketter = ['Menn', 'Kvinner']
antall_utøvere = [antall_mannlige_utøvere, antall_kvinnelige_utøvere]

antall_mannlige_utøvere_per_uke = antall_mannlige_utøvere / 52
antall_kvinnelige_utøvere_per_uke = antall_kvinnelige_utøvere / 52

plt.bar(range(len(etiketter)), [antall_mannlige_utøvere_per_uke, antall_kvinnelige_utøvere_per_uke])
plt.title('Antall Utøvere etter Kjønn')
plt.xlabel('Kjønn')
plt.ylabel('Antall Utøvere per Uke')

plt.xticks(range(len(etiketter)), etiketter)

for i, num in enumerate([antall_mannlige_utøvere_per_uke, antall_kvinnelige_utøvere_per_uke]):
    plt.text(i, num + 0.5, f'{num:.2f}', ha='center')

plt.show()
'''


#Denne kombinerer de 2 forrige og lager diagram for både alder og kjønnsgruppe
'''
import csv
import matplotlib.pyplot as plt

filnavn = "IT2/start/Databehandling/Prøvesmak/run.csv"

with open(filnavn, 'r', encoding="utf-8") as fil:
    leser = csv.DictReader(fil)
    data = list(leser)


unge_menn = []
unge_kvinner = []
middelaldrende_menn = []
middelaldrende_kvinner = []
eldre_menn = []
eldre_kvinner = []

for rad in data:
    aldersgruppe = rad['age_group']
    kjønn = rad['gender']
    if '18 - 34' in aldersgruppe:
        if kjønn == 'M':
            unge_menn.append(rad)
        else:
            unge_kvinner.append(rad)
    elif '35 - 54' in aldersgruppe:
        if kjønn == 'M':
            middelaldrende_menn.append(rad)
        else:
            middelaldrende_kvinner.append(rad)
    elif '55 +' in aldersgruppe:
        if kjønn == 'M':
            eldre_menn.append(rad)
        else:
            eldre_kvinner.append(rad)


def analyser_treningsmønstre(utøvere, gruppe_navn):
    distanser = [float(rad['distance']) for rad in utøvere]
    varigheter = [float(rad['duration']) for rad in utøvere]
    if len(distanser) > 0:
        gjennomsnittlig_distanse = sum(distanser) / len(distanser)
        gjennomsnittlig_varighet = sum(varigheter) / len(varigheter)
        print(f"Gjennomsnittlig distanse for {gruppe_navn}: {gjennomsnittlig_distanse:.2f} km")
        print(f"Gjennomsnittlig varighet for {gruppe_navn}: {gjennomsnittlig_varighet:.2f} minutter")
    else:
        print(f"Ingen utøvere i gruppen {gruppe_navn}.")


analyser_treningsmønstre(unge_menn, 'unge menn')
analyser_treningsmønstre(unge_kvinner, 'unge kvinner')
analyser_treningsmønstre(middelaldrende_menn, 'middelaldrende menn')
analyser_treningsmønstre(middelaldrende_kvinner, 'middelaldrende kvinner')
analyser_treningsmønstre(eldre_menn, 'eldre menn')
analyser_treningsmønstre(eldre_kvinner, 'eldre kvinner')


antall_unge_menn = len(unge_menn) / 52
antall_unge_kvinner = len(unge_kvinner) / 52
antall_middelaldrende_menn = len(middelaldrende_menn) / 52
antall_middelaldrende_kvinner = len(middelaldrende_kvinner) / 52
antall_eldre_menn = len(eldre_menn) / 52
antall_eldre_kvinner = len(eldre_kvinner) / 52


etiketter = ['Unge(M)', 'Unge(F)', 'Middel(M)', 'Middel(F)', 'Eldre(M)', 'Eldre(F)']
antall_utøvere_per_uke = [antall_unge_menn, antall_unge_kvinner, antall_middelaldrende_menn, antall_middelaldrende_kvinner, antall_eldre_menn, antall_eldre_kvinner]

plt.bar(range(len(etiketter)), antall_utøvere_per_uke)
plt.title('Antall Utøvere i Hver Aldersgruppe og Kjønn')
plt.xlabel('Aldersgruppe og Kjønn')
plt.ylabel('Antall Utøvere per Uke')
plt.xticks(range(len(etiketter)), etiketter)

for i, num in enumerate(antall_utøvere_per_uke):
    plt.text(i, num + 0.5, f'{num:.2f}', ha='center')

plt.show()

'''

#Kakediagram versjon:
'''
etiketter = ['Unge Menn', 'Unge Kvinner', 'Middelaldrende Menn', 'Middelaldrende Kvinner', 'Eldre Menn', 'Eldre Kvinner']
antall_utøvere = [antall_unge_menn, antall_unge_kvinner, antall_middelaldrende_menn, antall_middelaldrende_kvinner, antall_eldre_menn, antall_eldre_kvinner]

plt.figure(figsize=(8, 8))
plt.pie(antall_utøvere, labels=etiketter, autopct='%1.1f%%')
plt.title('Andel av Utøvere i Hver Aldersgruppe og Kjønn')
plt.show()
'''


#Prøvde å lage et scatter diagram for å vise alle landene, men det er vanskelig med teksten som går over hverandre og med hvor mange land det er 

'''
import csv
import matplotlib.pyplot as plt
import numpy as np

filnavn = "IT2/start/Databehandling/Prøvesmak/run.csv"

with open(filnavn, 'r', encoding="utf-8") as fil:
    leser = csv.DictReader(fil)
    data = list(leser)


land_utøvere = {}

for rad in data:
    land = rad['country']
    if land in land_utøvere:
        land_utøvere[land].append(rad)
    else:
        land_utøvere[land] = [rad]



# Finner antall utøvere per uke for hvert land
antall_utøvere_per_land_per_uke = {land: len(utøvere) / 52 for land, utøvere in land_utøvere.items()}

# Sorterer landene etter antall utøvere per uke (fra minst til mest)
sorted_data = sorted(antall_utøvere_per_land_per_uke.items(), key=lambda x: x[1])

# Lager en unik farge for hvert land
antall_land = len(sorted_data)
colors = plt.cm.viridis(np.linspace(0, 1, antall_land))

# Plotter antall utøvere per land
plt.figure(figsize=(12, 8))
for i, (land, antall_utøvere) in enumerate(sorted_data):
    plt.scatter(land, antall_utøvere, color=colors[i], alpha=0.7, label=land)

plt.title('Antall Utøvere fra Hvert Land per Uke')
plt.xlabel('Land')
plt.ylabel('Antall Utøvere per Uke')
plt.xticks(rotation=90)
plt.yscale('log')  # Bruker logaritmisk skala for y-aksen
plt.grid(False)  # Fjerner rutenettet

# Legger til navnene på landene ved siden av punktene
for land, antall_utøvere in sorted_data:
    plt.text(land, antall_utøvere, land, fontsize=8, ha='right', va='bottom', rotation=90)

plt.tight_layout()
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.show()
'''

import csv
import matplotlib.pyplot as plt

filnavn = "IT2/start/Databehandling/Prøvesmak/run.csv"

with open(filnavn, 'r', encoding="utf-8") as fil:
    leser = csv.DictReader(fil)
    data = list(leser)

# Oppretter et tomt dictionary for å telle antall utøvere per "major"
major_counts = {}

for rad in data:
    major = rad['major']
    if major:
        # Hvis "major" finnes, øk telleren for denne "major" med 1
        if major in major_counts:
            major_counts[major] += 1
        else:
            major_counts[major] = 1

# Deler antall utøvere per "major" på 52 for å justere for den ukentlige oppdateringen
for key in major_counts:
    major_counts[key] /= 52

# Plotter antall utøvere per "major" som et kakediagram
plt.figure(figsize=(8, 8))

labels = list(major_counts.keys())
sizes = list(major_counts.values())

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Andel av Utøvere per Major (Justert for ukentlig oppdatering)')
plt.axis('equal')
plt.tight_layout()
plt.show()


