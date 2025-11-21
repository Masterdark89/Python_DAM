"""Programa que lea 100 números no nulos y luego muestre un mensaje indicando cuántos
son positivos y cuantos negativos"""

contador_neg = 0
contador_pos = 0

for i in range(100):
    num = int(input("Introduzca números no nulos:"))
    while num == 0:
        num = int(input("No puede ser nulo:"))
        
    if num < 0:
        contador_neg += 1
    if num > 0:
        contador_pos += 1
        
print("Hay", contador_pos," números positivos y ", contador_neg ," números negativos.")