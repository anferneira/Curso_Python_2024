from math import ceil

def iniciar(i):
    f = int(input(f"\nDigite el número de filas de las matriz {i}: "))
    c = int(input(f"Digite el número de columnas de las matrices {i}: "))
    return f, c

def llenar(f, c, m):
    print(f"\nLlene la matriz {m}\n")
    for i in range(f):
        for j in range(c):
            if m == 1:
                m1[i][j] = float(input(f"Digite el valores (0 - 9) en la posición {i},{j}: "))
            else:
                m2[i][j] = float(input(f"Digite el valores (0 - 9) en la posición {i},{j}: "))

def multiplicar():
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                m3[i][j] += m1[i][k] * m2[k][j]
    
f1, c1 = iniciar(1)
f2, c2 = iniciar(2)
if f1 == c2:
    m1 = []
    for i in range(f1):
        m1.append([0] * c1)
    m2 = []
    for i in range(f2):
        m2.append([0] * c2)
    llenar(f1, c1, 1)
    llenar(f2, c2, 2)
    m3 = []
    for i in range(f1):
        m3.append([0] * c2)
    multiplicar()
    print("Matriz1 =", m1)
    print("Matriz2 =", m2)
    print("Resultado =", m3)
else:
    print("\nLas matrices no son multiplicables")