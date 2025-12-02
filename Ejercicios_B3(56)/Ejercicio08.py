"""Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas, el
vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas
que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y
comisiones"""

paga = float(input("¿Cual es el sueldo base?"))

venta_1 = float(input("Introduzca la primera venta:"))
venta_2 = float(input("Introduzca la segunda venta:"))
venta_3 = float(input("Introduzca la tercera venta:"))

venta_1 = venta_1 * 10 / 100
print("El total a recibir por la primera comisión es: ", venta_1, " euros")
venta_2 = venta_2 * 10 / 100
print("El total a recibir por la segunda comisión es: ", venta_2, " euros")
venta_3 = venta_3 * 10 / 100
print("El total a recibir por la tercera comisión es: ", venta_3, " euros")

paga = paga + venta_1 + venta_2 + venta_3

print("El total a recibir es: ", paga, " euros")
