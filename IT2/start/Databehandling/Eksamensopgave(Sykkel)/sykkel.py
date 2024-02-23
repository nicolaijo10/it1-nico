'''

#Oppgave 1

import csv
import matplotlib.pyplot as plt

filnavn = "IT2/start/Databehandling/Eksamensopgave(Sykkel)/sykkel.csv"

with open(filnavn, 'r', encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader) 
    data = list(reader)

startSteder = []

for row in data:
    startSted = row[4]

    startSteder.append(startSted) 

   
startStedTurer = {}

for sted in startSteder:
    if sted in startStedTurer:
        startStedTurer[sted] += 1
    else:
        startStedTurer[sted] = 1



sortert = sorted(startStedTurer.items(), key=lambda item: item[1])

høyeste = sortert[-3:]

laveste = sortert[:3]

høyeste.reverse()
print("De tre mest brukte stasjonene er: ")
print(høyeste)


print("De tre minst brukte startlokasjonene er: ")
print(laveste)

'''

#oppgave 2
 
import csv
import matplotlib.pyplot as plt
from datetime import datetime

filnavn = "IT2/start/Databehandling/Eksamensopgave(Sykkel)/sykkel.csv"

with open(filnavn, 'r', encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader) 
    data = list(reader)


startDato = []

for row in data:
    split = row[0].split(' ')
    dato = split[0]
    startDato.append(dato)
    #print(startDato)

#Alternativ metode(Vanskeligere å tolke, men sjappere og ryddigere å skrive)
#startDato = [row[0].split(' ')[0] for row in data]
    
turerPerUkedag = [0, 0, 0, 0, 0]

for dato in startDato:
    ukedag = datetime.strptime(dato, "%Y-%m-%d").weekday()
    if ukedag > 4:
        continue
    else:
        turerPerUkedag[ukedag] +=1
    #print(dato)

print(turerPerUkedag)
plt.bar(range(5), turerPerUkedag)
plt.xticks(range(5), ['mandag', 'tirsdag', 'onsdag', 'torsdag', 'fredag'])
plt.ylabel('Antall turer')
plt.title('totalt antall turer fra alle startlokasjoner til sammen, per ukedag.')
plt.show() 