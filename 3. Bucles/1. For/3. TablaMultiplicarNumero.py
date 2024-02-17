"""
    Realizar un programa que muestre la tabla de multiplicar de un número ingresado
"""

dec = dig = 0

num = input("Digite un número para mostrar su tabla de multiplicar: ")

for i in num:
    if i == ".":
        dec += 1
    elif i.isdigit() == True:
        dig += 1

if dec == 1 and dig == len(num) - 1:
    num = float(num)
elif dec == 0 and dig == len(num):
    num = int(num)

if (isinstance(num, int) or isinstance(num, float)):
    print(f"\nTabla de multiplicar del número {num}\n")
    for i in range(1, 11):
        if isinstance(num, int):
            print(f"{num} X {i} = {num * i}")
        else:
            print(f"{num} X {i} = {num * i:,.2f}")
else:
    print("\nDebe ingresar solo valores númericos")