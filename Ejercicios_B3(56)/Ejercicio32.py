"""La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro
es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos cuestan 1 euro, los
siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos, y a partir del décimo
minuto, 50 céntimos. Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día,
en turno de mañana, 15 %, y en turno de tarde, 10 %.
Realice un algoritmo para determinar cuánto debe pagar por cada concepto una persona
que realiza una llamada"""

tiempo = int(input("¿Cuanto ha durado la llamada (en minutos)?"))

dia = input("¿Que día?")
dia.lower()

hora = int(input("¿A que hora?"))
while hora < 0 or hora > 23:
    print("Hora incorrecta")
    hora = int(input("¿A que hora?"))

if tiempo >= 5:
    dinero = 1
    tiempo -= 5

    if tiempo >= 3:
        dinero += 0.8
        tiempo -= 3

        if tiempo >= 2:
            dinero += 0.7
            tiempo -= 2

            if tiempo != 0:
                dinero += 0.5 * tiempo
        else:
            dinero += 0.7
    else:
        dinero += 0.8

else:
    dinero = 1


if dia == "domingo":
    pagar = dinero + (dinero * 0.03)
else:
    if hora >= 0 and hora <= 12:
        pagar = dinero + (dinero * 0.15)
    else:
        pagar = dinero + (dinero * 0.10)

print("El dinero a pagar es", dinero)
