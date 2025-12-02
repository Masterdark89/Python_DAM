"""Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta"""

dia = int(input("Introduce un dia:"))
mes = int(input("Introduce un mes:"))
año = int(input("Introduce un año:"))

if dia > 0 and dia < 32:
    if mes > 0 and mes < 13:
        if año > 0 and año <= 2025:
            print("Fecha correcta")
        else:
            print("Fecha incorrecta")
    else:
        print("Fecha incorrecta")
else:
    print("Fecha incorrecta")
