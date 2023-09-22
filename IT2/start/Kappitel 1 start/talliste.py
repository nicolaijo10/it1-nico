import random 

tilfeldige_tall = []

for _ in range(9):
    tilfeldige_tall.append(random.randint(1, 50))

sum = sum(tilfeldige_tall)
minste = min(tilfeldige_tall)
høyeste = max(tilfeldige_tall)
gjennomsnitt = sum / len(tilfeldige_tall)

print(sum)
print(minste)
print(høyeste)
print(gjennomsnitt)
