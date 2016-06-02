# -*- coding: utf-8 -*-
"""
Created on Thu May 26 10:46:59 2016

@author: marioromero
"""

#Guardar en otro fichero de texto una linea con la operacion de suma que 
#incluya todos los operandos y el resultado, e.g: 24 + 34 + 2 = 60
fout = open("other.txt", "w")
ejemplo = "24 34 2"
sumatorio = 0
for s in ejemplo.split():
    sumatorio += int(s)
numeros = " + ".join(ejemplo.split()) + " = " + str(sumatorio) + "\n"
fout.write(numeros)
fout.close()

#A~nadir la linea [1, 2 ... 10]
fout = open("other.txt", "a")
numbers = [str(num) for num in list(range(1, 11))]
line = "\t".join(numbers)
fout.write(line + "\n")
fout.close()

#El producto de los numeros de la ultima linea
fout = open("other.txt", "r")
lines = fout.readlines()
prod = 1
lastline = lines[len(lines)-1]
for i in lastline.split():
    prod *= int(i)
print ("El producto de los numeros de la ultima linea es: {}".format(prod))
fout.close()

#El numero de lneas de "con comentarios" si ignoramos aquellas comentadas 
#(las que empiezan por #)
fd = open("con_comentarios.txt", "r")
commentlines = 0
for l in fd:
    if not l.startswith("#"):
        commentlines += 1
print ("El total de lineas con comentarios es: {}".format(commentlines))
fd.close()

#La suma de todos los numeros impares del documento
fd = open("con_comentarios.txt", "r")
sumaimpares = 0
for li in fd:
    if not li.startswith("#"):
        for nu in li.split():
            number = int(nu)
            if number % 2 != 0:
                sumaimpares += number
print ("La suma de todos los numeros impares del documento es: {}".format(sumaimpares))
fd.close()