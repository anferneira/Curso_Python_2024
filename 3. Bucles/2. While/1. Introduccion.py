nom = input("Digite su nombre: ")

i = 0
while i < len(nom):
    print(nom[i])
    i += 1

print()

i = 0
while i < len(nom):
    print(nom[i], end="")
    i += 1

print()
print()
print("Números del 0 a 20")

i = 0
while i < 21:
    print(f"Número {i}")
    i += 1

print("\nNúmeros del 1 a 20")

print("\nNúmeros pares del 1 a 20")

i = 2
while i < 21:
    print(f"Número {i}")
    i += 2

print("\nNúmeros pares del 1 a 20")

i = 1
while i < 21:
    if i % 2 == 0:
        print(f"Número {i}")
    i += 1

print("\nNúmeros impares del 1 a 20")

i = 1
while i < 21:
    print(f"Número {i}")
    i += 2

print("\nNúmeros impares del 1 a 20")

i = 1
while i < 21:
    if i % 2 == 1:
        print(f"Número {i}")
    i += 1

"""
    Leer números enteros por teclados, hasta que el usuario ingrese el 0.
    Mostrar , la sumatoria de los números ingresados.
"""

num = int(input("\nDigite un número entero: "))
sum = 0

while num != 0:
    sum += num
    num = int(input("Digite un número entero: "))

print(f"\nLa sumatoria de los números es {sum}")