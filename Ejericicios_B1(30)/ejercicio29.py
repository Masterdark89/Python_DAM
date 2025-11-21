"""Dibuja un ordinograma de un programa donde el usuario “piensa” un número del 1 al 100
y el ordenador intenta adivinarlo. Es decir, el ordenador irá proponiendo números una y otra
vez hasta adivinarlo (El usuario deberá indicarlo al ordenador si es mayor o menor o igual al
número pensado)."""

import random

num = random.randint(1, 100)
seguir = True

while seguir:
    respuesta = input(f"¿Tu número es mayor, menor o igual que {num}? ")

    match respuesta.lower():
        case "igual":
            print("¡He acertado!")
            seguir = False
        case "menor":
            num -= 1
        case "mayor":
            num += 1
        case _:
            print("Por favor, responde con 'mayor', 'menor' o 'igual'")
