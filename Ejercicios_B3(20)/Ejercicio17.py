"""Programa que suma independientemente los pares y los impares de los números
comprendidos entre 100 y 200, y luego muestra por pantalla ambas sumas."""

sum_par = 0
sum_impar = 0

for i in range(100, 201):
    
    if i % 2 == 0:
        suma_par += i
    else:
        sum_impar *= i

print("La suma de los pares es",sum_par,"y la suma de los impares es", sum_impar) 
