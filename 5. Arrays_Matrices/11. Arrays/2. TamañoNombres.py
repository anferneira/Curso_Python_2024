"""
    Crea dos arrays o arreglos unidimensionales que tengan el mismo tamaño (lo pedirá
    por teclado), en uno de ellos almacene el nombre de personas por cadenas y en el
    otro almacene la longitud de los nombres.

    Mostrar en pantalla el arreglo con los nombres, el arreglo con la longitud de los
    nombres y que me muestre un mensaje que diga "La longitud del nombre 'nombres' es
    <longitud>
"""

tam = int(input("Introduzca el tamaño de los arrays: "))
print()
nombre = []
longitud = []

for i in range(tam):
    nombre.append(input(f"Digite el nombre de la persona {i + 1}: "))
    longitud.append(len(nombre[i]))

print(f"El arreglo de nombres es: {nombre}")
print(f"El arreglo de longitud de nombres es: {longitud}")

for i in range(tam):
    print(f"La longitud del nombre '{nombre[i]}' es {longitud[i]}")