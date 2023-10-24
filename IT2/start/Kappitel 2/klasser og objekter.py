'''
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

