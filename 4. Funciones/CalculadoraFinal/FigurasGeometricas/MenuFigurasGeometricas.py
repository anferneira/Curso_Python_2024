from FigurasGeometricas.FigurasGeometricas import *
from PedirDatos import solicitar_datos
import time

def datos_figuras():
    opcion = 0

    while opcion != 6:

        print("**********************************\n",
            "*         FIGURAS GEOMÉTRICAS      *\n",
            "************************************\n",
            "*            1. Cuadrado           *\n",
            "*            2. Rectángulo         *\n",
            "*            3. Círculo            *\n",
            "*            4. Triángulo          *\n",
            "*            5. Hexágono           *\n",
            "*            6. Salir              *\n",
            "************************************")

        opcion = int(input("\nDigite una opción válida: "))
        if opcion == 1:
            l = solicitar_datos("Cuadrado")
            if isinstance(l, int) == True or isinstance(l, float) == True:
                ar, pe = a_p_cuadrado(l)
                print(f"\nEl perimetro del cuadrado cuyo lado es {l} es {pe}")
                print(f"El área del cuadrado cuyo lado es {l} es {ar}")
            else:
                print("\nEl lado del cuadrado debe ser numérico\n")
        elif opcion == 2:
            b, a = solicitar_datos("Rectangulo")
            if ((isinstance(a, int) == True) and (isinstance(b, int) == True)) or ((isinstance(a, int) == True) and (isinstance(b, float) == True)) or ((isinstance(a, float) == True) and (isinstance(b, int) == True)) or ((isinstance(a, float) == True) and (isinstance(b, float) == True)):
                ar, pe = a_p_rectangulo(b, a)
                print(f"\nEl perimetro del rectangulo con base {b} y altura {a} es {pe}")
                print(f"El área del rectángulo con base {b} y altura {a} es {ar}")
            else:
                print("\nLa base y la altura deben ser numéricos\n")
        elif  opcion == 3:
            r = solicitar_datos("Circulo")
            if isinstance(r, int) == True or isinstance(r, float) == True:
                ar, pe = a_p_circulo(r)
                print(f"\nEl perimetro del círculo cuyo radio es {r} es {pe}")
                print(f"El área del círculo cuyo radio es {r} es {ar}")
            else:
                print("\nEl radio del círculo debe ser numérico\n")
        elif opcion == 4:
            l1, l2, l3 = solicitar_datos("Triangulo")
            if ((isinstance(l1, int) == True) and (isinstance(l2, int) == True) and (isinstance(l3, int) == True)) or ((isinstance(l1, float) == True) and (isinstance(l2, float) == True) and (isinstance(l3, float) == True)) or ((isinstance(l1, float) == True) and (isinstance(l2, int) == True) and (isinstance(l3, int) == True)) or ((isinstance(l1, int) == True) and (isinstance(l2, float) == True) and (isinstance(l3, int) == True)) or ((isinstance(l1, int) == True) and (isinstance(l2, int) == True) and (isinstance(l3, float) == True)) or ((isinstance(l1, float) == True) and (isinstance(l2, float) == True) and (isinstance(l3, int) == True)) or ((isinstance(l1, float) == True) and (isinstance(l2, int) == True) and (isinstance(l3, float) == True)) or ((isinstance(l1, int) == True) and (isinstance(l2, float) == True) and (isinstance(l3, float) == True)):
                ar, pe = a_p_triangulo(l1, l2, l3)
                if ar > 0:
                    print(f"\nEl perimetro del triángulo con lado1 {l1}, lado2 {l2} y lado3 {l3} es {pe}")
                    print(f"El área del triángulo con lado1 {l1}, lado2 {l2} y lado3 {l3} es {ar}")
                else:
                    print("\nÁrea indeterminada")
            else:
                print("\nLos lados deben ser numéricos\n")
        elif opcion == 5:
            l, a = solicitar_datos("Hexagono")
            if ((isinstance(l, int) == True) and (isinstance(a, int) == True)) or ((isinstance(l, int) == True) and (isinstance(a, float) == True)) or ((isinstance(l, float) == True) and (isinstance(a, int) == True)) or ((isinstance(l, float) == True) and (isinstance(a, float) == True)):
                ar, pe = a_p_hexagono(l, a)
                print(f"\nEl perimetro del hexágono con lado {l} y apotema {a} es {pe}")
                print(f"El área del hexágono con lado {l} y apotema {a} es {ar}")
            else:
                print("\nEl lado y la apotema deben ser numéricos\n")
        elif opcion == 6:
            print("\nSaliendo de figuras Geométricas ...")
            time.sleep(2)
            break
    else:
        print("\nOpción no válida")
        time.sleep(4)