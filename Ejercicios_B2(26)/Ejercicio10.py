"""Escriba un programa que lea dos números, calcule y muestre el valor de sus suma, resta,
producto y división (Ten en cuenta la división por cero)"""

numero_1 = float(input("Introduce un número: "))
numero_2 = float(input("Introduce otro número: "))

suma = numero_1 + numero_2
resta = numero_1 - numero_2
multi = numero_1 * numero_2

if numero_2 == 0:
    print("No se puede dividir por 0")
    print("Suma: ", suma, "Resta: ", resta, "Multiplicacion", multi)
else:
    division = numero_1 / numero_2
    print("Suma: ", suma, "Resta: ", resta,
          "Multiplicacion:", multi, "Division:", division)
