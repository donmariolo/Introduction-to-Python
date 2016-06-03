# -*- coding: utf-8 -*-
"""
Created on Thu May 26 20:19:58 2016

@author: marioromero
"""

x = [8,2,3,7,5,3,7,3,1]
x_sorted = sorted(x,reverse=True)

#El mayor numero de la lista
mayor = x_sorted[0]

#menor
menor = x_sorted[-1]

#tres mayores
tresmaores = x_sorted[:3]

#mayor de los 3 primeros
mayordelos3primeros = max(x[:3])

#menor de los cuatro ultimos
menodelos4ultimos = min(x[-4:])

#suma de los 5 mayores
suma5mayores = sum(x_sorted[:5])

#suma de los 3 menores
suma3menores = sum(x_sorted[-3:])