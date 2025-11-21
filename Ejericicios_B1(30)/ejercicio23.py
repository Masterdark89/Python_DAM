"""Dibuja un ordinograma de un programa que lea una secuencia de números no nulos hasta
que se introduzca un 0, y luego muestre si ha leído algún número negativo, cuantos positivos y
cuantos negativos."""

c_positivo = 0
c_negativo = 0

for i in range(100):

    num = int(input("Introduce un número: "))

    if (num == 0):
        print("Fin del programa")
        print("Se han encontrado:", c_positivo,
              "números positivos y ", c_negativo, "números negativos")
        break

    else:
        if num < 0:
            c_negativo += 1
        else:
            c_positivo += 1
