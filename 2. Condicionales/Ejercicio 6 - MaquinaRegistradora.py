"""
    Simular una máquina registradora, la cual al ingresar una cantidad de dinero a pagar,
    deberá entregar el cambio; unicamente en billetes de 20.000, 10.000, 5.000, 2.000 y
    monedas de 50, 100, 200, 500 y 1.000 respectivamente. 
"""
c20000 = c10000 = c5000 = c2000 = c1000 = c500 = c200 = c100 = c50 = 0

vf = float(input("Digite el monto de la factura: "))
vp = float(input("Digite el monto a pagar: "))

dev = vp - vf

print()

if vp < vf:
    print("Dinero insuficiente para pagar la factura")
else:
    if 0 < dev < 50:
        print(f"Monto a pagar: ${vf:,.2f}")
        print(f"Monto pagado: ${vp:,.2f}")
        print("Devolución: $0.00")
    else:
        c20000 = dev // 20000
        aux = dev - 20000 * c20000
        c10000 = aux // 10000
        aux1 = aux - 10000 * c10000
        c5000 = aux1 // 5000
        aux2 = aux1 - 5000 * c5000
        c2000 = aux2 // 2000
        aux3 = aux2 - 2000 * c2000
        c1000 = aux3 // 1000
        aux4 = aux3 - 1000 * c1000
        c500 = aux4 // 500
        aux5 = aux4 - 500 * c500
        c200 = aux5 // 200
        aux6 = aux5 - 200 * c200
        c100 = aux6 // 100
        aux7 = aux6 - 100 * c100
        c50 = aux7 // 50
        print("\nDatos de la Factura:\n")
        print(f"Monto de la factura: ${vf:,.2f}")
        print(f"Monto pagado: ${vp:,.2f}")
        print(f"Monto devuelto: ${dev:,.2f}")
        print("\nDistribución de billetes y monedas devuelto:\n")
        print(f"Billetes de $20,000: {c20000:.0f}")
        print(f"Billetes de $10,000: {c10000:.0f}")
        print(f"Billetes de $5,000: {c5000:.0f}")
        print(f"Monedas de $2,000: {c2000:.0f}")
        print(f"Monedas de $1,000: {c1000:.0f}")
        print(f"Monedas de $500: {c500:.0f}")
        print(f"Monedas de $200: {c200:.0f}")
        print(f"Monedas de $100: {c100:.0f}")
        print(f"Monedas de $50: {c50:.0f}")