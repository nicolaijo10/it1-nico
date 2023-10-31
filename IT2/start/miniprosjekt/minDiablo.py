import random

#Karakter klasse for å definere alle de viktige variablene som er i en fight i et RPG spill
class Character:
    def __init__(self, name, level, hp, mana):
        self.name = name
        self.level = level
        self.hp = hp
        self.mana = mana
        self.healingFlaskCount = 3

    def __str__(self):
        return f"Name: {self.name}, Level: {self.level}, HP: {self.hp}, Mana: {self.mana}"
    
    def get_name(self):
        return self.name
    
    def get_level(self):
        return self.level
    
    def get_hp(self):
        return self.hp
    
    def get_mana(self):
        return self.mana
    
    def set_name(self, new_name):
        self.name = new_name

    def set_level(self, new_level):
        self.level = new_level

    def set_hp(self, new_hp):
        self.hp = new_hp

    def set_mana(self, new_mana):
        self.mana = new_mana

    def is_alive(self):
        return self.hp > 0
    
    def hit(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def heal(self, amount):
        self.hp += amount
        if self.hp > 100:
            self.hp = 100

    def cast_spell(self, cost):
        self.mana -= cost
        if self.mana < 0:
            self.mana = 0

    def use_healing_flask(self):
        if self.healingFlaskCount > 0:
            self.healingFlaskCount -= 1
            self.heal(10)  # Juster helbredelsesmengden etter dine behov
            print(f"{self.name} brukte en helbredelsesflaske. Nå har du {self.healingFlaskCount} flasker igjen og {self.hp} HP igjen")
        else:
            print(f"{self.name} har ingen helbredelsesflasker igjen.")
    
    #Restarter karakteren, bruker muligens i framtiden
    def reset_character(self):
        self.hp = 100  # Tilbakestill HP til startverdi
        self.mana = 250  # Tilbakestill mana til startverdi
        self.healing_flask_count = 3  # Tilbakestill flasketelleren til startverdi

    def cast_spell(self, spell, target):
        if self.mana >= spell["mana_cost"]:
            self.mana -= spell["mana_cost"]
            print(f"{self.name} kaster {spell['name']} og forårsaker {spell['damage']} skade!")
            target.hit(spell["damage"])  # Skaden påføres målet (bossen)
        else:
            print(f"{self.name} har ikke nok mana til å kaste {spell['name']}.")


# Definer spells
fireball_spell = {"name": "Fireball", "mana_cost": 30, "damage": 40}
lightning_spell = {"name": "Lightning", "mana_cost": 50, "damage": 60}
ice_spell = {"name": "Ice", "mana_cost": 20, "damage": 30}

# Legg spells i en liste
spells = [fireball_spell, lightning_spell, ice_spell]




#Første karakterer 
hero = Character("Hero(Placeholder)", 3, 100, 250)
print(f"All informasjon om helten: {hero}") # Skriv ut informasjon om helten, kallar __str__-metoden
# Lagar bossen
boss = Character("Boss(Placeholder)", 5, 210, 80)
print(f"All informasjon om bossen: {boss}") # Skriv ut informasjon om bossen, kallar __str__-metoden
print()

# Gjer gjerne meir ut av delen over, der du kan sette meir avanserte verdier for helten og bossen
# Kanskje du til og med kan la spelaren setje verdiane sjølv for helten (tenk "character creation")?

# Kampen
while hero.is_alive() and boss.is_alive():
    # Helten sin tur
    angrip = input("Vil du angripe, bruke en helbredelsesflaske eller kaste en spell? (angrip/helbred/spell) ")

    if angrip == "angrip":
        print("Du angriper!")
        print()
        boss.hit(20)
        print(f"Bossen har {boss.get_hp()} HP igjen.")
    elif angrip == "helbred":
        print("Du angriper ikke, og vurderer å bruke en helbredelsesflaske!")
        use_flask = input("Vil du bruke en helbredelsesflaske? (ja/nei) ")
        if use_flask == "ja":
            hero.use_healing_flask()
        print()
    elif angrip == "spell":
        print("Spells tilgjengelige:")
        for i, spell in enumerate(spells, 1):
            print(f"{i}. {spell['name']} (Mana: {spell['mana_cost']}) - Skade: {spell['damage']}")

        spell_choice = input("Velg en spell (1, 2, 3, osv.): ")
        if spell_choice.isdigit():
            spell_choice = int(spell_choice)
            if 1 <= spell_choice <= len(spells):
                chosen_spell = spells[spell_choice - 1]
                hero.cast_spell(chosen_spell, boss)  # Målet er nå bossen
            else:
                print("Ugyldig valg.")
        else:
            print("Ugyldig valg.")
    
    # Gjer det tilfeldig om bossen angrip, må ta seg ein pause, eller kanskje healer? Sistnemnte er ikkje implementert endå
    boss_angrip = random.choice([True, False])
    if boss_angrip:
        print("Bossen angriper!")
        hero.hit(10) # Gjer gjerne denne delen random (tilfeldig skade)
        print(f"Du har {hero.get_hp()} HP igjen.")

        print(f"Etter angrepet så har helten {hero.get_hp()} HP og bossen {boss.get_hp()} HP.")
    else:
        print(f"{boss.get_name()} Må ta seg ein pause.")
    
    print()

# Skriv ut resultatet av kampen (sidan me er ferdige med while-løkka, dvs ein av dei er døde)
print()
print("Kampen er over!")
print(f"Etter kampen så har helten {hero.get_hp()} HP og bossen {boss.get_hp()} HP.")
