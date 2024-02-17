"""
    Realizar un programa que muestre la suma y cantidad de los números pares e impares que
    se ingresan por teclado
"""

dig = par = impar = cpar = cimpar = 0
correcto = 0

num = input("Cantidad de números enteros a ingresar: ")

print()

for i in num:
    if i.isdigit() == True:
        dig += 1

if dig == len(num):
    num = int(num)

if isinstance(num, int):
    for numero in range(num):
        valor = input(f"Ingrese un número en la posición {numero + 1}: ")
        dig = 0
        for i in valor:
            if i.isdigit() == True:
                dig += 1
        if dig == len(valor):
            valor = int(valor)
            if valor % 2 == 0:
                par += valor
                cpar += 1
            else:
                impar += valor
                cimpar += 1
        else:
            print("\nDebe ingresar solo valores númericos")
    print(f"\nSuma de {cpar} números pares: {par}")
    print(f"Suma de {cimpar} números impares: {impar}")
else:
    print("Debe ingresar solo valores númericos")