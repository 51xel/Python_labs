h = int(input("Enter amount of lines = "))
w = int(input("Enter amount of columns = "))
arr = [[0 for x in range(w)] for y in range(h)] 

for i in range(len(arr)):
    for j in range(len(arr[0])):
        if (j + 1) % 2 != 0:
            arr[i][j] = 1

for i in range(len(arr)):
    for j in range(len(arr[0])):
       print(arr[i][j], " ", end="")
    print()