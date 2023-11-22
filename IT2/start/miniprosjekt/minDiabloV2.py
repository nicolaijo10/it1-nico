import random
import time

def printSlow(text):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(printSlow.speed)
    print()

# Lar spilleren velge tekstfart
def chooseSpeed():
    while True:
        speed_choice = input("Velg tekstfart (1, 2, 3, 4, 5):")
        if speed_choice == "1":
            printSlow.speed = 0.1
        elif speed_choice =="2":
            printSlow.speed = 0.07
        elif speed_choice == "3":
            printSlow.speed = 0.05 
        elif speed_choice == "4":
            printSlow.speed = 0.03
        elif speed_choice == "5":
            printSlow.speed = 0.01
        else:
            printSlow("DU MÅ SKRIVE INN ET TALLL MELLOM 1 OG 5!!!")

        printSlow("Dette er farten på teksten. Er denne farten grei? ja/nei")
        dobbelsjekk = input()

        if dobbelsjekk == "ja":
            break

chooseSpeed()  # Spør spilleren om ønsket hastighet

#Karakter klasse for å definere alle de viktige variablene som er i en fight i et RPG spill
class Character:
    def __init__(self, name, level, hp, mana):
        self.name = name
        self.level = level
        self.hp = hp
        self.mana = mana
        self.healingFlaskCount = 3
        self.antallPauser = 2

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
    
    def is_dead(self):
        return self.hp < 1
    
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
            self.heal(20)  # Juster helbredelsesmengden etter dine behov
            printSlow(f"{self.name} brukte en helbredelsesflaske. Nå har du {self.healingFlaskCount} flasker igjen og {self.hp} HP igjen")
        else:
            printSlow(f"{self.name} har ingen helbredelsesflasker igjen.")
    
    def taPause(self):
        if self.antallPauser > 0:
            self.antallPauser -= 1
            self.heal(50)
            printSlow(f"Nå har du {hero.hp} HP igjen.")
        else:
            printSlow(f"{self.name} har ingen pauser igjen.")
        
    
    #Restarter karakteren, bruker muligens i framtiden
    def reset_character(self):
        self.hp = 100  # Tilbakestill HP til startverdi
        self.mana = 250  # Tilbakestill mana til startverdi
        self.healing_flask_count = 3  # Tilbakestill flasketelleren til startverdi

    def cast_spell(self, spell, target):
        if self.mana >= spell["mana_cost"]:
            self.mana -= spell["mana_cost"]
            printSlow(f"{self.name} kaster {spell['name']} og forårsaker {spell['damage']} skade!")
            target.hit(spell["damage"])  # Skaden påføres målet (bossen)
        else:
            printSlow(f"{self.name} har ikke nok mana til å kaste {spell['name']}.")


#Første karakterer 
hero = Character("Hero(Placeholder)", 3, 100, 100)
printSlow(f"All informasjon om helten: {hero}") # Skriv ut informasjon om helten, kallar __str__-metoden
# Lagar bossen
boss = Character("Boss(Placeholder)", 5, 20, 0)
printSlow(f"All informasjon om bossen: {boss}") # Skriv ut informasjon om bossen, kallar __str__-metoden
print()

# Definer spells
fireball_spell = {"name": "Fireball", "mana_cost": 30, "damage": 40}
lightning_spell = {"name": "Lightning", "mana_cost": 50, "damage": 60}
ice_spell = {"name": "Ice", "mana_cost": 20, "damage": 30}

# Legg spells i en liste
spells = [fireball_spell, lightning_spell, ice_spell]

inventar = []

def legg_til_i_inventar(item):
    inventar.append(item)
    printSlow(f"Du har lagt til {item} i inventaret ditt.")

# Sjekker om spesifikke elementer er i inventaret før kampen starter
if "den gamle boken" in inventar:
    printSlow("Du har 'den gamle boken' i inventaret ditt")
    hero.mana = 120 
    for spell in spells:
        spell["damage"] += 10


if "den magiske amuletten" in inventar:
    printSlow("Du har 'den magiske amuletten' i inventaret ditt")
    

    



# Gjer gjerne meir ut av delen over, der du kan sette meir avanserte verdier for helten og bossen
# Kanskje du til og med kan la spelaren setje verdiane sjølv for helten (tenk "character creation")?

