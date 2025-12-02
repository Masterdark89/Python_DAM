"""Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica.
Python3 no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿Cómo se
puede calcular?"""

numero = float(input("Introduce un número: "))

raiz_cuadrada = numero ** 0.5

raiz_cubica = numero ** (1/3)

print("Raíz cuadrada:", raiz_cuadrada)
print("Raíz cúbica:", raiz_cubica)
