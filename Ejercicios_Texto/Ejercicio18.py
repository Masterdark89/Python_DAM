"""Leer una cadena y construir una nueva cadena dejando sólo los caracteres que
son consonantes (sin listas, usando condiciones y concatenación)."""

cadena = input("Introduce una cadena: ")
nuevacadena = ""

for i in range(len(cadena)):

    if cadena[i] == "a":
        aux = 0
    elif cadena[i] == "e":
        aux = 0
    elif cadena[i] == "i":
        aux = 0
    elif cadena[i] == "o":
        aux = 0
    elif cadena[i] == "u":
        aux = 0
    elif cadena[i] == " ":
        aux = 0
    else:
        nuevacadena += cadena[i]

print(nuevacadena)
