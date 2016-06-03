# -*- coding: utf-8 -*-
"""
Created on Wed May 25 17:20:18 2016

@author: marioromero
"""

x = input("Introduce un numero: ")

x = int(x)
#Imprimir "sentido de la vida encontrado" si x es igual a 42 (if).
#Si no, imprimir "sigue buscando" (else).
if (x==42):
    print("sentido de la vida encontrado")
else:
    print("sigue buscando")

#Si x es menor que cien, imprimir su valor e incrementarlo en uno.
#Si no, actualizar su valor a su cuadrado (x ** 2).
print("-------------------------------------------------------")
if(x<100):
    print("{} + {} = {}".format(x,1,x+1))
    x = x + 1
else:
    print("{} elevado a {} = {}".format(x,2,x**2))
    x = x ** 2

#Si es mayor que cero y par, imprimir "exacto".
#Si no, actualizar su valor a su mitad (x / 2).
print("-------------------------------------------------------")
if (x%2==0):
    print("exacto")
else:
    print("{} / {} = {}".format(x,2,x/2))
    x = x / 2

#Si es mayor que cero, impar y menor o igual que 365, imprimir
#por pantalla el mensaje "podria ser un dia", si no "no lo es".
print("-------------------------------------------------------")
if(x>0 and x%2!=0 and x<=365):
    print("podria ser un dia")
else:
    print("no lo es")

#Si el numero es diferente de cero, imprimir "algo es algo".
#Si el numero es cero, asignarle el valor cien.
print("-------------------------------------------------------")
if(x!=0):
    print("algo es algo")
else:
    x = 100
    print("x ha cambiado su valor a {}".format(x))