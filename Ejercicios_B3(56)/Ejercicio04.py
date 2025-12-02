"""Dados dos números, mostrar la suma, resta, división y multiplicación de ambos"""

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el primer número: "))

suma = num1 + num2
resta = num1 - num2
multi = num1 * num2

if num2 == 0:
    print("La suma es", suma)
    print("La resta es", resta)
    print("La multiplicacion es", multi)
    print("No se puede dividir entre 0")
else:
    division = num1 / num2
    print("La suma es", suma)
    print("La resta es", resta)
    print("La multiplicacion es", multi)
    print("La division es", division)
