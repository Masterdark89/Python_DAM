"""Crea una aplicación que dibuje una pirámide de asteriscos. Nosotros le pasamos la altura
de la pirámide por teclado. Este es un ejemplo, si introducimos 5 de altura"""

try:
    altura = int(input("Introduce la altura: "))
    if altura <= 0:
        raise ValueError
except ValueError:
    print("Error: Debes introducir un número entero positivo")
else:
    for i in range(1, altura + 1):
        espacios = altura - i
        asteriscos = 2 * i - 1
        
        print(" " * espacios, end="")
        print("*" * asteriscos)