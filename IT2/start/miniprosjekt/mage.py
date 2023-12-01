import time
import random

def printSlow(text):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(printSlow.speed)
    print()


class charactermage(Character):
    def __init__(self, name, level, hp, mana):
        super().__init__(name, level, hp, mana)
        self.spell_power = 50  # Legg til en variabel for spell power
        
    def cast_spell(self, spell, target):
        if self.mana >= spell["mana_cost"]:
            self.mana -= spell["mana_cost"]
            damage = spell["damage"] + self.spell_power  # Legg til spell power i skaden
            printSlow(f"{self.name} kaster {spell['name']} og forårsaker {damage} skade!")
            target.hit(damage)  # Skaden påføres målet (bossen)
        else:
            printSlow(f"{self.name} har ikke nok mana til å kaste {spell['name']}.")