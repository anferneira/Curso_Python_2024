"""
    Realizar un programa que pida la cantidad de asistentes a un evento, pida la edad
    del asitente usando el ciclo for y muestre el asistente con mayor y menor edad de 
    todos.
"""

mayor = -1
menor = 150

asistentes = int(input("Cantidad de asistentes al evento: "))
print()

if asistentes > 0:
    for i in range(asistentes):
        edad = int(input(f"Digite la edad del asistente nº {i + 1}: "))
        if edad > mayor:
            mayor = edad
        elif edad < menor:
            menor = edad
else:
    print("Debe ingresar un valor valido de asistentes")

print(f"\nEl asistente con mayor edad tiene {mayor} años")
print(f"El asistente con menor edad tiene {menor} años")