# -*- coding: utf-8 -*-
"""
Created on Thu May 26 19:51:42 2016

@author: marioromero
"""

import tema7 as functions

# MAIN
numberslist = [1,15,235,98,456,122,133,154,2,8,95]
num = 7
x = 2
y = 3
z = 5
 
print("Sumatorio: {}".format(functions.suma(numberslist)))
print("Potencia3: {}".format(functions.potencia3(x,y,z)))
print("Nueva lista con pares y >=113: {}".format(functions.parymayorde(numberslist)))
print("Media: {:.2f}".format(functions.media(numberslist)))
print("Factorial: {}".format(functions.factorial(num)))
print("Divisores de {}: {}".format(num,functions.listadivisores(num)))
print("¿{} es primo? {}".format(num,functions.primo(num)))