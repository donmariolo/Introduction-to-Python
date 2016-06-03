# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 16:57:18 2016

@author: marioromero
"""

lista = ["uno", "dos", "tres", "cuatro","cinco", "ciento uno", "ciento dos", "ciento tres", "ciento cuatro", "ciento cinco"]

diccionario_compresion = {cadena:len(cadena) for cadena in lista}

print("Diccionario por compresión: {}".format(diccionario_compresion))