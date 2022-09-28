import math

def Fibonacci(x):
    f = []
    f.append(0)
    f.append(1)

    i = 1

    while f[i] <= x:
        i = i + 1
        f.append(f[i - 1] + f[i - 2])
    
    return f[i]

def Z(x):
    if x > 45:
        return math.sqrt(x)
    elif x <= 45:
        return math.sin(2 * x)

x = int(input("Введіть X: "))
p = int(input("Введіть P: "))

print("Z = ", Z(x))
print("Fibonacci = ", Fibonacci(p))