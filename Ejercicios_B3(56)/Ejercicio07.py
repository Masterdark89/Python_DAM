"""Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas
horas y minutos corresponde"""

minutos = int(input("Introduce la cantidad en minutos: "))
horas = 0

while minutos >= 60:
    minutos -= 60
    horas += 1

print("Son", horas, "horas y ", minutos, "minutos.")
