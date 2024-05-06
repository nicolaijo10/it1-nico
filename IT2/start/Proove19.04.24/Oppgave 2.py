'''
Kilder:

https://www.geeksforgeeks.org/writing-csv-files-in-python/
https://github.com/hausnes/IT2-2023-2024
https://docs.python.org/3/library/csv.html
https://docs.python.org/3/library/unittest.html
https://www.quora.com/In-Python-how-do-I-append-a-user-input-to-a-specific-row-within-an-existing-CSV-file#:~:text=In%20Python%2C%20you%20can%20use,Copy%20codeimport%20csv



'''

import csv

#Her bare lager jeg en basis for framtidige andre produkter med felles informasjon som de alle sammen har
class Product:
    def __init__(self, name, purchase_date, purchase_price, current_value,):
        self.name = name
        self.purchase_date = purchase_date
        self.purchase_price = purchase_price
        self.current_value = current_value

#Her lager vi en arve klasse kalt "Console" som inneholder litt mer spesefikt om konsoller(den eneste forksjellen er "model") 
class Console(Product):
    def __init__(self, name, purchase_date, purchase_price, current_value, model):
        super().__init__(name, purchase_date, purchase_price, current_value)
        self.model = model

    #Hoved funksjonen til å skrive til csv, en veldig basic/barebones metode på å få intergrert det lille jeg kan om dette temaet
    def write_to_csv(self, filename):
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.name, self.purchase_date, self.purchase_price, self.current_value, self.model])

#Her lager vi en arve klasse kalt "Game" som inneholder litt mer spesefikt om konsoller(den eneste forksjellen er "type") 
class Game(Product):
    def __init__(self, name, purchase_date, purchase_price, current_value,type):
        super().__init__(name, purchase_date, purchase_price, current_value)
        self.type = type

    def write_to_csv(self, filename):
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.name, self.purchase_date, self.purchase_price, self.current_value, self.type])



#Objectene som vi skriver inn i csv filen 
console1 = Console("PlayStation 5", "2023-01-15", 500, 400, "PS5 Pro")
console2 = Console("Xbox Series X", "2023-02-20", 450, 380, "Xbox SX")
game1 = Game("Dark souls III", "2019-05-15", 60, 60, "Digital")

#Write to csv funksjonen som skriver inn i filen
filename = "products.csv"
console1.write_to_csv(filename)
console2.write_to_csv(filename)
game1.write_to_csv(filename)

'''
Denne delen lå jeg til nå i etterkant og lar deg faktisk legge inn spill selv i stedet for å ha alt hardkodet inn.
Den er også litt annerledes basert på om du legger inn en konsoll eller et spill
Et problem jeg dukker opp i er at når du skal adde et produkt så lager koden en ny csv fil. Du kan fortsette å legge til nye ting inne i den csv filen, men sekunde
jeg flytter csv-filen inn i prøve mappen min, så stopper koden min å skrive inn i den og lager i stedet en ny csv fil. 
Jeg prøvde å endre "filename" til den direkte fil plasseringen av csv filen, men det gikk heller ikke. Jeg finner ikke en god løsning akkurat nå.
'''

def add_product():
    product_type = input("Enter product type (Console/Game): ").lower()
    name = input("Enter product name: ")
    purchase_date = input("Enter purchase date (YYYY-MM-DD): ")
    purchase_price = float(input("Enter purchase price: "))
    current_value = float(input("Enter current value: "))

    if product_type == "console":
        model = input("Enter console model: ")
        new_product = Console(name, purchase_date, purchase_price, current_value, model)
    elif product_type == "game":
        game_type = input("Enter game type: ")
        new_product = Game(name, purchase_date, purchase_price, current_value, game_type)
    else:
        print("Invalid product type.")
        return

    filename = "IT2/start/Proove19.04.24/products.csv"
    new_product.write_to_csv(filename)
    print("Product added successfully.")

def main():
    add_product()

if __name__ == "__main__":
    main()






