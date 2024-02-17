"""
    CONDICIONALES
"""

edad = int(input("Digite su edad: "))
if (edad >= 18):
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

edad = int(input("Digite su edad: "))
if (edad >= 18) and (edad < 60):
    print("Eres mayor de edad")
elif (edad >= 60):
    print("Perteneces a la tercera edad")
else:
    print("Eres menor de edad")

edad = int(input("Digite su edad: "))
if (edad < 0) and (edad >= 115):
    print("Edad invalidad")
elif (edad >= 18) and (edad < 60):
    print("Eres mayor de edad")
elif (edad >= 60):
    print("Perteneces a la tercera edad")
else:
    print("Eres menor de edad")

edad = int(input("Digite su edad: "))
if 0 < edad >= 115:
    print("Edad invalidad")
elif 18 >= edad < 60:
    print("Eres mayor de edad")
elif edad >= 60:
    print("Perteneces a la tercera edad")
else:
    print("Eres menor de edad")

edad = int(input("Digite su edad: "))
if 0 < edad >= 115:
    pass
elif 18 >= edad < 60:
    print("Eres mayor de edad")
elif edad >= 60:
    print("Perteneces a la tercera edad")
else:
    print("Eres menor de edad")