"""Escriba un programa que dado el precio de un artículo y el precio de venta real nos muestre
el porcentaje de descuento realizado."""

print("Dame el precio del articulo: ")
precio = input()
precio = float(precio)

print("Dame el precio real: ")
precio_real = input()
precio_real = float(precio_real)

descuento = ((precio_real - precio) / precio_real) * 100

print("El descuento ha sido del: ", descuento, "%")
