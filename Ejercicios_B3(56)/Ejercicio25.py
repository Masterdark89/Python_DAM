"""Programa que lea una cadena por teclado y compruebe si es una letra mayúscula"""

cadena = input("Escribe algo: ")
contador = 0

for i in range(len(cadena)):
    if cadena[i] == cadena[i].upper():
        contador += 1

if contador != 0:
    print("Hay mayusculas")
else:
    print("No hay mayusculas")
