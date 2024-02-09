'''
filnavn = "IT2/start/Databehandling/reeleDatasertttttt/MikkelRev.txt"

with open(filnavn, encoding="utf-8") as fil:
  for linje in fil:
    print(linje)
'''
'''
tekst1 = "1,2,3,4"
tekst2 = "1 ; 2 ; 3 ; 4"
tekst3 = "1 2 3 4"

print(tekst1.split(","))
print(tekst2.split(";"))
print(tekst3.split("\t"))
'''

'''
class Rektangel:
  def __init__(self, lengde, bredde):
    self.lengde = lengde
    self.bredde = bredde
  
  def areal(self):
    return self.lengde * self.bredde

rektangler = []

filnavn = "IT2/start/Databehandling/reeleDatasertttttt/rektangler.txt"

with open(filnavn) as fil:
  for linje in fil:
    sidekanter = linje.rstrip().split(",")

    lengde = int(sidekanter[0])
    bredde = int(sidekanter[1])

    rektangler.append(Rektangel(lengde, bredde))

for rektangel in rektangler:
  print(rektangel.areal())
'''

'''
filnavn = "teksten_min.txt"

tekst = "Hei, jeg liker å programmere. Nå skal jeg bruke programmering for å lagre akkurat denne teksten i en fil."

with open(filnavn, "w") as fil:
  fil.write(tekst)

filnavn = "teksten_min_2.txt"

with open(filnavn, "a") as fil:
  fil.write("Hei, jeg liker å programmere.\n")
  fil.write("Nå skal jeg bruke programmering for å lagre akkurat denne teksten i en fil.")
  '''


import csv

filnavn = "IT2/start/Databehandling/reeleDatasertttttt/Befolkning_1951-2022.csv"

with open(filnavn, encoding="utf-8-sig") as fil:
  filinnhold = csv.reader(fil, delimiter=";")

  overskrifter = next(filinnhold)
  print(overskrifter)

  for rad in filinnhold:
    print(rad)
