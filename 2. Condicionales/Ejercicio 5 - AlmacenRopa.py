"""
    Un almacen de venta de ropa tiene las siguientes promociones para sus clientes,
    dependiendo que si es pago en efectivo (E), pago con tarjeta débito (TD) o si es
    pago con tarjeta de crédito (TC):
    
        a. Para ventas menores o iguales a 200.000, con pago en efectivo su descuento
           es del 20%, si es con tarjeta débito del 10% y con tarjeta de crédito del 5%.
        b. Para ventas mayores a 200.000 y menores o iguales a 500.000, con pago en
           efectivo su descuento es del 30%, si es con tarjeta débito del 20% y con tarjeta
           de crédito del 10%.
        c. Para ventas mayores a 500.000, con pago en efectivo su descuento es del 40%, si
           es con tarjeta débito del 30% y con tarjeta de crédito del 18%.

    El programa debe solicitar el monto a pagar sin descuento y el tipo de pago.
    El programa debe mostrar el monto a pagar, el tipo de pago, el monto del descuento y el 
    total a pagar.
"""

print("Tipos de pago:")
print("E. Efectivo")
print("TD. Tarjeta Débito")
print("TC. Tarjeta Crédito\n")
tp = input("Digite el tipo de pago: ").upper()

print()

if tp == "E":
    tp = "Efectivo (E)"
    montoP = float(input("Digite el monto a pagar: "))
    desc1 = montoP * 0.20
    desc2 = montoP * 0.30
    desc3 = montoP * 0.40
    porc1 = 20
    porc2 = 30
    porc3 = 40
    if 0 < montoP <= 200000:
        print("\nDatos de Factura:\n")
        print(f"Monto a pagar: ${montoP:,.2f}")
        print(f"Tipo de pago: {tp}")
        print(f"Monto de descuento {porc1}%: ${desc1:,.2f}")
        print(f"Total a pagar: ${montoP - desc1:,.2f}")
    elif 200000 < montoP <= 500000:
        print("\nDatos de Factura:\n")
        print(f"Monto a pagar: ${montoP:,.2f}")
        print(f"Tipo de pago: {tp}")
        print(f"Monto de descuento {porc2}%: ${desc2:,.2f}")
        print(f"Total a pagar: ${montoP - desc2:,.2f}")
    elif montoP > 500000:
        print("\nDatos de Factura:\n")
        print(f"Monto a pagar: ${montoP:,.2f}")
        print(f"Tipo de pago: {tp}")
        print(f"Monto de descuento {porc3}%: ${desc3:,.2f}")
        print(f"Total a pagar: ${montoP - desc3:,.2f}")
    else:
        print("\nValor ingresado incorrecto")
elif tp == "TD":
    tp = "Tarjeta Débito (TD)"
    montoP = float(input("Digite el monto a pagar: "))
    desc1 = montoP * 0.10
    desc2 = montoP * 0.20
    desc3 = montoP * 0.30
    porc1 = 10
    porc2 = 20
    porc3 = 30
    if 0 < montoP <= 200000:
        print("\nDatos de Factura:\n")
        print(f"Monto a pagar: ${montoP:,.2f}")
        print(f"Tipo de pago: {tp}")
        print(f"Monto de descuento {porc1}%: ${desc1:,.2f}")
        print(f"Total a pagar: ${montoP - desc1:,.2f}")
    elif 200000 < montoP <= 500000:
        print("\nDatos de Factura:\n")
        print(f"Monto a pagar: ${montoP:,.2f}")
        print(f"Tipo de pago: {tp}")
        print(f"Monto de descuento {porc2}%: ${desc2:,.2f}")
        print(f"Total a pagar: ${montoP - desc2:,.2f}")
    elif montoP > 500000:
        print("\nDatos de Factura:\n")
        print(f"Monto a pagar: ${montoP:,.2f}")
        print(f"Tipo de pago: {tp}")
        print(f"Monto de descuento {porc3}%: ${desc3:,.2f}")
        print(f"Total a pagar: ${montoP - desc3:,.2f}")
    else:
        print("\nValor ingresado incorrecto")
elif tp == "TC":
    tp = "Tarjeta de Crédito (TC)"
    montoP = float(input("Digite el monto a pagar: "))
    desc1 = montoP * 0.05
    desc2 = montoP * 0.10
    desc3 = montoP * 0.18
    porc1 = 5
    porc2 = 10
    porc3 = 18
    if 0 < montoP <= 200000:
        print("\nDatos de Factura:\n")
        print(f"Monto a pagar: ${montoP:,.2f}")
        print(f"Tipo de pago: {tp}")
        print(f"Monto de descuento {porc1}%: ${desc1:,.2f}")
        print(f"Total a pagar: ${montoP - desc1:,.2f}")
    elif 200000 < montoP <= 500000:
        print("\nDatos de Factura:\n")
        print(f"Monto a pagar: ${montoP:,.2f}")
        print(f"Tipo de pago: {tp}")
        print(f"Monto de descuento {porc2}%: ${desc2:,.2f}")
        print(f"Total a pagar: ${montoP - desc2:,.2f}")
    elif montoP > 500000:
        print("\nDatos de Factura:\n")
        print(f"Monto a pagar: ${montoP:,.2f}")
        print(f"Tipo de pago: {tp}")
        print(f"Monto de descuento {porc3}%: ${desc3:,.2f}")
        print(f"Total a pagar: ${montoP - desc3:,.2f}")
    else:
        print("\nValor ingresado incorrecto")
else:
    print("Opción inválida")