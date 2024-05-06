

'''

Kilder:

https://innhold.aunivers.no/fagpakker/realfag/informasjonsteknologi-1-2/it-2/3-databehandling/eksempel-kart-og-data
https://help.openstreetmap.org/questions/12623/displaying-gps-coordinates
https://www.openstreetmap.org/
https://realpython.com/python-folium-web-maps-from-data/
https://python-graph-gallery.com/312-add-markers-on-folium-map/
https://github.com/hausnes/IT2-2023-2024
https://stackoverflow.com/questions/22496657/how-can-i-access-each-element-of-a-pair-in-a-pair-list


og

Forrige prøver og oppgaver, slikt som sykkel oppgaven 

Oppgave A: 

Mulige problemer: 
Mangel på etternavn på host_name, dette fører til at senere i oppgaven når jeg skal undersøke host_name, så er det fullt mulig at noen av de ikke er samme person


På host-name så står det ofte 2 personer på en eller flere leiligheter, i tilleg til dette så har ofte de 2 personene også andre eiendommer som de står for seg selv på
dette gjorde det vanskelig for meg å faktisk finne ut hvor mange ganger et navn står i python listen, fordi "Claude & Sophie" for eksempel, vil stå som sitt eget navn med min kode
så "Sophie" i denne konteksten vil ikke ble telt som sin egen person, men "Claude & Sophie" vil.


Problemer som stoppet meg:
Jeg fant ikke en løsning til Del B 

Det var vanskelig å lage en graf for oppgave C og D fordi metoden jeg brukte, appendet informasjonen inn med både string og int, dette førte til errors når jeg skulle skrive "bar" delen av plt
jeg fikk en fiks meg dette

hosts_navn = [pair[0] for pair in høyeste_name]
hosts_antall = [pair[1] for pair in høyeste_name]

Den deler opp stringen og inten inn i sine egene definisjoner, med hosts_navn og hosts_antall. Spesefikt så deler den opp et "par" i den listen og du skriver inn pair[0] som er stringen min for første
og pair[1] som er INTen min for andre

'''


import csv
import matplotlib.pyplot as plt
import folium

filnavn = "IT2/start/Proove19.04.24/utleige.csv"

with open(filnavn, 'r', encoding="utf-8") as fil:
    leser = csv.DictReader(fil)
    data = list(leser)


neighbourhoods = []
host_names = []

#Appender nabolagene inn i "neighbourhoods" 
for row in data:
    neighbourhood = row['neighbourhood']

    neighbourhoods.append(neighbourhood) 

#Appender navnene inn i "host_names" 
for row in data:
    host_name = row['host_name']

    host_names.append(host_name)


neighbourhood_mengder = {}
host_names_mengder = {}

#hood
for hood in neighbourhoods:
    if hood in neighbourhood_mengder:
        neighbourhood_mengder[hood] += 1
    else:
        neighbourhood_mengder[hood] = 1

#name
for name in host_names:
    if name in host_names_mengder:
        host_names_mengder[name] += 1
    else:
        host_names_mengder[name] = 1


#sort
sortert = sorted(neighbourhood_mengder.items(), key=lambda item: item[1])
sortert_name = sorted(host_names_mengder.items(), key=lambda item: item[1])

#hoyest
høyeste = sortert[-5:]
høyeste.reverse()

høyeste_name = sortert_name[-5:]
høyeste_name.reverse()

#lavest
laveste = sortert[:5]

laveste_name = sortert_name[:5]

#host
print("De fem mest brukte nabolagene er: ")
print(høyeste)


#name
print("De fem hosta med mest utleierobjekt er:")
print(høyeste_name)


# 
nabolag_navn = [pair[0] for pair in høyeste]
nabolag_antall = [pair[1] for pair in høyeste]

plt.figure(figsize=(10, 6))
plt.bar(nabolag_navn, nabolag_antall, color='skyblue')
plt.title('Antall utleieobjekter i de fem mest brukte nabolagene')
plt.xlabel('Nabolag')
plt.ylabel('Antall utleieobjekter')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# 
hosts_navn = [pair[0] for pair in høyeste_name]
hosts_antall = [pair[1] for pair in høyeste_name]

plt.figure(figsize=(10, 6))
plt.bar(hosts_navn, hosts_antall, color='salmon')
plt.title('Antall utleieobjekter for de fem vertene med flest utleieobjekter')
plt.xlabel('Vertnavn')
plt.ylabel('Antall utleieobjekter')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()




by_reviews = {}
for row in data:
    by = row ['neighbourhood_group']
    reviews = int(row['number_of_reviews'])

    if by in by_reviews:
        by_reviews[by] += reviews
    else:
        by_reviews[by] = reviews

høyeste_reviews = sorted(by_reviews.items(), key=lambda item: item[1], reverse=True)[:5]

by_kordinater = {
    "Manhattan": (40.7670, -73.8364),
    "Brooklyn": (40.6450,-73.9449),
    "Queens": (40.6525,-73.8721),
    "Bronx": (40.8517,-73.8412),
    "Staten Island": (40.5641,-74.1467)
}

kart = folium.Map(location=[40.7831, -73.9712], zoom_start=10)

for city, _ in høyeste_reviews:
    if city in by_kordinater:
        folium.Marker(location=by_kordinater[city], popup=city).add_to(kart)

# Vis kartet
kart.save('top_byer_reviews_kart.html')
