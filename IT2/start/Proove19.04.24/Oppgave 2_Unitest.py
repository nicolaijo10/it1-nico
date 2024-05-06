#Dette er en veldig enkel test som bare tester om stringen "playstation 5" er i csv fila. På dette tidspunktet begynner jeg å få lite tid så jeg kunne ikke lage noe særlig mer

import unittest
import csv


class TestCSVFile(unittest.TestCase):
    def test_playstation_in_csv(self):
        filename = "IT2/start/Proove19.04.24/products.csv"
        product_found = False
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if "PlayStation 5" in row:
                    product_found = True
                    break
        self.assertTrue(product_found, "PlayStation 5 not found in CSV file")

if __name__ == '__main__':
    unittest.main()
