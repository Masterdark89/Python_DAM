"""Programa que calcula y escribe la suma y el producto de los 10 primeros números naturales"""

suma = 0
multi = 1

for i in range (1,10):
    suma += i
    multi *= i

print("La suma es",suma, "y la multiplicacion es",multi)