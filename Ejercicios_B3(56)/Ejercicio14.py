"""Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número
invertido"""

num = int(input("Introduce un número: "))
num_reves = 0

if num < 10:
    print("El número al revés es", num)
else:
    while num > 0:
        resto = num % 10
        num = num // 10
        num_reves = num_reves * 10 + resto

    print("El número al revés es", num_reves)
