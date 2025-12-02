"""Leer una cadena y contar cuántas vocales contiene."""

cadena = input("Introduce una cadena: ")
cadena.lower()
contador = 0

for i in range(len(cadena)):

    if cadena[i] == "a":
        contador += 1
    elif cadena[i] == "e":
        contador += 1
    elif cadena[i] == "i":
        contador += 1
    elif cadena[i] == "o":
        contador += 1
    elif cadena[i] == "u":
        contador += 1

if contador == 0:
    print("No hay vocales")
else:
    print("Hay ", contador, " vocales")
