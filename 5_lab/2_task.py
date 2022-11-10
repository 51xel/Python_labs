def sum(mass):
    summ = 0
    for i in range(len(mass)):
        summ = summ + mass[i]
    
    return summ


n = int(input("Enter the size of array = "))
arr = []

print("Enter the array:")
for i in range(n):
     arr.append(int(input()))

print("Sum of numbers = ", sum(arr))