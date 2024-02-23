from os import system

system('cls')

lista = []

for numero in range(1, 101):
    if numero % 2 == 0 and numero % 6 == 0:
        lista.append(numero)
    
print("Lista con números divisibles por 2 y 6:", lista)

lista = [numero for numero in range(1, 101) if numero % 2 == 0 and numero % 6 == 0]

print("Lista con números divisibles por 2 y 6:", lista)