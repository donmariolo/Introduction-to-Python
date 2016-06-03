# -*- coding: utf-8 -*-
"""
Created on Tue May 31 17:59:49 2016

@author: marioromero
"""

"""
Cree un script que realice una llamada al código del ejercicio 12.1. 
La salida de ese programa no se imprimirá por pantalla, sino que se guardará en un fichero llamado 'salida.txt'.
"""

import subprocess

subprocess.call("python tema12_1.py files\\in.txt files\\out.txt")

#Si queremos redirigir la salida por consola al fichero salida.txt
#==============================================================================
# fd = open("salida.txt","w")
# subprocess.call("python tema12.1.py in out.txt", stdout = fd)
# fd.close ()
#==============================================================================
