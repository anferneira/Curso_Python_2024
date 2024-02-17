"""
    Pida al usuario la edad y el genero del sexo, para verificar si puede pensionarse.
    Tome en cuenta que el hombre se puede pensionar a los 65 años y las mujeres a los
    60 años
"""

edad = int(input("Digite su edad: "))
genero = input("Digite su sexo: ")

if ((edad >= 65) and (genero == "masculino")) or ((edad >= 60) and (genero == "femenino")):
    print("Se puede pensionar")
else:
    print("No se puede pensionar")