matriz = [[1, 2, 3, 4, 5],
          [4, 3, 6, 8, 9],
          [0, 1, 8, 7, 6]]

print("La matriz es: ", matriz)
f = 0
for i in range(len(matriz)):
    c = 0
    for j in range(len(matriz)):
        print(f"matriz[{f},{c}] = {matriz[i][j]}")
        c += 1
    f += 1

matriz.append([0, 8, 7, 1, 9])
print("Agregar el arreglo[0, 8, 7, 1, 9] a la matriz: ", matriz)

matriz.remove([4, 3, 6, 8, 9])
print("Eliminar el arreglo [4, 3, 6, 8, 9] de la matriz: ", matriz)

matriz.reverse()
print("Matriz invertida: ", matriz)

matriz.sort()
print("Matriz ordenada ascendentemente: ", matriz)

matriz.sort(reverse=True)
print("Matriz ordenada descendentemente: ", matriz)