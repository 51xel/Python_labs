def deleteUnpaired(mass, size):
    for i in range(size):
        if i % 2 != 0 and i <= size:
            mass.pop(i)
            size = size - 1

n = int(input("Enter the size of array = "))
arr = []

print("Enter the array:")
for i in range(n):
     arr.append(int(input()))

deleteUnpaired(arr, n)

for i in range(len(arr)):
    print(arr[i], end=" ")