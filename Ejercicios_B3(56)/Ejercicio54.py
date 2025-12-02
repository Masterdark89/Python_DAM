"""Hacer un programa que muestre un cronometro, indicando las horas, minutos y segundos"""

n = int("¿Cuanto quieres esperar? (en segundos)")
print("Iniciando cronometro:")
contador = 0
hora = 0
minutos = 0
segundos = 0
print(hora, minutos, segundos)


while contador != n:

    segundos += 1
    if segundos == 60:
        segundos = 0
        minutos += 1
    if minutos == 60:
        minutos = 0
        hora += 1

    contador += 1
    print(hora, minutos, segundos)
