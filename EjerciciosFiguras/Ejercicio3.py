"""Imprime una pirámide de altura n donde se alternan asteriscos y espacios, formando un patrón de huecos internos.

Figura para n=6:

     *
    * *
   *   *
  * * * *
 *       *
***********"""

n = 6
contador = 0

for i in range(1, n+1):
    espacios = n - i

    if i == 1:
        print(" " * espacios + "*")

    elif i == n:
        print("*" * (2 * n - 1))

    else:
        if contador == 2:
            print(" " * espacios + "*" + (" " + "*") * 2 + " " + "*")
            contador = 0
        else:
            print(" " * espacios + "*" + " " * (2 * i - 3) + "*")
            contador += 1
