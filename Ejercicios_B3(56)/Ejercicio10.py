"""Un alumno desea saber cuál será su calificación final en la materia de Algoritmos Dicha
calificación se compone de los siguientes porcentajes:
• 55% del promedio de sus tres calificaciones parciales.
• 30% de la calificación del examen final.
• 15% de la calificación de un trabajo final"""
nota_parciales = 0

for i in range(3):
    nota = float(input("Introduce las notas de los parciales:"))
    nota_parciales += nota

nota_exfinal = float(input("Introduce la nota del examen final:"))
nota_trfinal = float(input("Introduce la nota del trabajo final:"))

nota_parciales = nota_parciales / 3
print(nota_parciales)

nota_final = (nota_parciales * 0.55) + \
    (nota_exfinal * 0.3) + (nota_trfinal * 0.15)

print("La nota final es", nota_final)
