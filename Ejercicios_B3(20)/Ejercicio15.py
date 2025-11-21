"""Crea una aplicación que dibuje una pirámide invertida de asteriscos. Nosotros le pasamos
la altura de la pirámide por teclado. Este es un ejemplo"""

try:
    altura = int(input("Introduce la altura: "))
    if altura <= 0:
        raise ValueError
except ValueError:
    print("Error: Debes introducir un número entero positivo")
else:
    for i in range(altura, 0, -1):

        print(' ' * (altura - i), end='')

        print('*' * (2 * i - 1))
