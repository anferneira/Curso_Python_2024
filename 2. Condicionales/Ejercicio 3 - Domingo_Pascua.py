"""
    Diseñar un programa que permita calcular el domingo de Pascua de una año
    ingresado por teclado
"""

año = int(input("Digite el año a calcular: "))

a = año % 19
b = año % 4
c = año % 7
d = (19 * a + 24) % 30
e = (2 * b + 4 * c + 6 * d + 5) % 7
n = 22 + d + e

if n <= 31:
    print(f"El Domingo de Pascua es el {n} de Marzo de {año}")
else:
    print(f"El Domingo de Pascua es el {n - 31} de Abril de {año}")