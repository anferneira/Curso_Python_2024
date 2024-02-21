import time

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calculadora(n1, n2):
    opcion = 0
    while opcion != 6:
        print(f"""
            Calculadora:
            
            1. Suma
            2. Resta
            3. Multiplicación
            4. Dividir
            5. Nuevos números
            6. Salir
        """)
        opcion = int(input("digite una opción: "))
        if opcion == 1:
            resp = suma(n1, n2)
            imprimir(f"{n1} + {n2} = {resp}")
        elif opcion == 2:
            resp = resta(n1, n2)
            imprimir(f"{n1} - {n2} = {resp}")
        elif opcion == 3:
            resp = multiplicar(n1, n2)
            imprimir(f"{n1} X {n2} = {resp}")
        elif opcion == 4:
            if n2 != 0:
                resp = dividir(n1, n2)
                imprimir(f"{n1} ÷ {n2} = {resp}")
            else:
                imprimir("Error, división por 0")
        elif opcion == 5:
            ingresar()
        elif opcion == 6:
            imprimir("S")
            break
        else:
            imprimir("E")

def imprimir(r):
    if r == "S":
        print("Saliste de la calculadora, vuelve pronto")
    elif r == "E":
        print("Opción de operación no valida")
    else:
        print(r)
    time.sleep(2)

def ingresar():
    num1 = float(input("Digite el primer número: "))
    num2 = float(input("Digite el segundo número: "))
    calculadora(num1, num2)

ingresar()