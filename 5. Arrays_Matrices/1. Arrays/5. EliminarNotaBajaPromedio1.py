"""
    Dada una cantidad de notas almacenadas en un arreglo ingresadas por teclado, 
    muestrelo en pantalla y elimine la nota más baja sin usar el método 'min'; 
    escriba en pantalla el nuevo arreglo. Saque el promedio de las notas descontando
    la nota eliminada.

    Las notas deben estar en un rango de 1 a 5

    Si hay varios registros de la nota mínima, se eliminan todos los registros mínimos

    Nota: Usar solo funciones y el programa termina cuando se ingrese el número 0
"""
array = []

def promedio():
    sum = 0
    for i in array:
        sum += i
    print(f"El promedio de las notas es: {sum / len(array)}")

def eliminar():
    min = 6
    for i in array:
        if i < min:
            min = i
    reg = 0
    for i in array:
        if i == min:
            reg += 1
    for i in range(reg):
        array.remove(min)
    print(f"La nota eliminada fué {min}")
    print(f"Notas válidas {round(array, 2)}")
    print(f"Cantidad de notas: {len(array)}")
    promedio()

def llenar():
    i = 1
    nota = 1
    while nota != 0:
        nota = float(input(f"Digite la nota {i}: ")) 
        if 1 <= nota <= 5:
            array.append(nota)
            i += 1
        elif nota == 0:
            pass
        else:
            print("La nota debe estar en un rango de 1 a 5")
    print("Notas: ", array)
    eliminar()

llenar()