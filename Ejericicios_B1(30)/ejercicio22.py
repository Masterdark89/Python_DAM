"""Dibuja un ordinograma de un programa que lea 100 números no nulos y luego muestre un
mensaje indicando cuántos son positivos y cuantos negativos."""

c_positivo = 0
c_negativo = 0

for i in range(100):

    num = int(input("Introduce un número: "))

    while (num == 0):
        print("Error, vuelve a intentarlo")
        num = int(input())

    if num < 0:
        c_negativo += 1
    else:
        c_positivo += 1

print("Se han encontrado:", c_positivo,
      "números positivos y ", c_negativo, "números negativos")
