"""Programa que dada una cantidad de euros que el usuario introduce por teclado (múltiplo de
5 €) mostrará los billetes de cada tipo que serán necesarios para alcanzar dicha cantidad
(utilizando billetes de 500, 200, 100, 50, 20, 10 y 5). Hay que indicar el mínimo de billetes posible.
Por ejemplo, si el usuario introduce 145 el programa indicará que será necesario 1 billete de 100
€, 2 billetes de 20 € y 1 billete de 5 € (no será válido por ejemplo 29 billetes de 5, que aunque
sume 145 € no es el mínimo número de billetes posible)"""

billete_500 = 0
billete_200 = 0
billete_100 = 0
billete_50 = 0
billete_20 = 0
billete_10 = 0
billete_5 = 0

dinero = int(input("¿Cuánto dinero tienes? "))

while dinero % 5 != 0:
    print("La cantidad debe ser múltiplo de 5")
    dinero = int(input("¿Cuánto dinero tienes?"))

while dinero >= 500:
    dinero -= 500
    billete_500 += 1

while dinero >= 200:
    dinero -= 200
    billete_200 += 1

while dinero >= 100:
    dinero -= 100
    billete_100 += 1

while dinero >= 50:
    dinero -= 50
    billete_50 += 1

while dinero >= 20:
    dinero -= 20
    billete_20 += 1

while dinero >= 10:
    dinero -= 10
    billete_10 += 1

while dinero >= 5:
    dinero -= 5
    billete_5 += 1

print("Serán necesarios:")
if billete_500 > 0:
    print(f"{billete_500} billete(s) de 500€")
if billete_200 > 0:
    print(f"{billete_200} billete(s) de 200€")
if billete_100 > 0:
    print(f"{billete_100} billete(s) de 100€")
if billete_50 > 0:
    print(f"{billete_50} billete(s) de 50€")
if billete_20 > 0:
    print(f"{billete_20} billete(s) de 20€")
if billete_10 > 0:
    print(f"{billete_10} billete(s) de 10€")
if billete_5 > 0:
    print(f"{billete_5} billete(s) de 5€")
