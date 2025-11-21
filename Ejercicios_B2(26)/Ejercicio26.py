"""En un casino de juegos se desea mostrar los mensajes respectivos por el puntaje obtenido
en el lanzamiento de tres dados de un cliente, de acuerdo a los siguientes resultados:
Si los tres dados son seis, mostrar el mensaje “Excelente”
Si dos dados se obtienen seis, mostrar el mensaje “Muy bien”
Si un dado se obtiene seis, mostrar el mensaje “Regular”
Si ningún dado se obtiene seis, mostrar el mensaje “Pésimo”
(Use el control switch)."""

contador = 0
contador_dado = 0

while contador != 3:
    dado = int(input("¿Que puntuacion ha sacado el cliente? "))
    if dado == 6:
        contador_dado = contador_dado + 1
    contador = contador + 1

match contador_dado:
    case 0:
        print("Pésimo")

    case 1:
        print("Regular")

    case 2:
        print("Muy bien")

    case 3:
        print("Excelente")

    case _:
        print("Error")
