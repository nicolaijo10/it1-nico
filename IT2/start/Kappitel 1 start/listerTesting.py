import random

tall = []
sortedTall = []

for i in range (15):
    tilfeldigTall = random.randint(1, 100)
    tall.append(tilfeldigTall)


while tall:
    min = tall[0]  
    for x in tall: 
        if x < min:
            min = x
    sortedTall.append(min)
    tall.remove(min)    

print(sortedTall)


'''
høyestTall = max(tall)

print(tall)
print(høyestTall)
'''
