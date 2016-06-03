# -*- coding: utf-8 -*-
"""
Created on Thu May 26 10:46:43 2016

@author: marioromero
"""

#La longitud en caracteres de la primera linea?
fd = open("files\\datos_ficheros.txt", "r")
firstline = fd.readline()
print ("First line length: {}".format(len(firstline)))
fd.close()

#El numero de lineas
fd = open("files\\datos_ficheros.txt", "r")
lines = fd.readlines();
print ("Lines number: {}".format(len(lines)))
fd.close()

#Cuantos numeros contiene la primera linea
numfirstline = firstline.split()
print ("Numbers in the first line: {}".format(len(numfirstline)))

#Guardar la suma de los numeros de la primera linea
numbersfirstline = [int(num) for num in numfirstline]
fout = open("files\\sum_numbersfl.txt", "w")
fout.write(str(sum(numbersfirstline))) #fout.write("{:.2f}".format(suma))
print ("Sum of the numbers in the first line: {}".format(sum(numbersfirstline)))
fout.close()