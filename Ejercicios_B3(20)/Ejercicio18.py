"""Programa que calcule el valor A elevado a B (A^B) sin hacer uso del operador de potencia
(^), siendo A y B valores introducidos por teclado, y luego muestre el resultado por pantalla.  """

num = int(input("Introduce un número: "))
elevado = int(input("¿A cuanto lo vas a elevar?"))
total = 1

for i in range(1, elevado):
    total *= num
    
print("El resultado es", total)
