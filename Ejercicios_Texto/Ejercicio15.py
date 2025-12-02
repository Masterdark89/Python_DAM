"""Dada una cadena, construir una nueva cadena donde cada vocal se reemplaza por un asterisco '*'."""

cadena = input("Introduce una cadena: ")
nuevacadena = ""

for i in range(len(cadena)):

    if cadena[i] == "a":
        nuevacadena += "*"
    elif cadena[i] == "e":
        nuevacadena += "*"
    elif cadena[i] == "i":
        nuevacadena += "*"
    elif cadena[i] == "o":
        nuevacadena += "*"
    elif cadena[i] == "u":
        nuevacadena += "*"
    else:
        nuevacadena += cadena[i]

print(nuevacadena)
