"""Programa que lee una secuencia de notas (con valores que van de 0 a 10) que termina con
el valor -1 y nos dice si hubo o no alguna nota con valor 10"""
contador = 0

while notas != -1:
    notas = int(input("Introduce las notas: "))

    while notas > 10 or notas < -1:
        print("Error: Deben estar comprendidas entre 0 y 10")
        notas = int(input("Introduce notas: "))

    if notas == 10:
        contador += 1

if contador != 0:
    print("Hubo algun 10")
else:
    print("No hay ningun 10")
