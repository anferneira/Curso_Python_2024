def iniciar():
    d = int(input(f"\nDigite la dimensión (1 - 3) de la matriz: "))
    return d

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

def det2x2(f, c, mat):
    multp = 1
    for i in range(f):
        for j in range(c):
            if i == j:
                if mat == 1:
                    multp *= m[i][j]
                elif mat == 2:
                    multp *= m2[i][j]
                elif mat == 3:
                    multp *= m3[i][j]
    mults = 1
    t = c - 1
    for i in range(f):
        for j in range(c):
            if j == t:
                if mat == 1:
                    mults *= m[i][j]
                elif mat == 2:
                    mults *= m2[i][j]
                elif mat == 3:
                    mults *= m3[i][j]
        t -= 1
    return multp, mults

def gauss(f, c):
    f1 = c1 = -1
    for i in range(0, f):
        col = []
        f1 += 1
        for j in range(0, c):
            c1 += 1
            if j < c - 1:
                col.append(m[i][j])
            else:
                col.append(m[i][j])
                col.append(m[i][0])
                col.append(m[i][1])
                break
        m1.append(col)

def intermedios(f, c, t):
    f1 = c1 = -1
    for i in range(0, f):
        col = []
        f1 += 1
        for j in range(t, c):
            c1 += 1
            col.append(m1[i][j])
        if t == 1:
            m2.append(col)
        else:
            m3.append(col)


def det3x3(f, c):
    gauss(f,c)
    print(f"\nMatriz aplicando regla de Sarrus {d},{d + 2}")    
    for i in range(d):
        for j in range(d + 2):
            print(m1[i][j], end="\t")
        print("\n")
    intermedios(f, c + 1, 1)
    intermedios(f, c + 2, 2)
    print(f"\nMatriz intermedia 1 regla de Sarrus {d},{d + 2}")    
    for i in range(d):
        for j in range(d):
            print(m2[i][j], end="\t")
        print("\n")
    print(f"\nMatriz intermedia 2 regla de Sarrus {d},{d + 2}")    
    for i in range(d):
        for j in range(d):
            print(m3[i][j], end="\t")
        print("\n")
    dp1, ds1 = det2x2(d, d, 1)
    dp2, ds2 = det2x2(d, d, 2)
    dp3, ds3 = det2x2(d, d, 3)
    return dp1 + dp2 + dp3 - ds1 - ds2 - ds3

    
    
d = iniciar()
m = []
m1 = []
m2 = []
m3 = []
m = llenar(d, d)
print(f"\nMatriz digitada {d},{d}")
for i in range(d):
    for j in range(d):
        print(m[i][j], end="\t")
    print("\n")
if d == 1:
    print(f"El determinante de la matriz es {m[0][0]}")
elif d == 2:
    dp, ds = det2x2(d, d, 1)
    print(f"\nEl determinante de la matriz {d},{d} es {dp - ds}")
elif d == 3:
    det = det3x3(d,d)
    print(f"\nEl determinante de la matriz {d},{d} es {det}")