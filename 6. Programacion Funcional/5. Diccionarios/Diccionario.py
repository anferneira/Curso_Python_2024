print("Diccionario")
opcion = 0
Diccionario = {}
valor1 = 0
while (opcion != 16):
    print("\nMenú de opciones")
    print("\n1. Agregar datos a diccionario")
    print("2. Imprimir Diccionario")
    print("3. Ver items del Diccionario")
    print("4. Ver claves del Diccionario")
    print("5. Ver valores del Diccionario")
    print("6. Modificar o agregar datos en el diccionario")
    print("7. Modificar o agregar datos en el diccionario con el método update()")
    print("8. Eliminar todos los registros del Diccionario")
    print("9. Eliminar primer registro del Diccionario")
    print("10. Eliminar último registro del Diccionario")
    print("11. Eliminar un registro del Diccionario")
    print("12. Copia del diccionario")
    print("13. Ejemplo de diccionario con el método fromkeys()")
    print("14. Ejemplo de diccionario con el método get()")
    print("15. Ejemplo de diccionario con el método setdefault()")
    print("16. Salir")
    opcion = int(input("\nDigite una opcion: "))
    if (opcion == 1):
        i = 1
        claves = list(Diccionario.keys())
        for j in claves:
            clave = "DICC-" + str(i)
            for k in claves:
                if (k == clave):
                   i += 1
        clave = "DICC-" + str(i)
        print(f"\nAgregar registro {i} al diccionario.")
        valor = input("Digite el valor del registro: ")
        Diccionario[clave] = valor
    elif (opcion == 2):
        print("\nDiccionario de datos:\n")
        i = 1
        for key in Diccionario:
            print(f"{i}. {key} : {Diccionario[key]}")
            i += 1
    elif (opcion == 3):
        print("\nItems del diccionario")
        j = 1
        items = list(Diccionario.items())
        for i in items:
            print(f"{j}.",i)
            j += 1
    elif (opcion == 4):
        print("\nClaves del diccionario")
        j = 1
        claves = list(Diccionario.keys())
        for i in claves:
            print(f"{j}.",i)
            j += 1
    elif (opcion == 5):
        print("\nValores del diccionario")
        j = 1
        valores = list(Diccionario.values())
        for i in valores:
            print(f"{j}.",i)
            j += 1
    elif (opcion == 6):
        print("\nModificar o agregar datos en el diccionario")
        print("Lista de registros en el diccionario\n")
        i = 1
        for key in Diccionario:
            print(f"{i}. {key} : {Diccionario[key]}")
            i += 1
        opcion1 = int(input(f"\nDigite la opcíon del registro a cambiar: "))
        i = 1
        claves = list(Diccionario.keys())
        for j in claves:
            clave = "DICC-" + str(i)
            for k in claves:
                if (k == clave):
                   i += 1
        clave = "DICC-" + str(i)
        lista = list(Diccionario.values())
        if (opcion1 <= len(lista)):
            print(f"\nEl valor actual de la clave '{claves[opcion1-1]}' es: {lista[opcion1-1]}")
            valor = input(f"Digite el nuevo valor del registro con clave '{claves[opcion1-1]}': ")
            Diccionario[claves[opcion1-1]] = valor
        else:
            valor = input(f"Digite el valor del nuevo registro ({i}) con clave '{clave}': ")
            Diccionario[clave] = valor
    elif (opcion == 7):
        print("\nModificar o agregar datos en el diccionario update()")
        print("Lista de registros en el diccionario\n")
        i = 1
        for key in Diccionario:
            print(f"{i}. {key} : {Diccionario[key]}")
            i += 1
        opcion1 = int(input(f"\nDigite la opcíon del registro a cambiar: "))
        claves = list(Diccionario.keys())
        datos = list(Diccionario.values())
        if ((opcion1 > 0 ) and (len(claves) >= opcion1)):
            print(clave)
            print(f"\nEl valor actual de la clave '{claves[opcion1-1]}' es: {datos[opcion1-1]}")
            valor = input(f"Digite el nuevo valor del registro con clave 'DICC-{opcion1}': ")
            dic ={}
            dic[claves[opcion1-1]] = valor
            valor = list(dic.items())
            Diccionario.update({valor[0]})
        else:
            i = 1
            for j in claves:
                clave = "DICC-" + str(i)
                for k in claves:
                    if (k == clave):
                        i += 1
            clave = "DICC-" + str(i)
            dic ={}
            print("\nEl registro no existe, se creará uno nuevo")
            valor = input(f"Digite el valor del registro con clave '{clave}': ")
            dic[clave] = valor
            valor = list(dic.items())
            Diccionario.update({valor[0]})
        print(Diccionario)
    elif (opcion == 8):
        Diccionario.clear()
        print("\nSe eliminaron los resgistros del diccionario")
    elif (opcion == 9):
        claves = list(Diccionario.keys())
        Diccionario.pop(claves[0])
        print("\nSe eliminó el primer registro del diccionario")
    elif (opcion == 10):
        Diccionario.popitem()
        print("\nSe eliminó el último registro del diccionario")
    elif (opcion == 11):
        print("\nEliminar datos del diccionario")
        print("Lista de registros en el diccionario\n")
        i = 1
        for key in Diccionario:
            print(f"{i}. {key} : {Diccionario[key]}")
            i += 1
        opcion1 = int(input(f"\nDigite la opcíon del registro a eliminar: "))
        claves = list(Diccionario.keys())
        clave = claves[opcion1-1]
        Diccionario.pop(clave,"No se encontro el registro en el diccionario")
        print(f"\nSe eliminó el registro del diccionario con clave '{clave}'")
    elif (opcion == 12):
        print("\nDiccionario de original: ",Diccionario)
        d = Diccionario.copy()
        print("\nDiccionario copia: ",d)
    elif (opcion == 13):
        print("\nEjemplos de diccionarios con formkeys()")
        secuencia = ["uno","dos","tres"]
        diccionario = dict.fromkeys(secuencia)
        print("Secuencia con lista sin valor: ",diccionario)
        secuencia = ["uno","dos","tres"]
        valor = 5
        diccionario = dict.fromkeys(secuencia,valor)
        print("Secuencia con lista y valor: ",diccionario)
        secuencia = {"uno": 1,"dos": 2,"tres": 3}
        print("Diccionario original: ",secuencia)
        valor = 5
        diccionario = dict.fromkeys(secuencia,valor)
        print("Secuencia con diccionario y valor: ",diccionario)
        secuencia = "HOLA"
        valor = 5
        diccionario = {}.fromkeys(secuencia,valor)
        print("Secuencia con texto y valor: ",diccionario)
        secuencia = "HOLA"
        valor = [1,2,"ESO"]
        diccionario = {}.fromkeys(secuencia,valor)
        print("Secuencia con texto y lista: ",diccionario)
        secuencia = "HOLA"
        valor = {"Juan": 25, "María": 22}
        diccionario = {}.fromkeys(secuencia,valor)
        print("Secuencia con texto y diccionario: ",diccionario)
    elif (opcion == 14):
        print("\nEjemplos de diccionarios con get()")
        diccionario = {"uno": 1,"dos": 2,"tres": 3}
        print("Diccionario: ",diccionario)
        valor = diccionario.get("uno")
        print(f"El valor de la clave 'uno': ",valor)
        valor = diccionario.get("dos")
        print(f"El valor de la clave 'dos': ",valor)
        valor = diccionario.get("tres")
        print(f"El valor de la clave 'tres': ",valor)
        valor = diccionario.get("cuatro")
        print(f"El valor de la clave 'cuatro': ",valor)
        valor = diccionario.get("cuatro", 4)
        print(f"Como el valor de la clave 'cuatro' no existe, asignamos el valor: ",valor)
    elif (opcion == 15):
        print("\nEjemplos de diccionarios con setdefault()")
        diccionario = {"uno": 1,"dos": 2,"tres": 3}
        print("Diccionario: ",diccionario)
        valor = diccionario.setdefault("uno",5)
        print(f"El valor retornado de ('uno',5): ",valor)
        print(f"Diccionario: ",diccionario)
        valor = diccionario.setdefault("cuatro")
        print(f"El valor retornado de ('cuatro'): ",valor)
        print(f"Diccionario: ",diccionario)
        valor = diccionario.setdefault("cinco",5)
        print(f"El valor retornado de ('cinco',5): ",valor)
        print(f"Diccionario: ",diccionario)
