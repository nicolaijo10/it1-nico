'''
import terninger as t

help(t.terning)
help(t.flereTerninger)

print(t.flereTerninger(5, 6))
'''

'''
import talliste as tl

print(tl.gjennomsnitt)
'''

import math

def overflateareal_og_volum_kule(radius):
    overflateareal = 4 * math.pi * radius**2
    volum = (4/3) * math.pi * radius**3
    return overflateareal, volum

def overflateareal_og_volum_sylinder(radius, høyde):
    overflateareal = 2 * math.pi * radius**2 + 2 * math.pi * radius * høyde
    volum = math.pi * radius**2 * høyde
    return overflateareal, volum

if __name__ == "__main__":
    # Test kulefunksjonen
    kule_radius = 6.0
    kule_overflateareal, kule_volum = overflateareal_og_volum_kule(kule_radius)
    print(f"Kule med radius {kule_radius}:")
    print(f"Overflateareal = {kule_overflateareal}")
    print(f"Volum = {kule_volum}\n")

    sylinder_radius = 3.0
    sylinder_høyde = 8.0
    sylinder_overflateareal, sylinder_volum = overflateareal_og_volum_sylinder(sylinder_radius, sylinder_høyde)
    print(f"Sylinder med radius {sylinder_radius} og høyde {sylinder_høyde}:")
    print(f"Overflateareal = {sylinder_overflateareal}")
    print(f"Volum = {sylinder_volum}\n")

