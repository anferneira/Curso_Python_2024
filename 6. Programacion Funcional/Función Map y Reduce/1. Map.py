def comienza_letra(x):
    return x[0] == "n"

lista = ["andrés", "fernando", "neira", "vargas", "samuel"]
obj = map(comienza_letra, lista)
print("Lista =", lista)
print("Comienzan por 'n' =", list(obj))
obj = map(lambda x: x[0] == "n", lista)
print("Comienzan por 'n' =", list(obj))
