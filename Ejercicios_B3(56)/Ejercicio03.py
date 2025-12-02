"""Dados los catetos de un triángulo rectángulo, calcular su hipotenusa"""
import math

cateto1 = float(input("Introduce un cateto:"))
cateto2 = float(input("Introduce el otro cateto:"))

hipotenusa = math.sqrt((cateto1*cateto1 + cateto2*cateto2))

print("La hipotenusa del triangulo es:", hipotenusa)
