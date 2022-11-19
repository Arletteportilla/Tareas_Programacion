"""Define una función llamada menorque() que nos devuelva en pantalla el número
menor entre dos enteros. Define una salida de texto en caso de que"""

num1= int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

def menorque():
    if num1 < num2:
        print("Es numero menor es: ", num1)  
    elif num2 < num1:
        print("Es un numero menor es: ", num2)    
    else:
        print("Ambos numeros son iguales")    
menorque()
