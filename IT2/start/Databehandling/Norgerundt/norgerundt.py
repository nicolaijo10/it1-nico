 
import csv
import matplotlib.pyplot as plt
from datetime import datetime

filnavn = "IT2/start/Databehandling/Norgerundt/NORGE-RUNDT.csv"

with open(filnavn, 'r', encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader) 
    data = list(reader)