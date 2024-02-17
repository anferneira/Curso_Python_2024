"""
    Muchos son los cambios que tenemos en nuestro cuerpo, debido a ciertos factores como
    son: la alimentación, el control de peso, entre otros. Un paciente se encuentra 
    preocupado por la salud de su núcleo familiar y encuentra un artículo sobre cómo llevar
    el control de peso, conocido como 'Indice de masa corporal - IMC' para adultos de 20
    años o más. El IMC permite establecer una clasificación al relacionar el peso en metros
    con el peso en kilogramos; la relación está determinada por el peso en (kg) / estatura (m)
    elevada al cuadrado, que determina un indice y a su vez el nivel de peso (bajo, normal, 
    sobrepeso y obeso)
"""

edad = int(input("Digite su edad: "))
peso = float(input("Digite su peso en (kg): "))
estatura = float(input("Digite su estatura en (m): "))

imc = peso / estatura ** 2

if edad >= 20:
    print(f"Su IMC es de {imc}")
    if imc < 18.5:
        print(f"Diagnostico: 'Bajo peso'")
    elif 18.5 <= imc < 25:
        print(f"Diagnostico: 'Peso normal'")
    elif 25 <= imc < 30:
        print(f"Diagnostico: 'Sobrepeso'")
    elif imc >= 30:
        print(f"Diagnostico: 'Obesidad'")
    else:
        print(f"Valores erroneos")
else:
    print("No se puede calcular el IMC por ser menor de edad")