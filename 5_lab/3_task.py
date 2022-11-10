def CountMaxFreq(arr):
    result = 0
    num_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
    max = 0

    for i in list(num_set):
        freq = arr.count(i)
        if freq > max:
            max = freq
            result = i
    
    return result

n = int(input("Enter the size of array = "))
arr = []

print("Enter the array:")
for i in range(n):
     arr.append(int(input()))

print("Max frequency has number = ", CountMaxFreq(arr))