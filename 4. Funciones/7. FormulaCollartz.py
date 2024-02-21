"""
    En 1937 un matemático alemán llamado Lothar Collartz formuló una hipótesis intrigante
    (aún no se ha comprobado) que se puede describir de la siguiente manera:

        1. Toma cualquier número entero que no sea negativo ni 0 y asignar el nombre c0.
        2. Sí es par, evalua un nuevo c0 como c0 / 2.
        3. De lo contrario, sí es impar, evalue un nuevo c0 cómo 3 x c0 + 1.
        4. Sí c0 es diferente de 1, salta al punto 2.

    La hitótesis dice que, independientemente del valor inicial de c0, el valor siempre
    tiende a 1.

    Por supuesto, es una tarea extremadamente compleja usar una computadoraa probar la
    hipótesis de cualquier número natural (incluso puede requerir IA), pero puede usar python
    para verificar algunos números individuales. Tal vez incluso el que refutaría la hipótesis.

    Escriba un número natural y ejecute los pasos anteriores siempre que c0 sea diferente de 1.
    Tambíen queremos que cuentes los pasos necesarios para lograr el objetivo. Tu código
    también debe mostrar los pasos intermedio de c0.
"""

def comprobar(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * c0 + 1

c0 = int(input("Digite un número entero positivo: "))
pasos = 0

if c0 > 0:
    while c0 != 1:
        c0 = comprobar(c0)
        pasos += 1
        print(f"Paso {pasos}: c0: {c0}")
else:
    print("El número debe ser mayor a 0 y entero")

print(f"Total de {pasos} pasos para llegar a la solución {c0}")