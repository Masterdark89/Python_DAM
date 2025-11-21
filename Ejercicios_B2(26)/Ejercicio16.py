"""Escriba un programa que pida un número entre 0 y 99999, y que diga cuantas cifras tiene"""

num = int(input("Introduce un numero: "))
contador = 1

while num < 0 or num > 99999:
    print("Numero no valido")
    num = int(input("Introduce un numero: "))

while num > 10:
    num = num / 10
    contador = contador+1

print("El número tiene ", contador, "cifras")
