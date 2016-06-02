# -*- coding: utf-8 -*-
"""
Created on Tue May 24 18:16:35 2016

@author: marioromero
"""

#Ejercicio 2
#Imprime por pantalla la secuencia [0, 1, 2 . . . 100].
print("--------------------------------------------------------------")
list0 = range(101)
for i in list0:
    print(i)

#Imprime por pantalla la secuencia [0, 2, 4 . . . 200].
print("--------------------------------------------------------------")
list2 = range(0,101,2)
for i in list2:
    #if (i%2==0): #para utilizar list, en vez de list2
        print(i)

#Imprime por pantalla la secuencia [86, 84, 82 . . . 14].
print("--------------------------------------------------------------")
list3 = list(range(86,13,-2))
print (list3)

#Imprime por pantalla la secuencia [10, 9, 8 . . . 0].
print("--------------------------------------------------------------")
list4 = range(10,-1,-1)
for i, num in enumerate(list4):
    print("{} -> {}".format(i,num))