'''
Denne oppgaven synes jeg var ekstremt vanskelig og jeg måtte søke flere ganger.
Når jeg ikke fant ting på internette så spurte jeg en AI hva jeg burde gjøre, men jeg fikk ikke AIen til å løse hele oppgaven.
Jeg brukte den som et verktøy til å hjelpe meg å finne ut av hva jeg har gjort gale eller hva som er god strategi
'''

import random

def bestemVinner(spillerValg, datamaskinValg):
    if spillerValg == datamaskinValg:
        return "Uavgjort"
    elif (spillerValg == "st" and datamaskinValg == "sa") or \
         (spillerValg == "sa" and datamaskinValg == "p") or \
         (spillerValg == "p" and datamaskinValg == "st"):
        return "Spilleren vinner"
    else:
        return "Datamaskinen vinner"

def score():
    spillerScore = 0
    datamaskinScore = 0

    while spillerScore < 5 and datamaskinScore < 5:
        print("Velg stein ('st'), saks ('sa') eller papir ('p'): ")
        spillerValg = input().lower()
        datamaskinValg = random.choice(["st", "sa", "p"])

        print("Spilleren valgte:", spillerValg)
        print("Datamaskinen valgte:", datamaskinValg)

        result = bestemVinner(spillerValg, datamaskinValg)
        print(result)

        if result == "Spilleren vinner":
            spillerScore += 1
        elif result == "Datamaskinen vinner":
            datamaskinScore += 1

        print(f"Poengstand: Spilleren {spillerScore} - {datamaskinScore} Datamaskinen")

    if spillerScore == 5:
        print("Spilleren vant!")
    else:
        print("Datamaskinen vant!")

if __name__ == "__main__":
    score()