def iniciar():
    f = int(input(f"\nDigite el número de filas de la matriz: "))
    c = int(input(f"Digite el número de columnas de la matriz: "))
    return f, c

def llenar(f, c):
    print("\nLlene la matriz\n")
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

def generar(f, c):
    print(f"\nMatriz transpuesta {f},{c}\n")
    for i in range(len(m1)):
        for j in range(len(m1[0])):
                m2[j][i] = m1[i][j]
    for i in range(c):
        for j in range(f):
            print(m2[i][j], end="\t")
        print("\n")
    if m1 == m2:
        print(f"\nLa matriz es simétrica\n")
    else:
        print(f"\nLa matriz es asimétrica\n")
    
f, c = iniciar()
if f == c:
    m1 = []
    m2 = []
    m1 = llenar(f, c)
    for i in range(c):
        m2.append([0] * f)
    print(f"\nMatriz digitada {f},{c}\n")
    for i in range(f):
        for j in range(c):
            print(m1[i][j], end="\t")
        print("\n")
    generar(f, c)
else:
    print("\nLas dimensiones deben ser iguales\n")