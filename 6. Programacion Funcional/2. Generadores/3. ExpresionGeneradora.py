from os import system

system("cls")
num = int(input("Digite el rango para generar los números enteros: "))

# Expresión generadora: Función generadora de caracter anónimo
generador = (num for num in range(1, num + 1))

print(f"Lista de número de 1 a {num}:", end=" ")

for i in generador:
    print(i, end=" ")