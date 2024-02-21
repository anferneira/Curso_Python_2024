from OperacionesBasicas.OperacionesBasicas import *

def operaciones_basicas():
    print("\nOperaciones Básicas\n")
    n1 = float(input("Ingrese el primer número: "))
    n2 = float(input("Ingrese el segundo número: "))
    return f"""\n
        Resultados:

        Suma:                   {n1} + {n2} = {suma(n1, n2)}
        Resta:                  {n1} - {n2} = {resta(n1, n2)}
        Multiplicación:         {n1} X {n2} = {multiplicar(n1, n2)}
        División:               {n1} ÷ {n2} = {dividir(n1, n2)}
        Módulo:                 {n1} % {n2} = {modulo(n1, n2)}
        Raiz Cuadrada de {n1}:  {raiz2(n1)}
        Raiz Cuadrada de {n2}:  {raiz2(n2)}
        Potencia:               {n1} ^ {n2} = {pow(n1, n2)}
        Raiz Cúbica de {n1}:    {raiz3(n1)}
        Raiz Cúbica de {n2}:    {raiz3(n2)}
    """