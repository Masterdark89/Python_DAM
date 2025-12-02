"""Calcular el perímetro y área de un rectángulo dada su base y su altura"""

base = int(input("¿Cual es la base del triangulo?"))
altura = int(input("¿Cual es la altura del triangulo?"))

perimetro = 2 * (base + altura)
area = base * altura

print(f"El perímetro del rectángulo es: {perimetro}")
print(f"El área del rectángulo es: {area}")
