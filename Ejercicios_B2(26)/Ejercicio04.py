"""Escriba un programa que lea dos números, calcule y muestre el valor de sus suma, resta,
producto y división."""

print("Introduce el primer numero:")
numero_1 = input()
numero_1 = int(numero_1)

print("Introduce el segundo numero:")
numero_2 = input()
numero_2 = int(numero_2)

suma = numero_1 + numero_2
resta = numero_1 - numero_2
multiplicacion = numero_1 * numero_2
division = numero_1 / numero_2

print("Suma:", suma, ", Resta:", resta, ", Multiplicacion:",
      multiplicacion, ", Division:", division)
