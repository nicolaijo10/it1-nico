'''
person = {
  "fornavn": "Nicolai", 
  "etternavn": "Johannessen",
  "foedselsaar": 2005
}

print(f"Personens fornavn er {person['fornavn']}.")
print(f"Personens etternavn er {person['etternavn']}.")
print(f"Personen er født i {person['foedselsaar']}.")

for noekkel in person.keys():
  print(noekkel)

for verdi in person.values():
  print(verdi)

for noekkel, verdi in person.items():
  print(f"Nøkkel: {noekkel}, verdi: {verdi}.")

'''



'''
if "fornavn" in person:
  person.pop("fornavn")
'''

'''
tirsdag = {
    "maksTemp": "18°c",
    "minTemp": "12°c",
    "vind": "4 m/s",
    "himmel": "solskinn med noen skyer"
}

print(f"velkommen til denne super værmeldingen, idag så blir det en makstemperatur av {tirsdag['maksTemp']}")

'''

'''
sommer_ol = [
  { "årstall": 2004, "vinnertider": { "100 m": 10.93, "200 m": 22.06, "400 m": 49.41 } },
  { "årstall": 2008, "vinnertider": { "100 m": 10.78, "200 m": 21.74, "400 m": 49.62 } },
  { "årstall": 2012, "vinnertider": { "100 m": 10.75, "200 m": 21.88, "400 m": 49.55 } },
  { "årstall": 2016, "vinnertider": { "100 m": 10.71, "200 m": 21.78, "400 m": 49.44 } },
  { "årstall": 2020, "vinnertider": { "100 m": 10.61, "200 m": 21.53, "400 m": 48.36 } }
]
'''

'''
for ol in sommer_ol:
  aar = ol["årstall"]
  vinnertid_100m = ol["vinnertider"]["100 m"]
  print(f"I {aar} var vinnertiden på 100 m: {vinnertid_100m}. sekunder")
'''

'''
for ol in sommer_ol:
  aar = ol["årstall"]
  vinnertid_200m = ol["vinnertider"]["200 m"]
  print(f"I {aar} var vinnertiden på 200 m: {vinnertid_200m}. sekunder")
'''

'''
for ol in sommer_ol:
  aar = ol["årstall"]
  vinnertid_400m = ol["vinnertider"]["400 m"]
  print(f"I {aar} var vinnertiden på 400 m: {vinnertid_400m}. sekunder")
'''

'''
for ol in sommer_ol:
  vinnertid2020_100m = sommer_ol[4]["vinnertider"]["100 m"]
  vinnertid2020_200m = sommer_ol[4]["vinnertider"]["200 m"]
  vinnertid2020_400m = sommer_ol[4]["vinnertider"]["400 m"]
  print(f"I 2020 var vinnertiden på 100 m: {vinnertid2020_100m}. sekunder, 200m: {vinnertid2020_200m}. sekunder, 400m: {vinnertid2020_400m}. sekunder")
'''


#Blandede oppgaver

'''
tall_tekst = {
    1: "en", 
    2: "to", 
    3: "tre", 
    4: "fire", 
    5: "fem", 
    6: "seks", 
    7: "syv", 
    8: "åtte", 
    9: "ni", 
    10: "ti"
}

print("Tall | Tekst")
print("-----|------")
for tall, tekst in tall_tekst.items():
    print(f"{tall:<5}| {tekst}")
'''

'''
handlekurv = {
   "melk": 17.90,
   "smør": 38.90,
   "kokt skinke": 23.10,
   "sjokolade": 11.90,
   "oppvaskmiddel": 24.40,
   "frossenpizza": 29.90
}

# Finner laveste pris og tilhørende produkt
laveste_pris_produkt = min(handlekurv, key = handlekurv.get)
laveste_pris = handlekurv[laveste_pris_produkt]

# Finner høyeste pris og tilhørende produkt
høyeste_pris_produkt = max(handlekurv, key = handlekurv.get)
høyeste_pris = handlekurv[høyeste_pris_produkt]

# Finner totalprisen
totalpris = sum(handlekurv.values())

# Skriver ut resultatene
print("Laveste pris:", laveste_pris_produkt, laveste_pris)
print("Høyeste pris:", høyeste_pris_produkt, høyeste_pris)
print("Totalpris:", totalpris)

'''


'''
# Ordbok over norske byer
norske_byer = {
    "Oslo": {
        "Befolkning": 693494,
        "Beliggenhet": "Østlandet",
        "Kjente attraksjoner": ["Operahuset", "Vigelandsparken", "Akershus festning"]
    },
    "Bergen": {
        "Befolkning": 280216,
        "Beliggenhet": "Vestlandet",
        "Kjente attraksjoner": ["Bryggen", "Fløibanen", "Akvariet i Bergen"]
    },
    "Trondheim": {
        "Befolkning": 198711,
        "Beliggenhet": "Trøndelag",
        "Kjente attraksjoner": ["Nidarosdomen", "Gamle Bybro", "Rockheim"]
    },
    "Stavanger": {
        "Befolkning": 143574,
        "Beliggenhet": "Rogaland",
        "Kjente attraksjoner": ["Preikestolen", "Stavanger domkirke", "Oljemuseet"]
    },
    "Tromsø": {
        "Befolkning": 76703,
        "Beliggenhet": "Troms og Finnmark",
        "Kjente attraksjoner": ["Ishavskatedralen", "Polaria", "Tromsøya"]
    }
}

# Skriv ut informasjonen om alle byene
for by, info in norske_byer.items():
    print(f"By: {by}")
    print(f"Befolkning: {info['Befolkning']}")
    print(f"Beliggenhet: {info['Beliggenhet']}")
    print(f"Kjente attraksjoner: {', '.join(info['Kjente attraksjoner'])}")
    print("\n")
'''

