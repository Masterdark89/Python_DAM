"""Leer dos cadenas y concatenarlas manualmente sin usar el
operador + en una sola operación (concatenar carácter a carácter con un ciclo)."""

cadena1 = input("Introduce la primera cadena: ")
cadena2 = input("Introduce la segunda cadena: ")

for i in range(len(cadena2)):
    cadena1 += cadena2[i]

print(cadena1)
