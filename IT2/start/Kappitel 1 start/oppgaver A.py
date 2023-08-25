import math as m
import calendar as c

'''
radius = input("hva er radiusen din")
radius = int(radius)

areal = radius ** 2 * m.pi
omkrets = radius * 2 * m.pi

print("arealet ditt er", areal, "og omkretsen din er", omkrets)
'''

'''
måned = c.month(2005,9)
print(måned)
'''

katet1 = float(input("Hva er verdien til det første katet? "))
katet2 = float(input("Hva er verdien til det andre katet? "))
hypotenus = (katet1**2 + katet2**2)**0.5

print("Hypotenusen er", hypotenus)