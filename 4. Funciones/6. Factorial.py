def iniciar():
    tot = 0
    num = -1
    while num != 0:
        num = int(input("Digite un número para hallar su factorial: "))
        res = factorial(num)
        imprimirFac(num, res)
        tot += 1
    total(tot)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def imprimirFac(n, r):
    print(f"El factorial de {n} es {r}")

def total(t):
    print(f"Cantidad total de numero leidos fue de: {t}")

print("El programa termina cuando se ingrese el número 0")
iniciar()