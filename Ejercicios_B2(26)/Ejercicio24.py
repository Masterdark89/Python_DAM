"""Tiendas Don Pepe desea un programa para ingresar por teclado el monto de compra y el día
de la semana; si el día es martes o jueves, se realizará un descuento del 15% por la compra.
Visualizar el descuento y el total a pagar por la compra.   """

precio = float(input("Introduce el precio de la compra: "))

opcion = input("¿Que dia de la semana es?")

match opcion.lower():
    case "lunes":
        print("El precio a pagar por la compra será de ", precio, "euros")

    case "martes":
        descuento = precio * 15 / 100
        precio = precio - descuento
        print("El descuento es de", descuento,
              "euros, por lo que se pagará por la compra será de ", precio, "euros")

    case "miercoles":
        print("El precio a pagar por la compra será de ", precio, "euros")

    case "jueves":
        descuento = precio * 15 / 100
        precio = precio - descuento
        print("El descuento es de", descuento,
              "euros, por lo que se pagará por la compra será de ", precio, "euros")

    case "viernes":
        print("El precio a pagar por la compra será de ", precio, "euros")

    case "sabado":
        print("El precio a pagar por la compra será de ", precio, "euros")

    case "domingo":
        print("El precio a pagar por la compra será de ", precio, "euros")

    case _:
        print("Dia no existente")
