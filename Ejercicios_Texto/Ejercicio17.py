"""Leer una cadena y crear una nueva donde sólo aparezcan los caracteres que se repiten más de una vez."""

cadena = input("Introduce una cadena: ")
nuevacadena = ""
contador = 0

for i in range(len(cadena)):
    for j in range(len(cadena)):
        if cadena[i] == cadena[j]:
            contador += 1
    if contador > 1:
        nuevacadena += cadena[i]
    contador = 0

print(nuevacadena)
