"""Leer una cadena y contar cuántos caracteres son letras mayúsculas."""

cadena = input("Introduce una cadena: ")

contador = 0

for i in range(len(cadena)):

    if cadena[i] != " ":
        if cadena[i] == cadena[i].upper():
            contador += 1


print("Hay", contador, "mayúsculas")
