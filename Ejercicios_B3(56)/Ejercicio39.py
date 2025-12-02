"""Crea una aplicación que permita adivinar un número. La aplicación genera un número
aleatorio del 1 al 100. A continuación, va pidiendo números y va respondiendo si el número a
adivinar es mayor o menor que el introducido, además de los intentos que te quedan (tienes 10
intentos para acertarlo). El programa termina cuando se acierta el número (además te dice en
cuantos intentos lo has acertado), si se llega al límite de intentos te muestra el número que
había generado"""

import random

num = random.randint(1, 100)
intentos = 10

while intentos != 0:
    num_posible = int(input("¿Que número crees que es?"))

    if num == num_posible:
        print("Acertaste")
        break

    if num > num_posible:
        print("Es mayor")

    if num < num_posible:
        print("Es menor")

    intentos -= 1
    print("Intentos restantes:", intentos)
    print(" ")
