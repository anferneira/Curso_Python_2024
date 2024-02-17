"""
    Realizar un programa que muestra la secuencia fibonacci de un número entero ingresado
    por teclado.

    Tenga en cuenta que la serie inicia con los números 0 y 1
"""

antp = 1
pen = 0
ult = 0

num = int(input("Digite un número entero para mostrar su serie Fibonacci: "))

print(f"La serie Fibonacci del número {num} es (", end="")

for sec in range(num):
    if (sec < num - 1):
        print(ult, end=" - ")
    else:
        print(ult, end="")
    ult = antp + pen
    antp = pen
    pen = ult

print(")")