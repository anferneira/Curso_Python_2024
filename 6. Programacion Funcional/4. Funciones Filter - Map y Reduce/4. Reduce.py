from functools import reduce
from os import system

def suma(x, y):
    return x + y

system("cls")
numeros = [1, 2, 3, 4, 5]
print(f"La suma de los números de la lista {numeros} es {reduce(suma, numeros)}")
print(f"La suma de los números de la lista {numeros} es ", end="")
print(reduce(lambda x, y: x + y, numeros))
print(f"La suma de los números de la lista {numeros} agregando el 10 es ", end="")
print(reduce(lambda x, y: x + y, numeros, 10))
print(f"La suma de los números de la lista {numeros} agregando el 10 es {reduce(suma, numeros, 10)}")