"""
    Leer varios números enteros por teclado  y sumar sus dígitos que lo componen.
    El programa termina cuandro se introduce -1
    Mostrar adicionalmente cuantos de los números introducidos son pares.
"""

par = 0
num = 0

print("El programa termina cuando se ingrese el número -1")

while num != -1:

    sum = 0
    
    num = int(input("\nDigite un número entero positivo: "))

    if num < -1:
        num *= -1
        n = num
    elif num == -1:
        n = 0
    else:
        n = num

    while n != 0:
        dig = n % 10
        sum += dig
        n //= 10
    
    if num != -1:
        print(f"\nLa suma de los digitos del número {num} es {sum}")
        
        if num % 2 == 0:
            par += 1

print(f"\nEl total de números pares introducidos fue {par}")