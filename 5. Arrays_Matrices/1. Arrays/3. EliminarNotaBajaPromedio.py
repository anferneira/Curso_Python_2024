"""
    Dada las siguientes notas almacenadas en un arrelgo [5, 4, 2, 1, 3], muestrelo
    en pantalla y elimine la nota más baja sin usar el método 'min'; escriba en pantalla el nuevo
    arreglo. Saque el promedio de las notas descontando la nota eliminada.
"""

array = [5, 4, 2, 1, 3]
min = array[0]
sum = 0

for i in array:
    if i < min:
        min = i

print(f"El array de notas original es {array}")

array.remove(min)

print(f"La menor nota es {min}")
print(f"El nuevo arreglo de notas es {array}")

for i in array:
    sum += i

print(f"El promedio de notas es {sum / len(array)}")