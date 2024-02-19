"""
    Un mago junior ha elegido un número secreto. Lo ha escondido en una variable llamada
    'numeroSecreto'. Quiere que todos los que ejecuten su programa jueguen al juego
    'Adivina el número secreto' y adivien el número que ha elegido para ellos. ¡Quienes
    no adivinen el número quedarán atrapados en un ciclo sin fin para siempre!. 
    Desafortunadamente el mago no sabe como completar el código.

    Tu tarea es ayudar al mago a completar su código de tal manera que:

        * Pedirá al usuario introducir su nombre.
        * El usuario debe ingresar un número entero.
        * Se debe usar el ciclo While.
        * Comprobar si el número introducido por el usuario es el mismo que el escogido
          por el mago. Si el número elegido por el usuario es diferente del número secreto
          del mago, deberá mostrar el mensaje '¡Ja, ja! ¡Estas atrapado en mi ciclo!' y se
          le solicitará que ingrese un nuevo número. Si el número ingresado por el usuario
          coincide con el número elegido por el mago, debe mostrar el siguiente mensaje en
          pantalla '!Bien hecho <nombreusuario>!, adivinaste el número <numero>, eres libre'

    El mago cuenta contigo!, no lo decepciones.

"""

import random

numeroSecreto = random.randint(0, 50)
nom = input("Digite su nombre: ").title()
num = int(input("\nDigite un número entero entre 0 y 50: "))

if 0 <= num <= 50:
    while num != numeroSecreto:
        print("\n¡Ja, ja! ¡Estas atrapado en mi ciclo!")
        num = int(input("\nDigite un número entero entre 0 y 50: "))
    
    print(f"\n!Bien hecho, {nom}!, adivinaste el número {num}, eres libre")
else:
    print("\nEl número debe estar entre 0 y 50")