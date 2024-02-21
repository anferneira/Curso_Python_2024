from math import sqrt, pow

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def modulo(a, b):
    return a % b

def raiz2(a):
    if a < 0:
        a = a * -1
    return sqrt(a)

def potencia(a, b):
    return pow(a, b)

def raiz3(a):
    if a < 0:
        a = a * -1
    return pow(a, 1/3)