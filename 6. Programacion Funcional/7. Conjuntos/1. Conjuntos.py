print("Conjuntos\n")
print("Conjuntos creados con {}\n")
print("\nEjemplo 1: {5, 1, 3, 2, 4}")
conjunto = {5, 1, 3, 2, 4}
print("Conjunto creado: ",conjunto)
print("\nEjemplo 2: {-1, 0, 5, -2, 1, 4}")
conjunto = {-1, 0, 5, -2, 1, 4}
print("Conjunto creado: ",conjunto)
print("\nEjemplo 3: {'e', 'o', 'a', 'u', 'i'}")
conjunto = {'e', 'o', 'a', 'u', 'i'}
print("Conjunto creado: ",conjunto)
print("\nEjemplo 4: {'e', 5, 'o', 0, 'a', 2, -1}")
conjunto = {'e', 5, 'o', 0, 'a', 2, -1}
print("Conjunto creado: ",conjunto)
print("\nEjemplo 5: {5, 1, 1, 1, 3, 5}")
conjunto = {5, 1, 1, 1, 3, 5}
print("Conjunto creado: ",conjunto)
print("\nEjemplo 6: {5, (3, 2, 4), 1, 0, 6}")
conjunto = {5, (3,2,4), 1, 0, 6}
print("Conjunto creado: ",conjunto)
print("\nEjemplo 7: {'hola', 'que', 'bien'}")
conjunto = {'hola', 'que', 'bien'}
print("Conjunto creado: ",conjunto)
print("\nUn conjunto creado por {}, no puede contener listas, diccionarios ni otros conjuntos\n")
print("Conjuntos creados con la función set()\n")
print("\nEjemplo 1: ['e', 5, 'o', 0, 'a', 2, -1]")
conjunto = set(['e', 5, 'o', 0, 'a', 2, -1])
print("Conjunto creado: ",conjunto)
print("\nEjemplo 2: String -> 'Hola'")
conjunto = set("Hola")
print("Conjunto creado: ",conjunto)
print("\nEjemplo 3: {'a':1, 'b':2, 'c':3}")
diccionario = {'a':1, 'b':2, 'c':3}
conjunto = set(diccionario.items())
print("Conjunto creado con items: ",conjunto)
conjunto = set(diccionario)
print("Conjunto creado con claves: ",conjunto)
conjunto = set(diccionario.values())
print("Conjunto creado con valores: ",conjunto)
ca = {1,2,3,4,5,6,7,8,9,10}
cb = {0,10,11,1,2,3}
print("\nConjunto A: ",ca)
print("Conjunto B: ",cb)
print("\nUnión de conjuntos")
print("Unión de conjuntos (A U B) por método union(): ",ca.union(cb))
print("Unión de conjuntos (A U B) por operador (|): ",ca | cb)
print("\nIntersección de conjuntos")
print("Intersección de conjuntos (A Ո B) por método intersection(): ",ca.intersection(cb))
print("Intersección de conjuntos (A Ո B) por operador(&): ",ca & cb)
print("\nDiferencia de conjuntos")
print("Diferencia de conjuntos (A ≠ B) por método difference(): ",ca.difference(cb))
print("Diferencia de conjuntos (A ≠ B) por operador (-): ",ca - cb)
print("Diferencia de conjuntos (B ≠ A) por método difference(): ",cb.difference(ca))
print("Diferencia de conjuntos (B ≠ A) por operador (-): ",cb - ca)
print("\nDiferencia simétrica de conjuntos")
print("Diferencia simétrica de conjuntos (A △ B) por método symmetric_difference(): ",ca.symmetric_difference(cb))
print("Diferencia simétrica de conjuntos (A △ B) por operador (^): ",ca ^ cb)
print("Diferencia simétrica de conjuntos (B △ A) por método symmetric_difference(): ",cb.symmetric_difference(ca))
print("Diferencia simétrica de conjuntos (B △ A) por operador (^): ",cb ^ ca)
print("\nAgregar un elemento a un conjunto")
c = {1,2,3,4,5,6,7,8,9,10}
print("\nConjunto: ",c)
c.add(int(input("Digite un número para agregar al conjunto: ")))
print("Conjunto: ",c)
print("\nEliminar un elemento de un conjunto")
print("\nConjunto: ",c)
c.remove(int(input("Digite un número para eliminar del conjunto (remove()): ")))
print("Conjunto: ",c)
c.discard(int(input("Digite un número para eliminar del conjunto (discard()): ")))
print("Conjunto: ",c)
c = {"azul","rojo","verde"}
l = ["amarillo","verde","negro"]
print("Conjunto: ",c)
print("Lista de nuevos valores: ",l)
print("Agregar valores al conjunto con el método update()")
c.update(l)
print("Conjunto: ",c)
print("\nRecorrer un conjunto con el ciclo for\n")
j = 1
for i in c:
    print(f"Posición {j} = {i}")
    j += 1
print("\nRecorrer un conjunto con el ciclo while\n")
i = 0
l = list(c)
while i < len(l):
    print(f"Posición {i+1} = {l[i]}")
    i += 1
