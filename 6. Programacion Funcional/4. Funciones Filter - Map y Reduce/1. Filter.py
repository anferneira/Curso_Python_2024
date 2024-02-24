numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Lista de números: {numeros}")
resultado = filter(lambda x: x % 2 == 0, numeros)
print(f"Lista de pares: {list(resultado)}")
resultado = filter(lambda x: x % 2 == 1, numeros)
print(f"Lista de impares: {list(resultado)}")
