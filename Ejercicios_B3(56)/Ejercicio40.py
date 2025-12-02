"""Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la
media de todos los números introducidos"""

num = 1
suma = 0
veces = 0

while num != 0:
    num = int(input("Introduce un número"))
    suma += num
    veces += 1

media = suma / veces

print("La suma es", suma, " y la media es", media)
