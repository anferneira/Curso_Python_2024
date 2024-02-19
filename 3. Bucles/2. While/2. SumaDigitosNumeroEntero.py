"""
    Leer un número entero por teclado los sumar sus dígitos que lo componen
"""

sum = 0
i = 0

print("El programa termina cuando se ingrese el número 0")
num = int(input("\nDigite un número entero positivo: "))

if num < 0:
    num *= -1

n = num

while n != 0:
    dig = n % 10
    sum += dig
    n //= 10

print(f"\nLa suma de los digitos del número {num} es {sum}")