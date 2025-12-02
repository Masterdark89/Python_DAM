"""Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 euros, el
segundo 20 euros, el tercero 40 euros y así sucesivamente. Realizar un algoritmo para
determinar cuánto debe pagar mensualmente y el total de lo que pagó después de los 20 meses"""

total = 0

pagar_mes = 10
total += pagar_mes
print("Debe pagar el mes 1:", pagar_mes)

for i in range(2, 21):
    pagar_mes *= 2
    print("Debe pagar el mes ", i, ":", pagar_mes)
    total += pagar_mes

print("El total a pagar es", total, "euros")
