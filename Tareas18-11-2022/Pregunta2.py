"""Define una función llamada num_max() que nos devuelva en pantalla el número
mayor entre 4 diferentes enteros. No definas ningún valor a imprimir en caso
de que ambos números sean iguales."""

num1 = int(input("Ingrese un valor: "))
num2 = int(input("Ingrese un valor: "))
num3 = int(input("Ingrese un valor: "))
num4 = int(input("Ingrese un valor: "))

def num_max ():
    if num1 > num2 and num1 > num3 and num1 >num4:
        print (num1)
    elif num2 > num1 and num2 > num3 and num2 > num4:
        print (num2)
    elif num3 > num1 and num3 > num2 and num3 > num4:
        print (num3)
    elif num4 > num1 and num4 > num3 and num4 > num2: 
        print(num4)   
    else:
        print ()
num_max()


