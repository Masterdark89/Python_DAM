"""Programa que lea una secuencia de números no nulos hasta que se introduzca un 0, y luego
muestre si ha leído algún número negativo, cuantos positivos y cuantos negativos"""

contador_neg = 0
contador_pos = 0

while num != 0:
    num = int(input("Introduzca números no nulos:"))
        
    if num < 0:
        contador_neg += 1
    if num > 0:
        contador_pos += 1

if contador_neg != 0:
    print("Hay números negativos")       
    print("Hay", contador_pos," números positivos y ", contador_neg ," números negativos.")
else:
    print("Hay", contador_pos," números positivos")