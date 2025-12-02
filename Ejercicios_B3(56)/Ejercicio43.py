"""Escribir un programa que imprima todos los números pares entre dos números que se le
pidan al usuario"""

n1 = int(input("Introduce un numero: "))
n2 = int(input("Introduce otro numero: "))

if n1 > n2:
    aux = n2
    n2 = n1
    n1 = aux

for i in range(n1, n2):
    if i % 2 == 0:
        print(i)
