"""Contar cuántas veces aparece un carácter dado en una cadena usando for y un contador."""

cadena = input("Introduce una cadena: ")
contador = 0
buscar = input("¿Que caracter quieres buscar?")

for i in range(len(cadena)):
    if cadena[i] == buscar:
        contador += 1

print("El caracter aparece ", contador, "veces")
