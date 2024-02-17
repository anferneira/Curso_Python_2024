import math
print("Algunas funciones (métodos) del Módulo Math")
num = int(input("Digite un número entero: "))
print(f"La raiz cuadrada de {num} es {math.sqrt(num)}")
print(f"El seno de {num} es {math.sin(math.radians(num))}")
print(f"El factorial de {num} es {math.factorial(num)}")
print(f"e elevado a la {num} es {math.exp(num)}")
print(f"El exponencial de e {math.e} es {math.log(math.exp(num))}")
print(f"Número Pi {math.pi} aproximado a 4 decimales es {round(math.pi,4)}")