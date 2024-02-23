array = [1, 2, 3, 4, 5]

print("El arreglo es: ", array)

print("El arreglo es: ")
for i in array:
    print(i)

print("El arreglo es: ", end="")
for i in array:
    print(i, end=" ")

array = [1, 2, 3]

print("\nEl arreglo original es: ", array)

array.append(8)
print("Agregar el número 8 al arreglo: ", array)

array.remove(2)
print("Eliminar el número 2 del arreglo: ", array)

array.reverse()
print("Arreglo invertido: ", array)

array.sort()
print("Arreglo ordenado ascendentemente: ", array)

array.sort(reverse=True)
print("Arreglo ordenado descendentemente: ", array)