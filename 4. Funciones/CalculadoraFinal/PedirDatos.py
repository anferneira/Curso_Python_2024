def solicitar_datos(figura):
    if figura == "Cuadrado":
        l = input("\nDigite el lado del cuadrado: ") 
        num = fl = 0
        for i in l:
            if i in '0123456789.':
                if i == '.':
                    fl += 1
                    if fl > 1:
                        num = 1
                        break
                pass
            else:
                num = 1
                break                 
        if (num == 0 and fl == 0) or (num == 0 and fl == 1):
            if num == 0 and fl == 0:
                return int(l)
            else:
                return float(l)
        else:
            return l
    elif figura == "Rectangulo":
        b = input("\nDigite la base del rectángulo: ")
        a = input("\nDigite la altura del rectángulo: ")
        num1 = num2 = fl1 = fl2 = 0
        for i in b:
            if i in '0123456789.':
                if i == '.':
                    fl1 += 1
                    if fl1 > 1:
                        num1 = 1
                        break
                pass
            else:
                num1 = 1
                break
        for i in a:
            if i in '0123456789.':
                if i == '.':
                    fl2 += 1
                    if fl2 > 1:
                        num2 = 1
                        break
                pass
            else:
                num2 = 1
                break
        if (num1 == 0 and fl1 == 0 and num2 == 0 and fl2 == 0) or (num1 == 0 and fl1 == 1 and num2 == 0 and fl2 == 1) or (num1 == 0 and fl1 == 0 and num2 == 0 and fl2 == 1) or (num1 == 0 and fl1 == 1 and num2 == 0 and fl2 == 0):
            if num1 == 0 and fl1 == 0 and num2 == 0 and fl2 == 0:
                return int(b), int(a)
            elif num1 == 0 and fl1 == 0 and num2 == 0 and fl2 == 1:
                return int(b), float(a)
            elif num1 == 0 and fl1 == 1 and num2 == 0 and fl2 == 0:
                return float(b), int(a)
            else:
                return float(b), float(a)
        else:
            return b, a
    elif figura == "Circulo":
        r = input("\nDigite el radio del círculo: ") 
        num = fl = 0
        for i in r:
            if i in '0123456789.':
                if i == '.':
                    fl += 1
                    if fl > 1:
                        num = 1
                        break
                pass
            else:
                num = 1
                break                 
        if (num == 0 and fl == 0) or (num == 0 and fl == 1):
            if num == 0 and fl == 0:
                return int(r)
            else:
                return float(r)
        else:
            return r
    elif figura == "Triangulo":
        l1 = input("\nDigite el lado1 del triángulo: ")
        l2 = input("\nDigite el lado2 del triángulo: ")
        l3 = input("\nDigite el lado3 del triángulo: ")
        num1 = num2 = num3 = fl1 = fl2 = fl3 = 0
        for i in l1:
            if i in '0123456789.':
                if i == '.':
                    fl1 += 1
                    if fl1 > 1:
                        num1 = 1
                        break
                pass
            else:
                num1 = 1
                break
        for i in l2:
            if i in '0123456789.':
                if i == '.':
                    fl2 += 1
                    if fl2 > 1:
                        num2 = 1
                        break
                pass
            else:
                num2 = 1
                break
        for i in l3:
            if i in '0123456789.':
                if i == '.':
                    fl3 += 1
                    if fl3 > 1:
                        num3 = 1
                        break
                pass
            else:
                num2 = 1
                break
        if (num1 == 0 and fl1 == 0 and num2 == 0 and fl2 == 0 and num3 == 0 and fl3 == 0) or (num1 == 0 and fl1 == 0 and num2 == 0 and fl2 == 0 and num3 == 0 and fl3 == 1) or (num1 == 0 and fl1 == 0 and num2 == 0 and fl2 == 1 and num3 == 0 and fl3 == 0) or (num1 == 0 and fl1 == 1 and num2 == 0 and fl2 == 0 and num3 == 0 and fl3 == 0) or (num1 == 0 and fl1 == 1 and num2 == 0 and fl2 == 1 and num3 == 0 and fl3 == 0) or (num1 == 0 and fl1 == 1 and num2 == 0 and fl2 == 0 and num3 == 0 and fl3 == 1) or (num1 == 0 and fl1 == 0 and num2 == 0 and fl2 == 1 and num3 == 0 and fl3 == 1) or (num1 == 0 and fl1 == 1 and num2 == 0 and fl2 == 1 and num3 == 0 and fl3 == 1):
            if num1 == 0 and fl1 == 0 and num2 == 0 and fl2 == 0 and num3 == 0 and fl3 == 0:
                return int(l1), int(l2), int(l3)
            elif num1 == 0 and fl1 == 0 and num2 == 0 and fl2 == 0 and num3 == 0 and fl3 == 1:
                return int(l1), int(l2), float(l3)
            elif num1 == 0 and fl1 == 0 and num2 == 0 and fl2 == 1 and num3 == 0 and fl3 == 0:
                return int(l1), float(l2), int(l3)
            elif num1 == 0 and fl1 == 1 and num2 == 0 and fl2 == 0 and num3 == 0 and fl3 == 0:
                return float(l1), int(l2), int(l3)
            elif num1 == 0 and fl1 == 1 and num2 == 0 and fl2 == 1 and num3 == 0 and fl3 == 0:
                return float(l1), float(l2), int(l3)
            elif num1 == 0 and fl1 == 1 and num2 == 0 and fl2 == 0 and num3 == 0 and fl3 == 1:
                return float(l1), int(l2), float(l3)
            elif num1 == 0 and fl1 == 0 and num2 == 0 and fl2 == 1 and num3 == 0 and fl3 == 1:
                return int(l1), float(l2), float(l3)
            else:
                return float(l1), float(l2), float(l3)
        else:
            return l1, l2, l3
    elif figura == "Hexagono":
        l = input("\nDigite el lado del hexágono: ")
        a = input("\nDigite el apotema del hexágono: ")
        num1 = num2 = fl1 = fl2 = 0
        for i in l:
            if i in '0123456789.':
                if i == '.':
                    fl1 += 1
                    if fl1 > 1:
                        num1 = 1
                        break
                pass
            else:
                num1 = 1
                break
        for i in a:
            if i in '0123456789.':
                if i == '.':
                    fl2 += 1
                    if fl2 > 1:
                        num2 = 1
                        break
                pass
            else:
                num2 = 1
                break
        if (num1 == 0 and fl1 == 0 and num2 == 0 and fl2 == 0) or (num1 == 0 and fl1 == 1 and num2 == 0 and fl2 == 1) or (num1 == 0 and fl1 == 0 and num2 == 0 and fl2 == 1) or (num1 == 0 and fl1 == 1 and num2 == 0 and fl2 == 0):
            if num1 == 0 and fl1 == 0 and num2 == 0 and fl2 == 0:
                return int(l), int(a)
            elif num1 == 0 and fl1 == 0 and num2 == 0 and fl2 == 1:
                return int(l), float(a)
            elif num1 == 0 and fl1 == 1 and num2 == 0 and fl2 == 0:
                return float(l), int(a)
            else:
                return float(l), float(a)
        else:
            return l, a