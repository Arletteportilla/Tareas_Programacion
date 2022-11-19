"""Define una función que permita imprimir un mensaje en base a los valores
tomados de una lista para comprobar si todos los de la lista son mayores o
menores de edad."""

def edad (lista):
    for edad in lista:
        if edad >= 18:
            print("Es mayor de edad")  
        else:
            print("Es menor de edad")  

edad([1,23,34,21,12,4])   