# Kampen
while hero.is_alive() and boss.is_alive():
    # Helten sin tur
    angrip = input("Vil du angripe, bruke en helbredelsesflaske eller kaste en spell? (angrip/helbred/spell) ")

    if angrip == "angrip":
        printSlow("Du angriper!")
        print()
        boss.hit(20)
        printSlow(f"Bossen har {boss.get_hp()} HP igjen.")
    elif angrip == "helbred":
        printSlow("Du angriper ikke, og vurderer å bruke en helbredelsesflaske!")
        use_flask = input("Vil du bruke en helbredelsesflaske? (ja/nei) ")
        if use_flask == "ja":
            hero.use_healing_flask()
        print() 
    elif angrip == "spell":
        printSlow("Spells tilgjengelige:")
        for i, spell in enumerate(spells, 1):
            printSlow(f"{i}. {spell['name']} (Mana: {spell['mana_cost']}) - Skade: {spell['damage']}")

        spell_choice = input("Velg en spell (1, 2, 3, osv.): ")
        if spell_choice.isdigit():
            spell_choice = int(spell_choice)
            if 1 <= spell_choice <= len(spells):
                chosen_spell = spells[spell_choice - 1]
                if hero.mana >= chosen_spell["mana_cost"]:
                    hero.cast_spell(chosen_spell, boss)  # Kast spellen hvis du har nok mana
                    printSlow(f"Din nye mana-mengde er {hero.mana}.")
                else:
                    printSlow("Du har ikke nok mana til å kaste denne spellen.")
            else:
                printSlow("Ugyldig valg.")
        else:
            printSlow("Ugyldig valg.")

    
    # Gjer det tilfeldig om bossen angrip, må ta seg ein pause, eller kanskje healer? Sistnemnte er ikkje implementert endå
    boss_angrip = random.choice([True, False])
    if boss_angrip:
        printSlow("Bossen angriper!")
        hero.hit(20) # Gjer gjerne denne delen random (tilfeldig skade)
        printSlow(f"Du har {hero.get_hp()} HP igjen.")

        printSlow(f"Etter angrepet så har helten {hero.get_hp()} HP og bossen {boss.get_hp()} HP.")
    else:
        printSlow(f"{boss.get_name()} Må ta seg ein pause.")
    
    print()

# Skriv ut resultatet av kampen (sidan me er ferdige med while-løkka, dvs ein av dei er døde)
print()
printSlow("Kampen er over!")
printSlow(f"Etter kampen så har helten {hero.get_hp()} HP og bossen {boss.get_hp()} HP.")


while hero.is_alive() and boss.is_dead():
    valgEtterBoss = input("Vil du fortsette eller vil du ta en pause? (Du har 2 pauser igjen for i dag, å ta pause vil gi deg 50hp tilbake) (pause/fortsett)")

    if valgEtterBoss == "pause":
        hero.taPause()
        printSlow(f"Nå har du {hero.hp} HP igjen.")
    elif valgEtterBoss == "fortsett":
        break  # Fortsetter spillet ved å hoppe ut av denne løkken

printSlow("Etter pausen, forsetter helten framover i fangehullet for å se etter mulige fanger")
printSlow("Mens helten ser rundt så oppdager han et rom med en kiste, kisten kan inneholde dyrebare ressurser, men døren inn til kisten har en stor felle på gulvet forran seg,")
printSlow("Helten kan prøve å avvæpne fellen, men det er en sjanse for at fellen går av og helten vet ikke hva den vil gjøre")

felleSvar = input("Vil du prøve å avæpne fellen? (ja/nei)")

if felleSvar == "ja":
    avæpneSuksess = random.choice([True, False])
    if avæpneSuksess:
        printSlow("Du klarte å avæpne den og kan fortsette til kisten")
        hero.healingFlaskCount += 1
        printSlow(f"Kisten inneholer en healing potion!! Nå har du {hero.healingFlaskCount} flasker igjen")

    else:
        printSlow("Du feilet på å avæpne kisten og utløste en pil felle som skyter på deg, den treffer armen din og gjør 20 damage, men du fikk i hvertfall forsatt kisten")
        hero.hit(20)
        hero.healingFlaskCount += 1
        printSlow(f"Kisten inneholer en healing potion!! Nå har du {hero.healingFlaskCount} flasker igjen ")

    print()
        

elif felleSvar == "nei":
    printSlow("du fortsetter videre som om ingenting var der")

else:
    printSlow("du må svare med ja eler nei!!!!!")

printSlow("Helten kommer til et rom fylt med magiske runer og møter en gammel trollmann.")
printSlow("Trollmannen ser på deg og tilbyr deg en gave som kan hjelpe deg videre i reisen din.")

gave_valg = input("Vil du velge 'den magiske amuletten' eller 'den gamle boken'? (amulett/bok): ")

if gave_valg == "amulett":
    printSlow("Du velger den magiske amuletten!")
    # Kode
    
elif gave_valg == "bok":
    printSlow("Du velger den gamle boken!")
    # Kode
    
else:
    printSlow("Du klarte ikke å velge og går videre uten en gave.")
        
