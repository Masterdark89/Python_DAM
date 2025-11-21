"""Dibuja un ordinograma que calcula el salario neto semanal de un trabajador en función del
número de horas trabajadas y la tasa de impuestos de acuerdo a las siguientes hipótesis:
• Las primeras 35 horas se pagan a tarifa normal.
• Las horas que pasen de las 35 horas se pagan a 1,5 veces la tarifa normal.
• Las tasas de impuesto son:
o Los primeros 500€ son libres de impuestos.
o Los siguientes 400€ tiene un 25% de impuesto.
o Los restantes un 45% de impuesto.
Escribe el nombre del trabajador, salario bruto, tasas y salario neto"""

horas = int(input("Introduce el número de horas trabajadas: "))
tarifa = float(input("Introduce la tarifa usada: "))

# saldo bruto
if horas <= 35:
    sueldo = horas * tarifa
else:
    horas = horas - 35
    sueldo = horas * (1.5*tarifa) + (35*tarifa)

# impuestos
if sueldo < 500:
    sueldo_final = sueldo
else:
    sueldo = sueldo - 500
    if sueldo < 400:
        sueldo = sueldo * 25 / 100
        sueldo = sueldo + 500
    else:
        sueldo = sueldo - 400
        sueldo = (sueldo * 45 / 100) + (400 * 25 / 100) + 500

print("El sueldo que recibirá el empleado es: ", sueldo, "euros")
