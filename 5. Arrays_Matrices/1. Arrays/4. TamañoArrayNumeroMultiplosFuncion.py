"""
    Realizar un programa que pida el tamaño de un array y el número del múltiplo por
    teclado y por medio de una función me almacene la cantidad de múltiplos en un
    array y me los muestre en pantalla.

    Ejemplo: Si el tamaño del vector es 5 y el número de multiplos es 3, me muestra
    el siguiente array en pantalla: [3, 6, 9, 12, 15]
"""

def llenar(t, m):
    array = []
    for i in range(t):
        array.append((i + 1) * m)
    print(f"El array de tamaño {t} con múltiplos de {m} es {array}")

tamaño = int(input("Digite el tamaño del array: "))
multiplo = int(input("Digite el número del multiplo: "))

llenar(tamaño, multiplo)