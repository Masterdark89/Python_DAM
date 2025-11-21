"""Dibuja un ordinograma de un programa que lea una secuencia de notas (con valores que
van de 0 a 10) que termina con el valor -1 y nos dice si hubo o no alguna nota con valor 10."""

contador = 0
seguir = True

while seguir:

    nota = int(input("Introduce las notas: (-1 para salir)"))

    if nota == -1:
        if contador != 0:
            print("Hubo algun 10")
        else:
            print("No hubo 10")

        break

    while nota < 0 or nota > 10:
        print("Nota erronea, vuelva a intentarlo:")
        nota = int(input())

    if nota == 10:
        contador += 1
