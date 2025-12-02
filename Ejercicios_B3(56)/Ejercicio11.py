"""Pide al usuario dos números y muestra la "distancia" entre ellos (el valor absoluto de su
diferencia, de modo que el resultado sea siempre positivo)."""

num1 = int(input("Introduce un número:"))
num2 = int(input("Introduce otro número:"))

distancia = num1 - num2

if (distancia < 0):
    distancia *= -1

print("La distancia es", distancia)
