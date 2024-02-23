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

lista_par = []
lista_impar = []
[lista_par.append(numero) if numero % 2 == 0 else lista_impar.append(numero) for numero in range(1, 21)]

print(f"Lista de pares del 1 al 20 {lista_par}")
print(f"Lista de impares del 1 al 20 {lista_impar}")

lista_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18],[19, 20]]
print("Lista original:", lista_listas)

lista_simple = [valor
                for sublista in lista_listas
                for valor in sublista]
print("Lista original sin sublistas:", lista_simple)

lista_par = []
lista_impar = []

[lista_par.append(numero) 
 if numero % 2 == 0 
 else lista_impar.append(numero) 
 for numero in lista_simple]

print(f"Lista de pares del 1 al 20 {lista_par}")
print(f"Lista de impares del 1 al 20 {lista_impar}")