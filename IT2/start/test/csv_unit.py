import csv

filnavn = "IT2/start/test/developers.csv"

filnavn2 = "IT2/start/test/dev2.csv"

with open(filnavn, encoding="utf-8") as fil:
  for linje in fil:
    print(linje)

with open(filnavn2, encoding="utf-8") as fil2:
  for linje in fil2:
    print(linje)