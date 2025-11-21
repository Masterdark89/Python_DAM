"""Crea una aplicación que dibuje una escalera de números, siendo cada línea números
empezando en uno y acabando en el numero de la línea. Este es un ejemplo, si introducimos un
5 como altura:"""

try:
    altura = int(input("Introduce la altura:"))
    if altura < 0:
        raise ValueError
except ValueError:
    print("Error")

else:
    for i in range(1, altura+1):
        for j in range(1, i+1):
            print(j,end="")
        print()