'''
import matplotlib.pyplot as plt
import numpy as np

xverdier = np.linspace(0, 20, 50)
yverdier = xverdier**2

# Skriver ut en oversikt over tilgjengelige stiler
print(plt.style.available)

# Angir at vi vil bruke stilen "bmh"
plt.style.use("bmh")

plt.plot(xverdier, yverdier)

plt.xlabel("$x$")
plt.ylabel("$y$")
plt.xlim(0, 20)
plt.ylim(0, 400)

plt.show()
'''

'''
import matplotlib.pyplot as plt
import numpy as np

xverdier = np.linspace(0, 20, 50)

# Graf 1
yverdier = 0.5*xverdier**2 

plt.subplot(2, 1, 1)
plt.plot(xverdier, yverdier)
plt.grid()

# Graf 2
yverdier = -0.3*xverdier**3 

plt.subplot(2, 1, 2)
plt.plot(xverdier, yverdier)
plt.grid()

plt.show()
'''
'''
import matplotlib.pyplot as plt

utdanningsprogram = [
  "Bygg- og anleggsteknikk", 
  "Elektro og datateknologi",
  "Helse- og oppvekstfag",
  "Naturbruk",
  "Restaurant- og matfag",
  "Teknologi- og industrifag",
  "Håndverk, design og produktutvikling",
  "Frisør, blomster, interiør og eksponeringsdesign",
  "Informasjonsteknologi og medieproduksjon",
  "Salg, service og reiseliv"
]

antall = [3811, 4168, 8661, 2057, 1484, 5501, 313, 901, 1309, 2061]

plt.figure(figsize=(10, 5))          # Angir dimensjoner for figure-objektet

plt.barh(utdanningsprogram, antall)  # Lager stolpediagrammet

plt.subplots_adjust(left=0.4)        # Øker plassen på venstre side av diagrammet

plt.grid(axis="x")                   # Legger til rutenett (bare vertikale linjer)
plt.show()                           # Viser diagrammet

'''

'''
import matplotlib.pyplot as plt
import numpy as np

utdanningsprogram = [
  "Bygg- og anleggsteknikk", 
  "Elektro og datateknologi",
  "Helse- og oppvekstfag",
  "Naturbruk",
  "Restaurant- og matfag",
  "Teknologi- og industrifag",
  "Håndverk, design og produktutvikling",
  "Frisør, blomster, interiør og eksponeringsdesign",
  "Informasjonsteknologi og medieproduksjon",
  "Salg, service og reiseliv"
]

antallGutter = [3811, 4168, 8661, 2057, 1484, 5501, 313, 901, 1309, 2061]
antallJenter = [352, 268, 7286, 1028, 709, 851, 243, 826, 200, 895]
antallGutter2 = []

for i in range(len(antallGutter)):
    antallGutter2.append(antallGutter[i]-antallJenter[i])


fig, ax = plt.subplots(figsize=(10, 5))    # Angir dimensjoner for figure-objektet

y = np.arange(10)

ax.barh(y+0.2, antallJenter, height=0.4, label="Jenter")  # Lager stolpediagram jenter
ax.barh(y-0.2, antallGutter2, height=0.4, label="Gutter")  # Lager stolpediagram gutter
ax.set_yticks(y, utdanningsprogram)                       # Legger til akseverdier
ax.legend()                                               # Legger til beskrivelse

fig.subplots_adjust(left=0.4)  # Øker plassen på venstre side av diagrammet

ax.grid(axis="x")  # Legger til rutenett (bare vertikale linjer)
plt.show()         # Viser diagrammet
'''

'''

#Oppgave 11

import matplotlib.pyplot as plt
import numpy as np

årstall = [1985, 1989, 1993, 1997, 2001, 2005, 2009, 2013, 2017, 2021]
arbeiderpartiet = [71, 63, 67, 65, 43, 61, 64, 55, 49, 48]
høyre = [50, 37, 28, 23, 38, 38, 41, 48, 45, 36]

fig, ax = plt.subplots(figsize=(8, 10))    # Angir dimensjoner for figure-objektet

y = np.arange(len(årstall))

ax.barh(y - 0.2, arbeiderpartiet, 0.4, label='Arbeiderpartiet')  # Lager stolpediagram for Arbeiderpartiet
ax.barh(y + 0.2, høyre, 0.4, label='Høyre')                      # Lager stolpediagram for Høyre

ax.set_ylabel('Årstall')
ax.set_xlabel('Antall stortingsrepresentanter')
ax.set_title('Antall stortingsrepresentanter for Arbeiderpartiet og Høyre')
ax.set_yticks(y)
ax.set_yticklabels(årstall)
ax.legend()

plt.tight_layout()
plt.show()

'''
'''

import matplotlib.pyplot as plt

partiforkortelser = ["AP", "FrP", "H", "KrF", "MDG", "R", "Sp", "SV", "V", "PF"]
representanter = [48, 21, 36, 3, 3, 8, 28, 13, 8, 1]
farger = ["#f58c68", "#004281", "#3396d2", "#d2bc2a", "#25a23c", "#5d0008", "#90cc93", "#d34d2f", "#005245", "#f69465"]

plt.pie(representanter, labels=partiforkortelser, colors=farger, labeldistance=1.15, wedgeprops = { "linewidth": 1, "edgecolor": "white" })

plt.show()

'''

'''
import matplotlib.pyplot as plt

utdanningsprogram = [
    "Bygg- og anleggsteknikk",
    "Elektro og datateknologi",
    "Helse- og oppvekstfag",
    "Naturbruk",
    "Restaurant- og matfag",
    "Teknologi- og industrifag",
    "Håndverk, design og produktutvikling",
    "Frisør, blomster, interiør og eksponeringsdesign",
    "Informasjonsteknologi og medieproduksjon",
    "Salg, service og reiseliv"
]

antallGutter = [3811, 4168, 8661, 2057, 1484, 5501, 313, 901, 1309, 2061]
antallJenter = [352, 268, 7286, 1028, 709, 851, 243, 826, 200, 895]

fig, ax = plt.subplots(figsize=(8, 8))

labels = utdanningsprogram
sizes = antallGutter  # Endre til antallJenter for å se fordelingen av jenter
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0)  # For å eksplodere den første sektoren (valgfritt)

ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=90)
ax.axis('equal')

plt.title('Fordeling av gutter etter utdanningsprogram')
# Endre tittelen til 'Fordeling av jenter etter utdanningsprogram'

plt.show()
'''