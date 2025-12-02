"""Construir una nueva cadena con todos los caracteres de la cadena original, pero duplicando cada vocal."""

cadena = input("Introduce una cadena: ")
nuevacadena = ""

for i in range(len(cadena)):

    if cadena[i] == "a":
        nuevacadena += cadena[i] * 2
    elif cadena[i] == "e":
        nuevacadena += cadena[i] * 2
    elif cadena[i] == "i":
        nuevacadena += cadena[i] * 2
    elif cadena[i] == "o":
        nuevacadena += cadena[i] * 2
    elif cadena[i] == "u":
        nuevacadena += cadena[i] * 2
    else:
        nuevacadena += cadena[i]

print(nuevacadena)
