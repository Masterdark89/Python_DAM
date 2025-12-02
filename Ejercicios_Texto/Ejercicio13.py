"""Leer una cadena y eliminar todos los espacios, construyendo una cadena continua."""

cadena = input("Introduce una cadena: ")
nuevacadena = ""

for i in range(len(cadena)):
    if cadena[i] != " ":
        nuevacadena += cadena[i]

print(nuevacadena)
