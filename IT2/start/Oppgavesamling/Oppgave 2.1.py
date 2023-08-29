#Skriv den manglende koden slik at programmet fungerer.

import random

hemmeligTall = random.randint(1, 100)  # Hent et tilfeldig tall

gjettet = 0  
antGjett = 0  

while gjettet != hemmeligTall:
    gjettet = int(input('Gjett det hemmelige tallet (1-100): '))  # Ta inn et gjett fra bruker
    antGjett += 1  # Øk antall forsøk med 1 for hver runde

    if gjettet < hemmeligTall:
        print('Gjettet var for lavt. Prøv igjen.')
    elif gjettet > hemmeligTall:
        print('Gjettet var for høyt. Prøv igjen.')

print('Du gjettet riktig! Det hemmelige tallet var', hemmeligTall, '. Du brukte', antGjett, 'forsøk.')

