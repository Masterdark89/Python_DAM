"""Una farmacia desea un programa para ingresar el valor de compra y calcular lo siguiente: si
el pago se efectúa al “contado”, calcular un descuento del 5%; pero si el pago es con “tarjeta”
se incrementa un recargo del 3% al valor de compra. Calcular y visualizar el descuento o recargo
según sea el caso y el total a pagar de la compra."""

precio = float(input("Introduce el precio de la compra: "))

print("¿Va a ser en efectivo? (S/N)")
opcion = input()

if opcion == "S":
    precio = precio - (precio * 5 / 100)
else:
    precio = precio + (precio * 3 / 100)

print("El precio a pagar es: ", precio)
