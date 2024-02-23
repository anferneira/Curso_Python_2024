def iniciar():
    f = int(input(f"\nDigite el número de filas de la matriz: "))
    c = int(input(f"Digite el número de columnas de la matriz: "))
    return f, c

def generar(f, c):
    print(f"\nMatriz {f},{c}\n")
    for i in range(f):
        mc = []
        for j in range(c):
            if i == j:
                mc.append(1)
            else:
                mc.append(0)
        m.append(mc)
    for i in range(f):
        for j in range(c):
            print(m[i][j], end="\t")
        print("\n")
    
f, c = iniciar()
if f == c:
    m = []
    generar(f, c)
else:
    print("\nLas dimensiones de la matriz no son iguales")