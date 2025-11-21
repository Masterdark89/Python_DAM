"""Escriba un programa que lea dos números y nos diga cual es mayor o si son iguales."""

numero_1 = int(input("Introduce un número: "))
numero_2 = int(input("Introduce otro número: "))

if numero_1 == numero_2:
    print("Ambos son iguales")
elif numero_1 > numero_2:
    print(numero_1, " es el mayor")
else:
    print(numero_2, " es el mayor")
