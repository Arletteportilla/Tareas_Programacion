"""Crea un código que solicite ingresar el nombre de un archivo con su extensión y
devuelva la extensión de la misma. Por ejemplo: La extensión de programandoaprenderpython.py es “.py”."""

nombrearchivo = input("Ingrese el nombre un nombre para archivo: ")
na_extns = nombrearchivo.split(".")
print ("El archivo con su extension es : " + repr(na_extns[-1]))
