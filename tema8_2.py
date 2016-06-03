# -*- coding: utf-8 -*-
"""
Created on Fri May 27 17:15:01 2016

@author: marioromero
"""

x = [8, 2, 3, 2, 2]
y = [8, 2, 3, 2, 9]

#Cuantos elementos hay en x si se eliminan los repetidos?
print("En x hay {} elementos si eliminamos los repetidos\n".format(len(set(x))))

#Una lista que contenga la concatenacion de ambas listas.
a = x.copy()
print("Concatenamos las listas x: {} e y: {}: {}\n".format(x,y,a.extend(y)))

#Una lista que contenga la union de ambas listas, sin duplicados.
print("Unimos las listas x: {} e y: {}, elminando los repetidos: {}\n".format(x,y,set(x).union(set(y))))

#Un conjunto que tenga la interseccion de ambas listas.
print("Interseccio de las listas x: {} e y: {}: {}\n".format(x,y,set(x).intersection(set(y))))

#Un diccionario en el que para cada entero de la lista x se almacena su 
#cuadrado.
diccionario = {}
for num in set(x):
    diccionario[num] = num**2 
print ("El diccionario con los numeros y sus cuadrados de la lista {} es: {}\n".format(set(x),diccionario))

#Un diccionario en el que se almacena el numero de veces que cada entero 
#aparece en la lista y.
diccionario2 = {}
for num in y:
    #diccionario2[num] = diccionario2.get(num,0)+1
    cont = 1
    if num in diccionario2:
        cont = diccionario2[num] + 1    
    diccionario2[num] = cont
print ("El diccionario con los numeros y sus cuadrados de la lista {} es: {}\n".format(set(x),diccionario2))