# Ejercicio 1: Piramide de asteriscos inclinada hacia la izquierda

try:
    altura = int(input("Introduce la altura: "))
    if altura <= 0:
        raise ValueError
except ValueError:
    print("Error: No puede ser negativo")
else:
    for i in range(1, altura + 1):
        espacios = altura - i
        
        print(" " * espacios, end="")
        
        if i == 1:
            print("*")
        else:
            print("*" + " " * (i - 2) + "*")
    
    for i in range(altura - 1, 0, -1):
        espacios = altura - i
        
        print(" " * espacios, end="")
        
        if i == 1:
            print("*")
        else:
            print("*" + " " * (i - 2) + "*")
            
# Ejercicio 2: Escalera de numeros

try:
    altura = int(input("Introduce la altura:"))
    if altura < 0:
        raise ValueError
except ValueError:
    print("Error")

else:
    for i in range(1, altura+1):
        for j in range(1, i+1):
            if i == altura:
                print("4", end="")
            elif j > 1 and j < i:
                print(" ", end="")
            else:
                print("4", end="")
        print()