"""Dibuja un ordinograma de un programa que lea un número positivo N y calcule y visualice
su factura N! siendo el factorial:
0!=1
1!=1
2!=2*1
…
N!= N*(N-1)*(N-2)*…*1"""


num = int(input("Introduce un número: "))
resultado = 1

if num == 1 or num == 0:
    print("El factorial es  1")
else:
    for i in range(num):
        resultado = (i+1) * resultado
    print("El factorial es: ", resultado)
