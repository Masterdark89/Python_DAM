"""Escribir un algoritmo para calcular la nota final de un estudiante, considerando que: por
cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en blanco 0. Imprime
el resultado obtenido por el estudiante"""

correcta = int(input("¿Cuantas respuestas correctas?"))
incorrecta = int(input("¿Cuantas respuestas incorrectas?"))
blanco = int(input("¿Cuantas respuestas en blanco?"))

total_preguntas = correcta + incorrecta + blanco
puntos = correcta * 5 - incorrecta

notamax = total_preguntas * 5

print("El alumno tiene", puntos, "sobre", notamax)
