# -*- coding: utf-8 -*-
"""
Created on Wed May 25 17:37:11 2016

@author: marioromero
"""

init_list = [59,67,88,99,100,13,15,25]
init_List1 = init_list[:-1]
init_list2 = init_list[1:]
diferencia = []
    
for i,j in zip(init_list,init_list2):
    diferencia.append(j-i)
    
print (diferencia)