n = int(input("Enter the size of array = "))
arr = []
sumOfPositiveEvenElements = 0

print("Enter the array:")
for i in range(n):
    arr.append(int(input()))
    if arr[i] > 0 and arr[i] % 2 == 0:
        sumOfPositiveEvenElements += arr[i]

print("Sum of positive even elements = ", sumOfPositiveEvenElements)