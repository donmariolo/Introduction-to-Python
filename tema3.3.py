# -*- coding: utf-8 -*-
"""
Created on Tue May 24 18:17:30 2016

@author: marioromero
"""

#Ejercicio 3
#Imprime por pantalla todas las potencias de dos menores o
#iguales que 2048, utilizando un bucle while.
pot = 0
i = 0
while pot < 2048:
    pot = 2**i
    print ("2 elevado a {} = {}".format(i,pot))
    i = i+1

#Lee valores del usuario hasta que teclee un numero par,
#utilizando un bucle while.
print("--------------------------------------------------------------")
while True:
    x=input("Introduce un numero: ")
    if(int(x)%2==0):
        print("Correcto!")
        break

#Imprime por pantalla las primeras 15 potencias de dos.
print("--------------------------------------------------------------")
i = 0
while i<=15:
    pot = 2**i
    print ("2 elevado a {} = {}".format(i,pot))
    i = i+1

#Lee una cadena de texto del usuario y para cada letra
#indica si es una vocal o una consonante.
print("--------------------------------------------------------------")
cadena=input("Introduce un texto: ")
vocales="aeiou"
for letra in cadena.lower():
    if(letra in vocales):
        print("{} es VOCAL".format(letra))
    else:
        print("{} es CONSONANTE".format(letra))

#A partir de dos listas de enteros, 'numeros1' y 'numeros2',
#crea una lista que contiene aquellos valores de la primera
#que tambien estan en la segunda e imprimela por pantalla.
#Es decir, calcula la interseccion de ambas listas. (Fichero
#for-05-vacio.py)
print("--------------------------------------------------------------")
list = []
numeros1 = [1,2,3,4,5,6,7,8,9]
numeros2 = [1,4,6,8,10]
for i in numeros1:
    if i in numeros2:
        print("{} esta en las dos listas".format(i))
        list.append(i)