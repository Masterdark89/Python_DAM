"""Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un
dado de seis caras y muestre por pantalla el número en letras (dato cadena) de la cara opuesta
al resultado obtenido.
Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el
mensaje: "ERROR: número incorrecto."."""

dado = int(input("Introduce la cara del dado:"))

match dado:
    case 1:
        print("6")
    case 2:
        print("5")
    case 3:
        print("4")
    case 4:
        print("3")
    case 5:
        print("2")
    case 6:
        print("1")
    case _:
        print("ERROR: número incorrecto.")
