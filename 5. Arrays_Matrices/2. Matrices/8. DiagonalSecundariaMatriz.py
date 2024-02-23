def iniciar():
    f = int(input(f"\nDigite el número de filas de la matriz: "))
    c = int(input(f"Digite el número de columnas de la matriz: "))
    return f, c

def llenar(f, c):
    print(f"\nLlene la matriz\n")
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
    print(f"\nMatriz diagonal secundaria {f},{c}\n")
    sum = 0
    t = c - 1
    for i in range(f):
        mc = []
        for j in range(c):
            if j == t:
                mc.append(m1[i][j])
                sum += m1[i][j]
            else:
                mc.append(0)
        t -= 1
        m2.append(mc)
    for i in range(f):
        for j in range(c):
            print(m2[i][j], end="\t")
        print("\n")
    print(f"La suma de la diagonal secundaria es {sum}")
    
f, c = iniciar()
if f == c:
    m1 = []
    m2 = []
    m1 = llenar(f, c)
    print(f"\nMatriz digitada {f},{c}\n")
    for i in range(f):
        for j in range(c):

            print(m1[i][j], end="\t")
        print("\n")
    generar(f, c)
else:
    print("\nLas dimensiones de la matriz no son iguales")