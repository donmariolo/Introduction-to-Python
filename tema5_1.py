# -*- coding: utf-8 -*-
"""
Created on Wed May 25 16:43:34 2016

@author: marioromero
"""

numeros = range(2,101,2)

num_list = list(numeros)

#Que tenemos en la lista? (en lenguaje natural).
print(list(numeros))

#Los ultimos diez elementos de la lista.
print("-------------------------------------------------------")
print(num_list[-10:])

#Todos los elementos excepto los tres primeros.
print("-------------------------------------------------------")
print(num_list[3:])

#Añadimos los valores (13, 12, 11... 2, 1) en el ultimo lugar
print("-------------------------------------------------------")
for i in range(13,0,-1):
    num_list.append(i) 
print(num_list)

#El minimo de los primeros quince elementos.
print("-------------------------------------------------------")
print (min(num_list[:15]))

#Insertamos el minimo de la lista en el ultimo lugar
print("-------------------------------------------------------")
num_list.append(min(num_list[:]))
print(num_list)

#Invertimos el orden de la lista.
print("-------------------------------------------------------")
print(num_list[::-1])

#La suma de los elementos que tienen indices pares.
print("-------------------------------------------------------")
print (sum(num_list[::2]))

#La media aritmetica de los elementos de la lista.
print("-------------------------------------------------------")
suma = 0
for i in num_list:
    suma += i

print (suma/len(num_list))

#A partir de (1, 2, 3, 4, 5), generar (1, 2, 3, 4, 5, 4, 3, 2, 1).
print("-------------------------------------------------------")
init_list = [1, 2, 3, 4, 5]
final_lista=init_list+init_list[-2::-1]
print (final_lista)
