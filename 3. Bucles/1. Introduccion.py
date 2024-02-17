nom = input("Digite su nombre: ")

for i in nom:
    print(i)

print()

for i in nom:
    print(i, end="")

print()
print()
print("Números del 0 a 20")

for i in range(21):
    print(f"Número {i}")

print("\nNúmeros del 1 a 20")

for i in range(1, 21):
    print(f"Número {i}")

print("\nNúmeros pares del 1 a 20")

for i in range(2, 21, 2):
    print(f"Número {i}")

print("\nNúmeros pares del 1 a 20")

for i in range(2,21):
    if i % 2 == 0:
        print(f"Número {i}")

print("\nNúmeros impares del 1 a 20")

for i in range(1, 21, 2):
    print(f"Número {i}")

print("\nNúmeros impares del 1 a 20")

for i in range(21):
    if i % 2 == 1:
        print(f"Número {i}")