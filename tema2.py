# -*- coding: utf-8 -*-
"""
Created on Wed May 25 16:28:09 2016

@author: marioromero
"""

#Ejercicio_L2
#Manipulacion de original_lists utilizando el interprete

# original_list de inicio
original_list = ["primero", 2, "3.5", 4.0, "ultimo"]

#1 El tama~no de la original_list?
tam = len(original_list)
print(tam)

#2 El tama~no de la original_list multiplicado por su segundo elemento
print(tam * original_list[1])

#3 El producto del segundo elemento de la original_list por el tercero
print(original_list[1] * float(original_list[2]))

#4 Esta 2 en la original_list? Y 2.0?
if (2 in original_list):
    print("2 esta en lista")
else:
    print("2 NO esta en lista")


if (2.0 in original_list):
    print("2.0 esta en lista")
else:
    print("2 NO esta en lista")

#5 Eliminar el primer elemento de la original_list
del original_list[0]
print(original_list)

#6 Eliminar ahora los dos ultimos elementos simultaneamente
del original_list[-2]
print(original_list)

#7 >Esta la original_list vacia?
emptyList = bool(original_list)
if(emptyList is False):
    print("lista vacia")

#8 A~nadir el elemento "nuevo ultimo" a la original_list.
original_list.append("nuevo ultimo")
print(original_list)