# -*- coding: utf-8 -*-
"""
Created on Tue May 24 18:19:07 2016

@author: marioromero
"""

#Ejercicio 6
#Lee una cadena de texto del usuario e imprime por
#pantalla un mensaje simpatico si y solo si la cadena es un
#palindromo (se lee igual de izquierda a derecha que de
#derecha a izquierda). Algunos ejemplos:
    #La ruta natural
    #¿Son mulas o civicos alumnos?
    #Dabale arroz a la zorra el abad

while True:
    cadena = input("Introduce una cadena: ")
    cadena = cadena.lower().replace(" ", "")
    print (cadena)
    print (cadena[::-1])
    
    if (cadena == cadena[::-1]):
        print("{} es PALINDROMO".format(cadena))
        break
    else:
        print("Intentalo otra vez")