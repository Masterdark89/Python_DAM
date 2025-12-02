"""Escribir un programa que lea un año indicar si es bisiesto. Nota: un año es bisiesto si es un
número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por
400."""

año = int(input("Introduce un año: "))

if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            print("Es bisiesto")
        else:
            print("No es bisiesto")
    else:
        print("Es bisiesto")
else:
    print("No es bisiesto")
