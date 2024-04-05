import csv
import matplotlib.pyplot as plt

filnavn = "IT2/start/Proove19.03.24/run.csv"

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


antall_unge_utøvere = len(unge_utøvere)
antall_middelaldrende_utøvere = len(middelaldrende_utøvere)
antall_eldre_utøvere = len(eldre_utøvere)

etiketter = ['Unge Utøvere', 'Middelaldrende Utøvere', 'Eldre Utøvere']
antall_utøvere = [antall_unge_utøvere, antall_middelaldrende_utøvere, antall_eldre_utøvere]

#Siden datasette har alle de samme utøverne, men resultatet skrevet for vær uke, så er teknisk sett alle utøverne skreve 52 ganger inn i datasette,derfor deler vi på 52
#Slikt at den ikke teller alle utøverne 52 ganger
antall_unge_utøvere_per_uke = antall_unge_utøvere / 52
print("I alderskategorien 18-34 er det: ",  antall_unge_utøvere_per_uke, "utøvere")

antall_middelaldrende_utøvere_per_uke = antall_middelaldrende_utøvere / 52
print("I alderskategorien 35-54 er det: ", antall_middelaldrende_utøvere_per_uke, "utøvere")

antall_eldre_utøvere_per_uke = antall_eldre_utøvere / 52
print("I alderskategorien 55+ er det: ", antall_eldre_utøvere_per_uke, "utøvere")

plt.bar(range(len(etiketter)), [antall_unge_utøvere_per_uke, antall_middelaldrende_utøvere_per_uke, antall_eldre_utøvere_per_uke])
plt.title('Antall Utøvere i Hver Aldersgruppe')
plt.xlabel('Aldersgruppe')
plt.ylabel('Antall Utøvere')

plt.xticks(range(len(etiketter)), etiketter)

for i, num in enumerate([antall_unge_utøvere_per_uke, antall_middelaldrende_utøvere_per_uke, antall_eldre_utøvere_per_uke]):
    plt.text(i, num + 0.5, f'{num:.2f}', ha='center')

plt.show()