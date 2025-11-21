"""Programa que lea 100 números no nulos y luego muestre un mensaje de si ha leído algún
número negativo o no"""
contador = 0

for i in range(100):
    num = int(input("Introduzca números no nulos:"))
    while num == 0:
        num = int(input("No puede ser nulo:"))
        
    if num < 0:
        contador += 1
        
if contador != 0:
    print("Hay números negativos")
else:
    print("No hay negativos")