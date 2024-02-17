"""
    Conversión de Número Decimal a Número Romano
"""

num = int(input("Digite un número entero entre 1 y 3999: "))

if 0 < num < 4000:
    millar = (num // 1000) * 1000 # 3000
    centena = ((num - millar) // 100) * 100 # 200
    decena = ((num - millar - centena) // 10) * 10 # 50
    unidad = num - millar - centena - decena # 4

    romano = str()

    if millar == 3000:
        romano += "MMM"
    elif millar == 2000:
        romano += "MM"
    elif millar == 1000:
        romano += "M"
    
    if centena == 900:
        romano += "CM"
    elif centena == 800:
        romano += "DCCC"
    elif centena == 700:
        romano += "DCC"
    elif centena == 600:
        romano += "DC"
    elif centena == 500:
        romano += "D"
    elif centena == 400:
        romano += "CD"
    elif centena == 300:
        romano += "CCC"
    elif centena == 200:
        romano += "CC"
    elif centena == 100:
        romano += "C"
    
    if decena == 90:
        romano += "XC"
    elif decena == 80:
        romano += "LXXX"
    elif decena == 70:
        romano += "LXX"
    elif decena == 60:
        romano += "LX"
    elif decena == 50:
        romano += "L"
    elif decena == 40:
        romano += "XL"
    elif decena == 30:
        romano += "XXX"
    elif decena == 20:
        romano += "XX"
    elif decena == 10:
        romano += "X"
    
    if unidad == 9:
        romano += "IX"
    elif unidad == 8:
        romano += "VIII"
    elif unidad == 7:
        romano += "VII"
    elif unidad == 6:
        romano += "VI"
    elif unidad == 5:
        romano += "V"
    elif unidad == 4:
        romano += "IV"
    elif unidad == 3:
        romano += "III"
    elif unidad == 2:
        romano += "II"
    elif unidad == 1:
        romano += "I"

    print(f"El número arábigo {num} en romano es {romano}")
else:
    print("Digite valores correctos")