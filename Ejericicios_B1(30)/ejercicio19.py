"""Dibuja un ordinograma de un programa que lea tres números y nos diga cual es mayor, cual
menor y cuales son iguales"""

numero_1 = int(input("Introduce un número: "))
numero_2 = int(input("Introduce otro número: "))
numero_3 = int(input("Introduce otro número: "))

if numero_1 == numero_2 == numero_3:
    print("Todos son iguales")

elif numero_1 > numero_2 == numero_3:
    print(numero_1, ">", numero_2, "=", numero_3)

elif numero_1 < numero_2 == numero_3:
    print(numero_1, "<", numero_2, "=", numero_3)

elif numero_1 == numero_2 > numero_3:
    print(numero_1, "=", numero_2, ">", numero_3)

elif numero_1 == numero_2 < numero_3:
    print(numero_1, "=", numero_2, "<", numero_3)

elif numero_1 == numero_3 < numero_2:
    print(numero_1, "=", numero_3, "<", numero_3)

elif numero_1 == numero_3 > numero_2:
    print(numero_1, "=", numero_2, ">", numero_3)
