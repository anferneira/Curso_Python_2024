def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calculadora(n1, n2):
    print(f"""
        Calculadora:
          
          1. Suma
          2. Resta
          3. Multiplicación
          4. Dividir
    """)
    opcion = int(input("digite una opción: "))
    if opcion == 1:
        resp = suma(n1, n2)
        return f"{n1} + {n2} = {resp}"
    elif opcion == 2:
        resp = resta(n1, n2)
        return f"{n1} - {n2} = {resp}"
    elif opcion == 3:
        resp = multiplicar(n1, n2)
        return f"{n1} X {n2} = {resp}"
    elif opcion == 4:
        if n2 != 0:
            resp = dividir(n1, n2)
            return f"{n1} ÷ {n2} = {resp}"
        else:
            return "Error, división por 0"
    else:
        return "E"

def imprimir(r):
    if r == "E":
        print("Opción de operación no valida")
    else:
        print(r)

num1 = float(input("Digite el primer número: "))
num2 = float(input("Digite el segundo número: "))
respuesta = calculadora(num1, num2)
imprimir(respuesta)