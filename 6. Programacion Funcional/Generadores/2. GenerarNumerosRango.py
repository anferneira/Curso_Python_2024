from os import system

def generador(num):
    for numero in range(1, num + 1):
        yield numero

system("cls")
num = int(input("Digite el rango para generar los números enteros: "))
print(f"Lista de número de 1 a {num}:", end=" ")
for i in generador(num):
    print(i, end=" ")