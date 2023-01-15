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

def division (a, b):
    if b == 0:
        print("No se puede divir entre cero")
        time.sleep(2)
    else:
        print("La division de",a," / ", b, " = ", a/b)
        time.sleep(2)

def raiz (a):
    print("La raiz de",a, " = ", np.sqrt(a))
    time.sleep(2)

def exponente (a, b):
    print(a, "elevado a",b," = ", np.power(a, b))
    time.sleep(2)

def seno (a):
    grados = a
    radianes = (grados* math.pi)/180
    print("El seno de",a,"°"," = ", math.sin(radianes))
    time.sleep(2)

def coseno (a):
    grados = a
    radianes = (grados* math.pi)/180
    print("El coseno de",a,"°"," = ", math.cos(radianes))
    time.sleep(2)

def tangente (a):
    grados = a
    radianes = (grados* math.pi)/180
    print("La tangente de",a,"°"," = ", math.tan(radianes))
    time.sleep(2)

while True:
    print("""
    Indique la operación a realizar:

    1) Sumar    
    2) Restar
    3) Multiplicar
    4) Dividir
    5) Raiz n
    6) Exponente n
    7) Seno
    8) Coseno
    9) Tangente
    10) Apagar calculadora
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
        introducirNumero()
        division(numero1,numero2)  
    elif opcion == 5:
        Numero()
        raiz(num1)     
    elif opcion == 6:
        introducirNumero()
        exponente(numero1,numero2)   
    elif opcion == 7:
        Numero()
        seno(num1) 
    elif opcion == 8:
        Numero()
        coseno(num1) 
    elif opcion == 9:
        Numero()
        tangente(num1) 
    elif opcion == 10:
        print("Hasta Pronto ✌")
        break