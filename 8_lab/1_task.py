import csv

dataToSave = []

try:
    csvfile = open("./8_lab/data.csv", 'r')
    reader = csv.DictReader(csvfile, delimiter = ",")
    print("Coutry Name: 2019 [YR2019]")
    for row in reader:
        print(row["Country Name"], " : ", row["2019 [YR2019]"])
    csvfile.seek(0)
except:
    print("Can`t open file")

print("Commands:\n\t1 - select country\n\t2 - see selected countries\n\t3 - save results to file and exit")
while(True):
    command = int(input("\nEnter the command: "))

    if command == 1:
        country = input("Enter country name: ")
        
        flag = True
        for row in reader:
            if row["Country Name"] == country:
                if row["2019 [YR2019]"] != "..":
                    print("Result(", row["Country Name"], " : ", row["2019 [YR2019]"], ")")
                    dataToSave.append([row["Country Name"], row["2019 [YR2019]"]])
                else:
                    print("No data about ", country)

                flag = False
                break

        csvfile.seek(0)
        if flag:
            print("The country name you entered does not exist")
    elif command == 2:
        print("Selected country to save: ")
        for row in dataToSave:
            print(row)
    elif command == 3:
        csvFileToSave = open("./8_lab/dataSave.csv", 'w')
        writer = csv.writer(csvFileToSave, delimiter=";")
        for row in dataToSave:
            writer.writerow(row)
        
        print("Saved!")
        csvFileToSave.close()
        break

csvfile.close()