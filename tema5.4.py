# -*- coding: utf-8 -*-
"""
Created on Wed May 25 18:21:09 2016

@author: marioromero
"""

exponentes = range(1, 11)
exp_list = list(exponentes)

#Imprimir cada elemento de la lista junto a su posicion (indice).
for i, val in enumerate(exp_list):
    print("{} -> {}".format(i,val))

#Usando una variable en la que vamos almacenando el resultado,
#obtener la suma de calcular 7 ** x (potencias de 7) para cada
#elemento de la lista.
print("-------------------------------------------------------")
res = 0
for i in exp_list:
    res += 7**i
print (res)

#Hacer que el ejercicio anterior se detenga en el momento en el
#que el valor acumulado sea mayor que 200.
print("-------------------------------------------------------")
res = 0
for i in exp_list:
    res += 7**i
    print (res)
    if(res>200):
        print("STOP!")
        break