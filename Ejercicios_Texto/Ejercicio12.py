"""Leer una cadena y construir una nueva cadena con los caracteres en orden inverso."""

cadena = input("Introduce una cadena: ")
cadenareves = ""

for i in range(len(cadena)-1, -1, -1):
    cadenareves += cadena[i]

print(cadenareves)
