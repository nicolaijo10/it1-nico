'''
#Planet eksmepler

import math as m

class Planet:
  def __init__(self, navn, solavstand, radius):
    self.navn = navn
    self.solavstand = solavstand
    self.radius = radius

  def volum(self):
    return (4/3) * m.pi * self.radius**3
  
  def visInfo(self):
    print(f"Planeten {self.navn} er {self.solavstand} millioner km unna sola og har radius {self.radius} km. Den har også et volum på {self.volum()}")


    
mars = Planet("Mars", 227.9, 3389.5)
jupiter = Planet("Jupiter", 778.5, 69911)
jorden = Planet("Jorden", 152 , 6371 )
merkur = Planet("Merkur", 58, 2439)
venus = Planet("Venus", 108, 6051)

print(jupiter.radius)
print(jorden.solavstand)
print(merkur.navn)
print(venus.radius)
print(jupiter.volum())

jupiter.visInfo()

'''

'''
#Billet pris utregning (Oppgave)

class Billett():
  def __init__(self):
      self.mva = 0.12
      self.pris = 20

  def beregnPris(self):
    return self.pris + (self.pris * self.mva)
  
class Barnebillett(Billett):
  def __init__(self):
      super().__init__()
      self.rabatt = 0.5
  
  def beregnPris(self):
      return super().beregnPris() * self.rabatt
  
class ukeBillett(Billett):
    def __init__(self):
      super().__init__()
      self.rabatt = 0.8

    def beregnPris(self):
       return super().beregnPris() * self.rabatt * 7


vanlig_billett = Billett()
barne_billett = Barnebillett()
uke_billett = ukeBillett()

print("Vanlig billett pris:", vanlig_billett.beregnPris())
print("Barnebillett pris:", barne_billett.beregnPris())
print("Ukebillett pris:", uke_billett.beregnPris())

'''

'''
#Rektangel eksempel (+ oppgave)
class Rektangel:
  """Klasse for å representere et rektangel"""
  def __init__(self, lengde:int, bredde:int):
    """Konstruktør"""
    self.lengde = lengde
    self.bredde = bredde
  
  def areal(self):
    """Metode for å beregne areal"""
    return self.lengde * self.bredde

  def visInfo(self):
    """Skriver ut informasjon om et rektangel"""
    print(f"Rektangel med lengde {self.lengde} og bredde {self.bredde} har areal {self.areal()}")

class Kvadrat(Rektangel):
  """Klasse for å representere et kvadrat"""
  def __init__(self, sidekant:int):
    super().__init__(sidekant, sidekant)
  
  def visInfo(self):
    """Skriver ut informasjon om et kvadrat"""
    print(f"Kvadrat med sidelengde {self.lengde} har areal {self.areal()}")

# Liste som skal holde på rektangler
rektangler = []

# Lager og legger til noen rektangler
rektangler.append(Rektangel(2, 5))
rektangler.append(Rektangel(4, 3))
rektangler.append(Rektangel(5, 6))

for r in rektangler:
  r.visInfo()


# Liste som skal holde på rektangler
kvadrater = []

# Lager og legger til noen rektangler
kvadrater.append(Kvadrat(2))
kvadrater.append(Kvadrat(4))
kvadrater.append(Kvadrat(5))

for k in kvadrater:
  k.visInfo()
'''

'''
#medlem eksempel
class Medlem:
  medlemsnummer = 0

  def __init__(self, fornavn, etternavn):
    self.fornavn = fornavn
    self.etternavn = etternavn
    Medlem.medlemsnummer = Medlem.medlemsnummer + 1
    self.medlemsnummer = Medlem.medlemsnummer

per = Medlem("Per", "Lund")
kim = Medlem("Kim", "Svendsen")
kelly = Medlem("Kelly", "Brixton")

print(f"{per.fornavn} har medlemsnummer {per.medlemsnummer}")
print(f"{kim.fornavn} har medlemsnummer {kim.medlemsnummer}")
print(f"{kelly.fornavn} har medlemsnummer {kelly.medlemsnummer}")

'''

'''
import random

class Bankkonto:
    def __init__(self, saldo, eier):
        self.eier = eier
        self.saldo = saldo
        self.kontonummer = random.randint(1000, 9999)

    def innskudd(self, antall):
        self.saldo += antall

    def uttak(self, antall):
        self.saldo -= antall

per = Bankkonto(69000, "Per")
berit = Bankkonto(20000, "Berit")
narkoman = Bankkonto(-10000, "Ronny")

# Setter 5000 kr inn i kontoen til narkomanen
narkoman.innskudd(5000)

print(f"Saldoen til {narkoman.eier} er nå: {narkoman.saldo} kr")
'''

