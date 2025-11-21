"""Crea una aplicación que dibuje una escalera de números, siendo cada línea un número.
Nosotros le pasamos la altura por teclado."""

try:
    altura = int(input("Introduce la altura:"))
    if altura < 0:
        raise ValueError
except ValueError:
    print("Error")

else:
    for i in range(1, altura+1):
        for j in range(1, i+1):
            print(i,end="")
        print()