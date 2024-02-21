from SistemasNumericos.SistemasNumericos import *
import time

def sistemas_numericos():
    opcion = 0

    while opcion != 5:
        print("******************************************\n",
              "*            SISTEMAS NÚMÉRICOS          *\n",
              "*        ¿Qué base desea convertir?      *\n",
              "******************************************\n",
              "*            1. Decimal                  *\n",
              "*            2. Binario                  *\n",
              "*            3. Octal                    *\n",
              "*            4. Hexadecimal              *\n",
              "*            5. Salir                    *\n",
              "******************************************")
        
        opcion = int(input("Digite una opción válida: "))

        if opcion == 1:
            print(decimal())
            time.sleep(4)
        elif opcion == 2:
            print(binario())
            time.sleep(4)
        elif opcion == 3:
            print(octal())
            time.sleep(4)
        elif opcion == 4:
            print(hexadecimal())
            time.sleep(4)
        elif opcion == 5:
            print("\nSaliendo de sistemas numéricos ...")
        else:
            print("\nOpción no válida")
            time.sleep(4)