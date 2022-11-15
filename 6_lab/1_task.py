import random

n = 5
listMag = dict()

for i in range(n):
  listMag['mag' + str(i + 1)] = [random.randint(100, 500), random.randint(1000, 15000)]

amountOfMagazines = 0
commonCost = 0

for keys in sorted(listMag.keys()):
    print(keys, " : ", listMag[keys])
    if listMag[keys][1] < 10000:
        amountOfMagazines += 1
        commonCost += listMag[keys][0]

print("Average price of magazines that have fewer than 10,000 copies = ", commonCost / amountOfMagazines)

del listMag['mag1']

print(listMag)