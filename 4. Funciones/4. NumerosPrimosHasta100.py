def NumeroPrimo():
    for i in range(3, 101):
        r = factor(i)
        if r == 2:
            print(i, end=" ")

def factor(n):
    i = 1
    f = 0
    while i <= n:
        if n % i == 0:
            f += 1
        i += 1
    return f


print("Los números primos de 1 a 100 son: 1 2", end=" ")
NumeroPrimo()