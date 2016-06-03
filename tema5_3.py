# -*- coding: utf-8 -*-
"""
Created on Wed May 25 17:31:45 2016

@author: marioromero
"""

exponentes = range(1, 11)
exp_list = list(exponentes)

#Que tenemos en la lista? (en lenguaje natural).
print(exponentes)
print(exp_list)

#A~nadir a la lista de exponentes [18, 19].
print("-------------------------------------------------------")
exp_list = exp_list + [18,19]
print(exp_list)

#Para cada elemento de la lista, imprimir por pantalla 2 elevado a x.
print("-------------------------------------------------------")
for i in exp_list:
    print("{} elevado a {} = {}".format(2,i,2**i))

#Para cada elemento de la lista, imprimir por pantalla su
#cuadrado.
print("-------------------------------------------------------")
for j in exp_list:
    print("{} elevado a {} = {}".format(j,2,j**2))

#Hacer que el ejercicio anterior muestre los resultados en orden
#inverso (es decir, hay que iterar sobre los exponentes hacia
#atras).
print("-------------------------------------------------------")
for j in exp_list[::-1]:
    print("{} elevado a {} = {}".format(j,2,j**2))

#Para cada elemento de la lista, comprobar si 2 ** x es un
#numero par.
print("-------------------------------------------------------")
for i in exp_list:
    if((2**i) %2 == 0):
        print("{} elevado a {} = {} es PAR".format(2,i,2**i))
    else:
        print("{} elevado a {} = {} NO es PAR".format(2,i,2**i))