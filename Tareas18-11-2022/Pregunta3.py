"""Define una función llamada num_max() que nos devuelva en pantalla el mayor
entre 3 diferentes enteros. En caso de que todos sean iguales imprime en pantalla
un mensaje indicándolo"""

num1 = int(input("Ingrese un valor: "))
num2 = int(input("Ingrese un valor: "))
num3 = int(input("Ingrese un valor: "))


def num_max ():
    if num1 > num2 and num1 > num3 :
        print (num1)
    elif num2 > num1 and num2 > num3:
        print (num2)
    elif num3 > num1 and num3 > num2 :
        print (num3)
   
    else:
        print ("Todos los numeros son iguales")
num_max()