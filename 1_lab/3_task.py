while True:
    N = int(input("Enter N: "))
    if N >= 1 and N <= 9:
        break
    print("Erroneous N: N >= 1 and N <= 9")

for i in range(N):
    for j in range(N - (i + 1)):
            print(' ', end='')
    for k in range(i + 1):
        print(N - k, end='')
    print()
