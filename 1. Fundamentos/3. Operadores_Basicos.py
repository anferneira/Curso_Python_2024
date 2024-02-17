print("Operadores\n")
num1 = float(input("Digite el primer número: "))
num2 = float(input("Digite el segundo número: "))

"""
    OPERADORES ARITMÉTICOS
"""
print("Operadores Aritméticos\n")
print(f"Suma ==> {num1} + {num2} = {num1 + num2}")
print(f"Resta ==> {num1} - {num2} = {num1 - num2}")
print(f"Multiplicación ==> {num1} x {num2} = {num1 * num2}")
print(f"división ==> {num1} ÷ {num2} = {num1 / num2}")
print(f"Módulo ==> {num1} ÷ {num2} = {num1 % num2}")
print(f"Potencia ==> {num1} ^ {num2} = {num1 ** num2}")
print(f"División entera ==> {num1} ÷ {num2} = {num1 // num2}")

"""
    OPERADORES RELACIONALES
"""
print("\nOperadores Relacionales\n")
print(f"Mayor ==> {num1} > {num2} = {num1 > num2}")
print(f"Menor ==> {num1} < {num2} = {num1 < num2}")
print(f"Mayor o Igual ==> {num1} >= {num2} = {num1 >= num2}")
print(f"Menor o Igual ==> {num1} <= {num2} = {num1 <= num2}")
print(f"Igual ==> {num1} == {num2} = {num1 == num2}")
print(f"Diferente ==> {num1} <> {num2} = {num1 != num2}")

"""
    OPERADORES DE ASIGNACIÓN
"""
print("\nOperadores de Asignación\n")
num1 = 25
print(f"El valor inical de la variable es {num1}")
num1 += 1
print(f"Operador '+' (suma 1) ==> {num1}")
num1 -= 3
print(f"Operador '-' (resta 3) ==> {num1}")
num1 *= 2
print(f"Operador '*' (multiplíca por 2) ==> {num1}")
num1 /= 2
print(f"Operador '/' (divide por 2) ==> {num1}")
num1 %= 5
print(f"Operador '%' (módulo por 5) ==> {num1}")
num1 **= 3
print(f"Operador '**' (elevar a la 3) ==> {num1}")
num1 //= 2
print(f"Operador '//' (división entera por 2) ==> {num1}")

"""
    OPERADORES BIT A BIT
"""
print("\nOperadores bit a bit\n")
num1 = 50
num1 &= 2
print(f"El valor inical de la variable es {num1}")
print(f"Operador '&' (AND agregando 2) ==> {num1}")
num1 = 50
num1 |= 2
print(f"El valor inical de la variable es {num1}")
print(f"Operador '|' (OR agregando 2) ==> {num1}")
num1 = 50
num1 ^= 2
print(f"El valor inical de la variable es {num1}")
print(f"Operador '^' (Or exclusivo (XOR) agregando 2) ==> {num1}")
num1 = 20
print(f"El valor inical de la variable es {num1}")
num1 = num1 >> 2
print(f"Operador '>>' (Desplazamiento de 2 bit a la derecha) ==> {num1}")
num1 = 5
print(f"El valor inical de la variable es {num1}")
num1 <<= 2
print(f"Operador '<<' (Desplazamiento de 2 bit a la izquierda) ==> {num1}")

"""
    OPERADORES LÓGICOS
"""
print("\nOperadores lógicos\n")
valor1 = True
valor2 = False
res = valor1 & valor2
print(f"El valor inical de la variable1 es {valor1}")
print(f"El valor inical de la variable2 es {valor2}")
print(f"Operador '&' (AND) ==> {res}")
valor1 = False
valor2 = True
res = valor1 & valor2
print(f"El valor inical de la variable1 es {valor1}")
print(f"El valor inical de la variable2 es {valor2}")
print(f"Operador '&' (AND) ==> {res}")
valor1 = False
valor2 = False
res = valor1 & valor2
print(f"El valor inical de la variable1 es {valor1}")
print(f"El valor inical de la variable2 es {valor2}")
print(f"Operador '&' (AND) ==> {res}")
valor1 = True
valor2 = True
res = valor1 & valor2
print(f"El valor inical de la variable1 es {valor1}")
print(f"El valor inical de la variable2 es {valor2}")
print(f"Operador '&' (AND) ==> {res}")
valor1 = True
valor2 = False
res = valor1 | valor2
print(f"El valor inical de la variable1 es {valor1}")
print(f"El valor inical de la variable2 es {valor2}")
print(f"Operador '|' (OR) ==> {res}")
valor1 = False
valor2 = True
res = valor1 | valor2
print(f"El valor inical de la variable1 es {valor1}")
print(f"El valor inical de la variable2 es {valor2}")
print(f"Operador '|' (OR) ==> {res}")
valor1 = False
valor2 = False
res = valor1 | valor2
print(f"El valor inical de la variable1 es {valor1}")
print(f"El valor inical de la variable2 es {valor2}")
print(f"Operador '|' (OR) ==> {res}")
valor1 = True
valor2 = True
res = valor1 | valor2
print(f"El valor inical de la variable1 es {valor1}")
print(f"El valor inical de la variable2 es {valor2}")
print(f"Operador '|' (OR) ==> {res}")
valor1 = True
valor2 = False
res = valor1 & valor2
print(f"El valor inical de la variable1 es {valor1}")
print(f"El valor inical de la variable2 es {valor2}")
print(f"Operador '&' (AND) ==> {res}")
valor1 = False
valor2 = True
res = valor1 & valor2
print(f"El valor inical de la variable1 es {valor1}")
print(f"El valor inical de la variable2 es {valor2}")
print(f"Operador '&' (AND) ==> {res}")
valor1 = False
valor2 = False
res = valor1 & valor2
print(f"El valor inical de la variable1 es {valor1}")
print(f"El valor inical de la variable2 es {valor2}")
print(f"Operador '&' (AND) ==> {res}")
valor1 = True
res = not(valor1)
print(f"El valor inical de la variable es {valor1}")
print(f"Operador 'not' (Negación) ==> {res}")
valor1 = False
res = not(valor1)
print(f"El valor inical de la variable es {valor1}")
print(f"Operador 'not' (Negación) ==> {res}")