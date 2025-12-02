"""Escribe un programa que dados dos números, uno real (base) y un entero positivo
(exponente), saque por pantalla el resultado de la potencia. No se puede utilizar el operador de
potencia"""

base = float(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))
total = 1

while exponente < 0:
    print("Error, no puede ser negativo")
    exponente = int(input("Introduce el exponente: "))

for i in range(exponente):
    total = total * base

print("El resultado es", total)
