lista = ["andrés", "fernando", "neira", "vargas", "samuel", "mary", "luz", "murcia"]

print("Lista de nombres: ", lista)
lista1 = filter(lambda x: str(x).startswith('m'), lista)
print("Lista de nombres que empiezan por 'm': ", list(lista1))
lista1 = filter(lambda x: str(x).endswith('a'), lista)
print("Lista de nombres que terminan con 'a': ", list(lista1))
texto = "mary,andres,julio,fernando, pedro, samuel, mary, juan, gabriela, gabriel"
print("Texto = ", texto)
texto = texto.replace(" ", "")
print("Texto final = ", texto)
lista1 = list(set(texto.split(',')))
print("Lista sin repetidos = ", lista1)
lista2 = filter(lambda x: str(x).startswith('g'), lista1)
print("Lista de nombres que empiezan por 'g': ", list(lista2))
lista2 = filter(lambda x: str(x).find('g'), lista1)
print("Lista de nombres eliminando los que empiezan por 'g': ", list(lista2))
lista2 = filter(lambda x: "an" in x, lista1)
print("Lista de nombres que contienen por 'an': ", list(lista2))
