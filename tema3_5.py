# -*- coding: utf-8 -*-
"""
Created on Tue May 24 18:18:44 2016

@author: marioromero
"""

cadenas=["python","hello", "word","informatica"]

#Ejercicio 5
#Para cada una de las cadenas de texto almacenadas en
#una lista, imprimir por pantalla el indice y la cadena en si
#e indicar si la palabra es demasiado corta (cinco o menos
#caracteres) o larga (mas de cinco caracteres) (Fichero
#for-08-vacio.py).
for i, cadena in enumerate(cadenas):
    tam = len(cadena)
    print("{}: '{}' tiene {} letras".format(i,cadena,tam))  
    if tam<=5:
        print("\tPEQUEÑO\n")
    else:
        print("\tGRANDE\n")

#Recibe una lista de enteros y calcula la media aritmetica
#(Fichero for-09-vacio.py).
print("--------------------------------------------------------------")
numeros=[1,2,3,4,5,6,77,11,3]
suma = 0

for i in numeros:
    suma = suma + i

print("La media de estos {} elementos es: {}".format(len(numeros),suma/len(numeros)))