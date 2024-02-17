num1= 5
num2 = 3
mensaje = "Suma ="
resultado = num1 + num2

print("Suma =",resultado)
print(mensaje,resultado)

print("\nTipos de datos")
print("float: Número con coma decimal")
print("int: Número entero")
print("complex: Número complejo")
print("str: Cadena de texto String")
print("bool: Valor booleano")
print("list: Lista de datos")
print("tuple: Tupla de datos inmutables")
print("range: Secuencia de datos inmutables")
print("dict: Diccionario de datos (clave - valor)")
print("set - frozenset: Conjunto de datos únicos e inmutables")
print("bytes: Secuencia inmutable de bytes")
print("bytearray: Secuencia mutables de bytes\n")

mensaje = input("Digite su nombre: ")
num1 = int(input("Digite el primer número entero: "))
num2 = int(input("Digite el segundo número entero: "))
resultado1 = num1 + num2

print(mensaje,"la suma es",resultado1)

resultado2 = str(num1) + str(num2)

print(mensaje,"unir",num1,"y",num2,"es",resultado2)

resultado1 = True
print("\nValor",resultado1)
resultado2 = False
print("Valor",resultado2)

num1 = 8
num2 = 3
print(num1,"es mayor a",num2,"=",num1>num2)
print(num1,"es menor a",num2,"=",num1<num2)
print(num1,"es igual a",num2,"=",num1==num2)
num1 = 3
print(num1,"es igual a",num2,"=",num1==num2)
resultado1 = num1 + num2