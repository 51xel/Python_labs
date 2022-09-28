def Fibonacci(x):
    f = []
    f.append(0)
    f.append(1)

    i = 1

    while f[i] <= x:
        i = i + 1
        f.append(f[i - 1] + f[i - 2])
    
    return f[i]