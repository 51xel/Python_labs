def printDict(currentD):
  for i in currentD:
    print("Magazine ", i, " edition = ", currentD[i][0], " price = ", currentD[i][1])

def add(currentD, key, data):
  if key in currentD:
    print("Key = ", key, " is already exists")
  else:
    currentD[key] = data
    print("Key = ", key, " was added")

def dell(currentD, key):
  if key in currentD:
    del currentD[key]
    print("Key ", key, " was deleted")
  else:
    print("Key = ", key, " is not exists")

def printSort(currentD):
  for i in sorted(currentD.keys()):
    print("Magazine ", i, " edition = ", currentD[i][0], " price = ", currentD[i][1])

def findAveragePriceFor(currentD, amountOfCop):
  amountOfMagazines = 0
  commonCost = 0

  for i in currentD:
    if currentD[i][1] < amountOfCop:
      amountOfMagazines += 1
      commonCost += currentD[i][0]
  
  return commonCost / amountOfMagazines

listMag = dict()
listMag = {"Ranok" : [150, 12122], "SumyNews" : [190, 9809], "MusicAndMusic" : [678, 5430], "Weather" : [50, 20000], "SUMDUNEWS" : [150, 200]}

print("1 - add\n2 - delete\n3 - print\n4 - sorted print\n5 - find average price\n0 - exit")

while(True):
  command = int(input("Enter the code: "))

  if command == 1:
    data = []
    key = input("\tEnter the key to add: ")
    data.append(int(input("\tEnter the price to add: ")))
    data.append(int(input("\tEnter the copies to add: ")))

    add(listMag, key, data)
  elif command == 2:
    key = input("\tEnter the key to delete: ")

    dell(listMag, key)
  elif command == 3:
    printDict(listMag)
  elif command == 4:
    printSort(listMag)
  elif command == 5:
    amount = int(input("\tEnter the amount of copies to sort: "))

    print("Average price for magazines that has less then", amount, " copies = ", findAveragePriceFor(listMag, amount))
  elif command == 0:
    break
  else:
    print("Wrong code")


