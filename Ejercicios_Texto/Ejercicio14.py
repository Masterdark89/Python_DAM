"""Leer una cadena y contar cuántos caracteres numéricos ('0' a '9') contiene."""

cadena = input("Introduce una cadena: ")
contador = 0

for i in range(len(cadena)):

    if cadena[i] == "0":
        contador += 1
    elif cadena[i] == "1":
        contador += 1
    elif cadena[i] == "2":
        contador += 1
    elif cadena[i] == "3":
        contador += 1
    elif cadena[i] == "4":
        contador += 1
    elif cadena[i] == "5":
        contador += 1
    elif cadena[i] == "6":
        contador += 1
    elif cadena[i] == "7":
        contador += 1
    elif cadena[i] == "8":
        contador += 1
    elif cadena[i] == "9":
        contador += 1

print("Hay", contador, "caracteres numericos")
