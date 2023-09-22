import random as rd

def terning(antallSider: int) -> int:
  """Returnerer et tilfeldig heltall i intervallet [1, antallSider], med begge endepunktente inkludert."""
  return rd.randint(1, antallSider)

def flereTerninger(antallTerninger: int, antallSider: int) -> list:
  """Returnerer en liste med resultater fra antallTerninger terninger med antallSider sider."""
  resultater = []
  
  for i in range(antallTerninger):
    resultater.append(terning(antallSider))
  
  return resultater