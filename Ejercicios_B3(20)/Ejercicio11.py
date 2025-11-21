"""Crea una aplicación que dibuje una escalera de asteriscos. Nosotros le pasamos la altura de
la escalera por teclado. Este es un ejemplo si insertaras un 5 de altura:"""

try:
    altura = int(input("Introduce la altura:"))
    if altura < 0:
        raise ValueError
except ValueError:
    print("Error")

else:
    for i in range(1, altura+1):
        for j in range(1, i+1):
            print("*",end="")
        print()