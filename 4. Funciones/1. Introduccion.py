def suma1():
    res = 5 + 3
    print(f"5 + 3 = {res} ==> Llamado a función suma sin envio de argumentos sin retorno")

def suma2(a, b):
    res = a + b
    print(f"{a} + {b} = {res} ==> Llamado a función suma con envio de argumentos sin retorno")

def suma3(a=5, b=3):
    res = a + b
    print(f"{a} + {b} = {res} ==> Llamado a función suma sin envio de argumentos, recibiendo argumentos por defecto y no hay retorno")

def factorial1(a):
    f = 1
    for i in range(1, a + 1):
        f *= i
    return f

def factorial2(a):
    if a == 0:
        return 1
    return a * factorial2(a - 1)

def tablaMultiplicar(a):
    print(f"La tabla de multiplicar del número {a} es:")
    for i in range(1, 11):
        tabmult = i * a
        imprimirtabla(a, i, tabmult)

def imprimirtabla(n, j , res):
    print(f"{n} X {j} = {res}")

suma1()
suma2(5, 3)
suma3()
fact = factorial1(5)
print(f"El factorial de 5 es {fact} ==> Llamado a función factorial con envio de argumentos con retorno")
fact = factorial2(5)
print(f"El factorial de 5 es {fact} ==> Llamado a función factorial usando recursividad")
tablaMultiplicar(5)