from os import system

system("cls")

lista_par = []
lista_impar = []

for numero in range(1, 21):
    if numero % 2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)

print(f"Lista de pares del 1 al 20 {lista_par}")
print(f"Lista de impares del 1 al 20 {lista_impar}")