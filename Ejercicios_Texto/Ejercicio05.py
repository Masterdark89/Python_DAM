"""Verificar si un carácter específico está en la cadena con un ciclo y comparaciones."""

cadena = input("Introduce una cadena: ")
cadena2 = input("Introduce la segunda cadena: ")
igual = True

if len(cadena) > len(cadena2):
    ciclo = len(cadena)
else:
    ciclo = len(cadena2)

for i in range(ciclo):
    if cadena[i] != cadena2[i]:
        igual = False

if igual:
    print("Ambas cadenas son iguales")
else:
    print("Ambas cadenas son diferentes")
