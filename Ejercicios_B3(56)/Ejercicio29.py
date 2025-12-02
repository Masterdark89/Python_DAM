"""Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los
lados de un triángulo. El programa debe determinar qué tipo de triángulo es, teniendo en
cuenta:
• Si se cumple Pitágoras entonces es triángulo rectángulo
• Si sólo dos lados del triángulo son iguales entonces es isósceles.
• Si los 3 lados son iguales entonces es equilátero.
• Si no se cumple ninguna de las condiciones anteriores, es escaleno."""

A = float(input("Introduce A: "))
B = float(input("Introduce B: "))
C = float(input("Introduce C: "))

if A * A + B * B == C * C:
    if A == B == C:
        print("Es un triángulo rectángulo equilátero")

    elif A == B or A == B or B == C:
        print("Es un triángulo rectángulo isósceles")

    else:
        print("Es un triángulo rectángulo escaleno")

else:
    if A == B == C:
        print("Es un triángulo equilátero")

    elif A == B or A == B or B == C:
        print("Es un triángulo isósceles")

    else:
        print("Es un triángulo escaleno")
