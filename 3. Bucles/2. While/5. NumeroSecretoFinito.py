"""
    Modificar el programa del mago, indicandole al usuario, sí el número ingresado es mayor
    o menor al elegido por el mago.
"""

import random

numeroSecreto = random.randint(0, 50)
nom = input("Digite su nombre: ").title()
num = int(input("\nDigite un número entero entre 0 y 50: "))

if 0 <= num <= 50:
    while num != numeroSecreto:
        print("\n¡Ja, ja! ¡Estas atrapado en mi ciclo!")
        
        if (num < numeroSecreto):
            print("\nEl número secreto es mayor a tú número, sigue intentando")
        else:
            print("\nEl número secreto es menor a tú número, sigue intentando")

        num = int(input("\nDigite un número entero entre 0 y 50: "))
    
    print(f"\n!Bien hecho, {nom}!, adivinaste el número {num}, eres libre")
else:
    print("\nEl número debe estar entre 0 y 50")