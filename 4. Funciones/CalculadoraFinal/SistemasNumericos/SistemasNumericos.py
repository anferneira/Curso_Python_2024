def decimal():
    d = input("Introduzca un número decimal (Base 10): ")
    r = validar(d, 10)
    if r == len(d):
        d = int(d)
        b = str(bin(d))
        o = str(oct(d))
        h = str(hex(d))
        return f"""\n
                Resultados de la conversión:\n
                    1. El número decimal {d:,} en binario es {b[2: len(b)]}\n
                    2. El número decimal {d:,} en octal es {o[2: len(o)]}\n
                    3. El número decimal {d:,} en hexadecimal es {h[2: len(h)].upper()}\n
                """
    else:
        return "\nDebe ingresar números compuestos de 0 - 9"

def binario():
    b = input("Introduzca un número binario (Base 2): ")
    r = validar(b, 2)
    if r == len(b):
        d = int(b, base=2)
        o = str(oct(d))
        h = str(hex(d))
        return f"""
                Resultados de la conversión:\n
                    1. El número binario {b} en decimal es {d:,}\n
                    2. El número binario {b} en octal es {o[2: len(o)]}\n
                    3. El número binario {b} en hexadecimal es {h[2: len(h)].upper()}\n
                """
    else:
        return "\nDebe ingresar números compuestos de 0 - 1"

def octal():
    o = input("Introduzca un número octal (Base 10): ")
    r = validar(o, 8)
    if r == len(o):
        d = int(o, base=8)
        b = str(bin(d))
        h = str(hex(d))
        return f"""
                Resultados de la conversión:\n
                    1. El número octal {o} en decimal es {d:,}\n
                    2. El número octal {o} en binario es {b[2: len(b)]}\n
                    3. El número octal {o} en hexadecimal es {h[2: len(h)].upper()}\n
                """
    else:
        return "\nDebe ingresar números compuestos de 0 - 7"
    

def hexadecimal():
    h = input("Introduzca un número hexadecimal (Base 16): ").upper()
    r = validar(h, 16)
    if r == len(h):
        d = int(h, base=16)
        b = str(bin(d))
        o = str(oct(d))
        return f"""
                Resultados de la conversión:\n
                    1. El número hexadecimal {h.upper()} en decimal es {d:,}\n
                    2. El número hexadecimal {h.upper()} en binario es {b[2: len(b)]}\n
                    3. El número hexadecimal {h.upper()} en octal es {o[2: len(o)]}\n
                """
    else:
        return "\nDebe ingresar números compuestos de 0 - 9 y/o caracteres cde la A - F"
    
def validar(num, base):
    dig = 0
    if base == 10:
        for i in num:
            if i.isdigit() == True and int(i) >= 0 and int(i) <= 9:
               dig += 1
            else:
               return 0
        return dig
    elif base == 2:
        for i in num:
            if i.isdigit() == True and (int(i) == 0 or int(i) == 1):
               dig += 1
            else:
                return 0
        return dig
    elif base == 8:
        for i in num:
            if i.isdigit() == True and int(i) >= 0 and int(i) <= 7:
               dig += 1
            else:
               return 0
        return dig
    else:
        num = str(num).upper()
        for i in num:
            if i.isdigit() == True or (ord(i) >= 65 and ord(i) <= 70):
               dig += 1
            else:
               return 0
        return dig