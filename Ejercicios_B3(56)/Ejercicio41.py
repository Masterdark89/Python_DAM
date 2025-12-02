"""Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a
introducir). El programa debe informar de cuantos números introducidos son mayores que 0,
menores que 0 e iguales a 0"""

n = int(input("¿Cuantos numeros vas a introducir?"))
mayor = 0
menor = 0
igual = 0

for i in range(n):
    num = int(input("Introduce un número:"))

    if num == 0:
        igual += 1
    if num > 0:
        mayor += 1
    if num < 0:
        menor += 1

if igual != 0:
    print("Hay", igual, "números iguales a 0")

if mayor != 0:
    print("Hay", mayor, "números mayores a 0")

if menor != 0:
    print("Hay", menor, "números menores a 0")
