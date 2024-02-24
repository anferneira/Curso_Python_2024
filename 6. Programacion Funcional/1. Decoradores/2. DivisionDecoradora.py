from time import time
from os import system

def decorador(func):
    def dividirnum(*args, **kwargs):
        tiempo = time()
        print("Efectuando la división")
        resultado = func(*args, **kwargs)
        tiempo2 = time()
        print('La función tardó {:.4f} segundos en ejecutarse'.format(tiempo2 - tiempo))
        return resultado
    return dividirnum

@decorador
def division(n1, n2, n3):
    return "{:,.2f}".format(n1 / n2 / 3)

system("cls")
print(f"10,000 / 2 / 3 = {division(10000, 2, 3)}")