"""Dibuja un ordinograma que lea una calificación numérica entre 0 y 10 y la transforme en la
calificación alfabética, escribiendo el siguiente resultado.
• De 0 a < 3 Muy Deficiente.
• De 3 a < 5 Insuficiente.
• De 5 a < 6 Suficiente.
• De 6 a < 7 Bien.
• De 7 a <9 Notable.
• De 9 a 10 Sobresaliente."""

n = int(input("Introduce una nota: "))

match n:
    case n if 0 <= n < 3:
        print("Muy deficiente")
    case n if 3 <= n < 5:
        print("Insuficiente")
    case n if 5 <= n < 6:
        print("Suficiente")
    case n if 6 <= n < 7:
        print("Bien")
    case n if 7 <= n < 9:
        print("Notable")
    case n if 9 <= n <= 10:
        print("Sobresaliente")
    case _:
        print("Nota no válida")
