# -*- coding: utf-8 -*-
"""
Created on Tue May 24 18:16:35 2016

@author: marioromero
"""

numeros1 = [1,2,3,4,5]
numeros2 = [4,5,6,7,8]


#Ejercicio 4
#A partir de dos listas de enteros, 'numeros1' y 'numeros2'
#de igual tamano, generar otra cuyo primer elemento es el
#producto del primer elemento de las listas 'numeros1' y
#'numeros2', y asi sucesivamente. (Fichero for-06-vacio.py)
prodlist = []
for i, n1 in enumerate(numeros1):
    prodlist.append(n1*numeros2[i])

print (prodlist)

for i,j in zip(numeros1, numeros2):
    prodlist.append(i*j)

#A partir de dos listas de enteros, 'numeros1' y 'numeros2',
#almacenar en una lista el resultado de multiplicar cada uno
#de los elementos de 'numeros1' por, a su vez, cada uno de
#los elementos de 'numeros2'. Es decir, la lista resultante
#tendra len(numeros1) * len(numeros2) elementos. (Fichero
#for-07-vacio.py)
print("--------------------------------------------------------------")
prodlist = []
numeros1 = [1,2,3,4,5,2,3]
numeros2 = [4,5,6,7,8]
for i in numeros1:
    for j in numeros2:
        prodlist.append(i*j)
print (prodlist)
