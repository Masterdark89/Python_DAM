"""Dibuja un ordinograma de un programa que muestre los números pares comprendidos
entre el 1 y el 200. Esta vez utiliza un contador sumando de 1 en 1."""

n = 1

for i in range(200):
    if (n % 2 != 0):
        print(n)
    n += 1
