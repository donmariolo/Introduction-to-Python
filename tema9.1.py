# -*- coding: utf-8 -*-
"""
Created on Fri May 27 19:20:53 2016

@author: marioromero
"""

lista = [8, 2, 3, -1, 2, -5, 7, -4]
personas = ["Sara", "Pedro", "Miguel"]

#El cubo de cada elemento de la lista x.
print([x**3 for x in lista])

#El cuadrado de los elementos impares de x.
print([x**2 for x in lista if not x%2==0])

#El cuadrado de los elementos pares y positivos de x.
print([x**2 for x in lista if x%2==0 and x>0])

#Los elementos de personas con mas de cinco caracteres.
print([x for x in personas if len(x)>5])

#Los elementos de personas que contienen la vocal o.
print([x for x in personas if 'o' in x.lower()])

#Los elementos de personas que contienen la vocal e y ademas tienen una 
#longitud de al menos seis caracteres.
print([x for x in personas if 'e' in x.lower() and len(x)>=6])