"""Dibuja un ordinograma de un programa que lea dos números y lo visualiza en orden
ascendente"""

numero_1 = int(input("Introduce un número: "))
numero_2 = int(input("Introduce otro número: "))

if numero_1 > numero_2:
    print("El orden es: ", numero_2, ",", numero_1)
else:
    print("El orden es: ", numero_1, ",", numero_2)
