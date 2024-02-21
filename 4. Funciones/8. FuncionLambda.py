import math

sumar = lambda a, b: a + b
potencia = lambda a , b: pow(a, b)
fact = lambda a: math.factorial(a)

print(f"2 + 3 = {sumar(2, 3)}")
print(f"2 ^ 3 = {potencia(2, 3)}")
print(f"El factorial de {5} es {fact(5)}")