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
lista_par = [numero for numero in range(1, 21) if numero % 2 == 0]
lista_impar = [numero for numero in range(1, 21) if numero % 2 == 1]

print(f"Lista de pares del 1 al 20 {lista_par}")
print(f"Lista de impares del 1 al 20 {lista_impar}")

print("Lista 1: ", list(range(0, 101, 10)))
nombre = "Andrés Fernando Neira Vargas"
print("Lista 2: ", list(nombre))
lista = list(nombre)
print("Lista 2 invertida: ", lista[ : : -1])
print("Lista 3 ordenada ascendentemente: ", sorted(lista))
print("Lista 3 ordenada: descendentemente", sorted(lista, reverse=True))
lista = list()
print("Lista 3 vacia: ", lista)