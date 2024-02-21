from OperacionesBasicas.MenuOperacionesBasicas import *
from SistemasNumericos.MenuSistemasNumericos import *
from FigurasGeometricas.MenuFigurasGeometricas import *
import time

opcion = 0

while opcion != 4:
    print("\n********************************\n",
            "*          CALCULADORA         *\n",
            "*      1. Operaciones Básicas  *\n",
            "*      2. Sistemas Numéricos   *\n",
            "*      3. Figuras Geométricas  *\n",
            "*      4. Salir                *\n",
            "********************************")
    
    opcion = int(input("\nDigite una opción válida: "))

    if opcion == 1:
        respuesta = operaciones_basicas()
        print(respuesta)
        print("\nSaliendo de operaciones básicas ...")
        time.sleep(4)
    elif opcion == 2:
        sistemas_numericos()
        time.sleep(4)
    elif opcion == 3:
        datos_figuras()
        time.sleep(4)
    elif opcion == 4:
        print("\nApagando calculadora ...")
        time.sleep(4)
        exit()
    else:
        print("\nOpción no válida")
        time.sleep(4)