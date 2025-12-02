"""Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea
saber cuánto deberá pagar finalmente por su compra."""

pagar = float(input("Introduce el precio: "))

descuento = pagar * 15 / 100

pagar = pagar - descuento

print("El precio tras el descuento es de", pagar, "euros.")
