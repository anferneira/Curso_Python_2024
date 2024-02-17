"""
    Programa de la Cifra del César:

    Un grupo de amigos decide organizar un juego de estrategia, para lo cual forman 2 equipos
    de 6 integrantes cada uno, donde un integrante de cada equipo es el 'jefe' y los otros 5
    son sus 'oficiales'. La regla más importante del juego es que sólo se comunicarán mediante
    un canal común, por lo que deben buscar la forma de ocultar el contenido de sus mensajes.
    
    Uno de los equipos decide utilizar un método antiguo de encriptación llamado 'La cifra
    del César', que consiste en correr cada letra del mensaje, considerando la posición de 
    cada una en el alfabeto una determinada cantidad de lugares. Ejemplo: Si el corrimiento
    es de 2 lugares, la palabra 'ATAQUE' se transforma en 'CVCSWG'.
    
    Cada día el 'jefe' del equipo debe enviar un mensaje a cada uno de sus 'oficiales'.
    
    Escribir un programa que permita encriptar los 5 mensajes. El corrimiento será dado por
    el usuario antes de comenzar a encriptar y los 5 mensajes usarán el mismo corrimiento.

    Nota: si el alfabeto termina antes de poder correr la cantidad de lugares necesarios, se
    vuelve a comenzar desde la letra 'a o A'. Ejemplo: La palabra 'EXTRA' corrida 3 lugares
    se convierte en 'HAWUD', usando el alfabeto español. El siguiente cálculo matemático
    permite volver a empezar por el principio una vez que se llegue a la letra 'z o Z':
                    (indice de la letra a correr + corrimiento) % 27

    Sólo se encriptan las letras del mensaje, el resto de caracteres no se modifican
"""

alfabeto = "abcdefghijklmnñopqrstuvwxyz"
corrimiento = int(input("Digite la cantidad de posiciones a correr: "))

for i in range(5):
    mensaje = input("\nIngrese el mensaje a encriptar: ")
    encriptado = ''
    desencriptado = ''
    for caracter in mensaje:
        if caracter.lower() in alfabeto:
            indice = alfabeto.find(caracter.lower())
            indice = (indice + corrimiento) % 27
            encriptado += alfabeto[indice]
        else:
            encriptado += caracter
    for caracter in encriptado:
        if caracter.lower() in alfabeto:
            indice = alfabeto.find(caracter.lower())
            indice = (indice - corrimiento) % 27
            desencriptado += alfabeto[indice]
        else:
            desencriptado += caracter
    print(f"\nEl mensaje encriptado es '{encriptado}'")
    print(f"El mensaje desencriptado es '{desencriptado}'")
