# -*- coding: utf-8 -*-
"""
Created on Tue May 31 19:16:27 2016

@author: marioromero
"""

"""
11.Realice un listado de ficheros del directorio C:\windows\system32. Almacene en un fichero llamado "listado_windows.txt" la
ruta y tamaño de cada fichero con el formato siguiente: ruta;tamaño con una línea para cada fichero encontrado.

12.Use fichero "listado_windows.txt" para determinar el número de ficheros que tienen igual extensión.

13.¿Cuál es el fichero de mayor tamaño de los registrados en "listado_windows.txt"?
"""
import os

path = "C:\\Windows\\System32"
try:
    fd = open("listado_windows.txt","w")
    for i in os.walk(path):
        for j in i[2]:
            fd.write("{};{}\n".format(os.path.join(i[0],j),os.path.getsize(os.path.join(i[0],j))))
    fd.close()
except OSError:
    print("Problema con el acceso a ficheros")
    
fd = open("listado_windows.txt","r")
lista_nombres_fichero = []
for linea in fd:
    elementos = linea.split(';')
    ruta_fichero = elementos[0]
    tamanyo_fichero = elementos[1]
    lista_nombres_fichero.append(ruta_fichero)
fd.close()

lista_extensiones = [os.path.splitext(fich)[-1] for fich in lista_nombres_fichero]
                     
diccionario  = {}

for extension in lista_extensiones:
    try:
        diccionario[extension.lower()] += 1
    except KeyError:
        diccionario[extension.lower()] = 1 #para la primera vez que salga
