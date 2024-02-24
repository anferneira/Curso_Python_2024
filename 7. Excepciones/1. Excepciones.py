from os import system

system('cls')

try:
    print(5 / 0)
except:
    print("5 ÷ 0 = Error al dividir por 0 ")

try:
    print(x)
except:
    print("Valor de la variable x = 'La variable no existe'")

try:
    suma(5, 4)
except:
    print("5 + 4 = La función suma no existe")

lista = [8, 10, 4, 2, 9]
try:
    print("La lista es", lista)
    for i in range(-1, len(lista)):
        print(f"[pos {i + 1}: {lista[i + 1]}]", end=" ")
except:
    print(f"[pos {i + 1}: No exite]", end=" ")
else:
    print("==> Ejecución correcta")
finally:
    print("==> Fin.")

try:
    print("La lista es", lista)
    for i in range(0, len(lista)):
        print(f"[pos {i}: {lista[i]}]", end=" ")
except:
    print(f"[pos {i + 1}: No exite]")
else:
    print("==> Ejecución correcta", end=" ")
finally:
    print("==> Fin.")

try:
    print(5 / 0)
except ZeroDivisionError:
    print(f"5 ÷ 0 = Error al dividir por 0")

try:
    print(5 / 0)
except ZeroDivisionError:
    print(f"5 ÷ 0 = Error al dividir por 0: {ZeroDivisionError}")

try:
    print(x)
except NameError:
    print(f"Valor de la variable x = 'La variable no existe': {NameError}")

try:
    x = int(input("Digite un número entero: "))
except ValueError:
    print(f"El valor de la variable debe ser de tipo númerico y entero: {ValueError}")

try:
    print("La lista es", lista)
    for i in range(-1, len(lista)):
        print(f"[pos {i + 1}: {lista[i + 1]}]", end=" ")
except IndexError:
    print(f"[pos {i + 1}: No exite]: {IndexError}")

try:
    print("La lista es", lista)
    for i in range(-1, len(lista)):
        print(f"[pos {i + 1}: {lista[i + 1]}]", end=" ")
except IndexError as e:
    print(f"[pos {i + 1}: No exite]: {e}")

try:
    x = int(input("Digite un número entero: "))
    print(p)
    print(5 / 0)
except ValueError:
    print(f"El valor de la variable debe ser de tipo númerico y entero")
except NameError:
    print(f"Valor de la variable x = 'La variable no existe'")
except ZeroDivisionError:
    print(f"5 ÷ 0 = Error al dividir por 0")