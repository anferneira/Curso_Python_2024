from  math import pi, sqrt

def a_p_cuadrado(lado):
    area = lado ** lado
    perimetro = 4 * lado
    return area, perimetro

def a_p_rectangulo(base, altura):
    area = base * altura
    perimetro = 2 * base + 2 * altura
    return area, perimetro

def a_p_circulo(radio):
    area = pi * radio ** radio
    perimetro = 2 * pi * radio
    return area, perimetro

def a_p_triangulo(lado1, lado2, lado3):
    perimetro = lado1 + lado2 + lado3
    semiperimetro = perimetro / 2
    res = semiperimetro * (semiperimetro - lado1) * (semiperimetro - lado2) * (semiperimetro - lado3)
    if res > 0:
        area = sqrt(res)
    else:
        area = -1
    return area, perimetro

def a_p_hexagono(lado, apotema):
    perimetro = 6 * lado
    area = perimetro * apotema / 2
    return area, perimetro