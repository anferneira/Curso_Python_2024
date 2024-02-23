import numpy as np
from math import ceil

def iniciar():
    f = int(input("\nDigite el número de filas de las matrices: "))
    c = int(input("Digite el número de columnas de las matrices: "))
    return f, c

def llenar(f, c, m):
    print(f"\nLlene la matriz {m}\n")
    f1 = c1 = -1
    fil = []
    for i in range(0, f):
        col = []
        f1 += 1
        for j in range(0, c):
            c1 += 1
            valor = float(input(f"Digite el valores (0 - 9) en la posición {i},{j}: "))
            col.append(valor)
        fil.append(col)
    return fil

def sumar():
    print("\nSuma de matrices 'm1 + m2'\n")
    suma = m1 + m2
    for i in range(len(m1)):
        if i + 1 == ceil(len(m1) / 2):
            print(m1[i], " + ", m2[i]," = ", suma[i])
        else:
            print(m1[i], "   ", m2[i],"   ", suma[i])
    

def restar():
    print("\nResta de matrices 'm1 - m2'\n")
    resta = m1 - m2
    for i in range(len(m1)):
        if i + 1 == ceil(len(m1) / 2):
            print(m1[i], " - ", m2[i]," = ", resta[i])
        else:
            print(m1[i], "   ", m2[i],"   ", resta[i])

def multiplicar():
    print("\nMultiplicación de matrices 'm1 X m2'\n")
    mult = m1 * m2
    for i in range(len(m1)):
        if i + 1 == ceil(len(m1) / 2):
            print(m1[i], " X ", m2[i]," = ", mult[i])
        else:
            print(m1[i], "   ", m2[i],"   ", mult[i])

def operaciones():
    sumar()
    restar()
    multiplicar()

m1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], float)
m2 = np.array([[3, 4, 5], [6, 7, 8], [7, 8, 9]], float)

print("     ", m1[0], "          ", m2[0])
print("m1 = ", m1[1], "     m2 = ", m2[1])
print("     ", m1[2], "          ", m2[2])

print("\nSuma de matrices 'm1 + m2'\n")

suma = m1 + m2

print(m1[0], "   ", m2[0],"   ", suma[0])
print(m1[1], " + ", m2[1]," = ", suma[1])
print(m1[2], "   ", m2[2],"   ", suma[2])

print("\nResta de matrices 'm1 - m2'\n")

resta = m1 - m2

print(m1[0], "   ", m2[0],"   ", resta[0])
print(m1[1], " - ", m2[1]," = ", resta[1])
print(m1[2], "   ", m2[2],"   ", resta[2])

print("\nMultiplicación de matrices 'm1 + m2'\n")

mult = m1 * m2

print(m1[0], "   ", m2[0],"   ", mult[0])
print(m1[1], " X ", m2[1]," = ", mult[1])
print(m1[2], "   ", m2[2],"   ", mult[2])

f, c = iniciar()
m1 = np.array(llenar(f, c, 1))
m2 = np.array(llenar(f, c, 2))
operaciones()