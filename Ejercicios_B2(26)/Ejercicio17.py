"""Escriba un programa que simule un inicio de sesión solicitando el nombre de usuario y
contraseña, y mostrar un mensaje en pantalla, inicio de sesión correcto/ nombre de usuario
incorrecto"""

usuario_real = "usuario1225"
contraseña_real = "contraseñasegura123"
entrar = False
entrar2 = False

usuario = input("Introduce tu usuario:")
contraseña = input("Introduce tu contraseña:")

if usuario == usuario_real:
    entrar = True
else:
    print("Usuario incorrecto")

if contraseña == contraseña_real:
    entrar2 = True
else:
    print("Contraseña incorrecto")

if entrar and entrar2:
    print("Inicio de sesión correcto")
