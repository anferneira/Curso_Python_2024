from os import system

system("cls")
num = int(input("Digite el rango para generar los cuadrados y sumarlos: "))

# Expresión generadora: Función generadora de caracter anónimo
generador1 = (num ** 2 for num in range(1, num + 1))
generador2 = sum(num ** 2 for num in range(1, num + 1))

print(f"Lista de número de 1 a {num}:", end=" ")

for i in generador1:
    print(i, end=" ")

print(f"\nLa suma de los cuadrados es {generador2}")