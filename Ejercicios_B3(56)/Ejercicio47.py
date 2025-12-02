"""Escribe un programa que diga si un número introducido por teclado es o no primo. Un
número primo es aquel que sólo es divisible entre él mismo y la unidad. Nota: Es suficiente
probar hasta la raíz cuadrada del número para ver si es divisible por algún otro número"""
import math

num = int(input("Introduce un número: "))
contador = 0

if num <= 1:
    print("No es primo")
else:
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            contador += 1

            if contador > 1 and i != 1:
                break

    if contador == 1:
        print("Es primo")
    else:
        print("No es primo")
