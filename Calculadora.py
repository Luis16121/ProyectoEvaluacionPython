import time
import math
import numpy as np

def Numero():
    global num1
    num1 = int(input("Introduzca el primer número: "))

def introducirNumero ():
    global numero1, numero2
    numero1 = int(input("Introduzca el primer número: "))
    numero2 = int(input("Introduzca el segundo número: " ))

def sumar (a, b):
    print("La suma de", a ," + " , b , " = ", a+b)
    time.sleep(2)

def restar (a, b):
    print("La resta de", a ," - " , b , " = ", a-b)
    time.sleep(2)

def multiplicacion (a, b):
    print("La multiplicación de", a ," x " , b , " = ", a*b)
    time.sleep(2)


while True:
    print("""
    Indique la operación a realizar:

    1) Sumar    
    2) Restar
    3) Multiplicar
    4) Apagar calculadora

    """)

    opcion = int(input(">> "))

    if opcion == 1:
        introducirNumero()
        sumar(numero1,numero2)
    elif opcion == 2:
        introducirNumero()
        restar(numero1,numero2)
    elif opcion == 3:
        introducirNumero()
        multiplicacion(numero1,numero2)
    elif opcion == 4:
        print("Hasta Pronto ✌")
        break