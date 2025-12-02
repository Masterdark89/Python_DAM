"""Escribe un programa que pida un nombre de usuario y una contraseña y si se ha
introducido "pepe" y "asdasd" se indica "Has entrado al sistema", sino se da un error."""

usuario_correcto = "pepe"
contraseña_correcta = "asdasd"

usuario = input("Introduce tu usuario:")
contraseña = input("Introduce tu contraseña:")

if usuario == usuario_correcto and contraseña == contraseña_correcta:
    print("Has entrado al sistema")
else:
    print("Error")
