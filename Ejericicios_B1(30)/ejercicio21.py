"""Dibuja un ordinograma de un programa que lea 100 números no nulos y luego muestre un
mensaje de si ha leído número negativo o no."""

contador = 0

for i in range(100):

    num = int(input("Introduce un número: "))

    while (num == 0):
        print("Error, vuelve a intentarlo")
        num = int(input())

    if num < 0:
        contador += 1

if (contador != 0):
    print("Se han encontrado números negativos")
else:
    print("No se han encontrado números negativos")
