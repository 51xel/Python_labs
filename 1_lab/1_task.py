def X(a, b):
    if a > b:
        return (2 * a) + b
    elif a == b:
        return -2
    elif a < b:
        return (a - 5) / b

while True:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    if a >= 1 and a <=100 and b >= 1 and b <= 100:
        break
    print("Erroneous data: 1 >= a and b >= 100")

print("X = ", X(a,b))
