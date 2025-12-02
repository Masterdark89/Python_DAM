"""Realizar un algoritmo que muestre la tabla de multiplicar de un número introducido por
teclado"""

num = int(input("¿De que número quieres la tabla? "))

for i in range(11):
    resultado = num * i
    print(num, " * ", i, " = ", resultado)
