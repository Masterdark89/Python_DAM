"""Dibuja un ordinograma de un programa que suma independientemente los pares y los
impares de los números comprendidos entre 100 y 200, y luego muestre por pantalla ambas
sumas."""

suma_par = 0
suma_impar = 0
i = 100

for i in range(200):
    if i % 2 == 0:
        suma_par += i
    else:
        suma_impar += i

print("La suma de los pares es: ", suma_par)
print("La suma de los impares es: ", suma_impar)
