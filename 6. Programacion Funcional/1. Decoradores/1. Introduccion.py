from os import system

def mi_decorador(funcion):
    def factor(n):
        fac = funcion(n)
        print(f"El factorial de {n} es {fac}")
        return fac
    return factor

def mi_decorador1(funcion):
    def operar(a, b):
        print("Se va a llamar la ", end="")
        c = funcion(a, b)
        return c
    return operar

def mi_decorador2(arg):
    def mi_decorador_real(funcion):
        def operar(a, b):
            print(arg)
            print("Se va a llamar la ", end="")
            c = funcion(a, b)
            return c
        return operar
    return mi_decorador_real

@mi_decorador
def factorial(n):
    f = 1
    while (n > 0):
        f = f * n
        n -= 1
    return f

@mi_decorador1
def suma(a, b):
    print("función suma")
    print(f"{a} + {b} = ", end="")
    return a + b

@mi_decorador1
def resta(a, b):
    print("función resta")
    print(f"{a} - {b} = ", end="")
    return a - b

@mi_decorador1
def multiplicar(a, b):
    print("función multiplicar")
    print(f"{a} * {b} = ", end="")
    return a * b

@mi_decorador1
def dividir(a, b):
    print("función dividir")
    print(f"{a} / {b} = ", end="")
    return a / b

@mi_decorador2("Decorador")
def sumar(a, b):
    print("función suma")
    print(f"{a} + {b} = ", end="")
    return a + b

system("cls")
factorial(5)
print(suma(5, 2))
print(resta(5, 2))
print(multiplicar(5, 2))
print(dividir(5, 2))
print(sumar(5, 2))