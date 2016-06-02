# -*- coding: utf-8 -*-
"""
Created on Tue May 31 18:21:06 2016

@author: marioromero
"""

"""
¿Cuántos días faltan para su cumpleaños?
Si la clase termina a las 14:30 horas, ¿cuánto tiempo le queda para terminar la clase de hoy?
"""

import datetime

mybirth = datetime.date(2016,9,18)
print("Quedan {} días hasta el {}".format((mybirth-datetime.date.today()).days,mybirth))

#==============================================================================
# fin = datetime.time(20,30)
# print("Quedan {} horas hasta las {}".format(fin-datetime.time(),fin))
#==============================================================================


"""
Script que recorra el directorio de instalación de winpython y saque por pantalla todos los ejecutables q contenga
"""

import os

path = "E:\\WinPython-64bit-3.4.4.2"

print ("En el directorio '{}' podemos encontrar los siguientes ejecutables:".format(path))
for i in os.walk(path):
    for j in i[2]:
        if j.endswith('.exe'):    
            print ("    - {}".format(j))