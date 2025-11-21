"""Dibuja un ordinograma de un programa que calcule y escriba la suma y el producto de los
10 primeros números naturales."""

suma = 0
multi = 1

for i in range(10):
    suma = suma + i
    multi = multi * i

print("La suma es", suma, " y la multiplicacion es ", multi)
