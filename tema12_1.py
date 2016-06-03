# -*- coding: utf-8 -*-
"""
Created on Tue May 31 17:07:47 2016

@author: marioromero
"""

"""
Cree un programa que reciba exactamente 2 parámetros: fichero de entrada y fichero de salida. Si el número de parámetros es
distinto de ese valor, muestre el siguiente mensaje de error 'ERROR: Número de parámetros no válido' y termine el programa.
En caso contrario, abra el fichero de entrada. Si el fichero no existe, imprimir el mensaje 'ERROR: el fichero de entrada no existe'
y termine el programa. Lea el número de espacios en blanco que aparecen en el fichero y guarde en el fichero de salida el
siguiente mensaje: 'En el fichero FFF se han encontrado XXX espacios en blanco.', donde FFF es el nombre del fichero leído y XXX
el número de espacios encontrados. Si el fichero de salida no se puede crear, muestre el mensaje 'ERROR: No se ha podido crear
el fichero de salida' y termine.
"""
import sys
if __name__ == '__main__':
    print ('Numero de parametros =', len(sys.argv))
    if len(sys.argv) != 3:
        print("ERROR: Número de parámetros no válido. Modo de uso: {} fichero_entrada fichero_salida".format(sys.argv[0]))
        sys.exit(1)
    else:
        try:
            fi = open("files\\"+sys.argv[1],"r")
            cont = 0
            for i in fi:
                cont += i.count(" ")
            fi.close()
        except FileNotFoundError:
            print("ERROR: el fichero de entrada no existe")    
            sys.exit(2)
        try:
            fo = open("files\\"+sys.argv[2],"w")
            fo.write("En el fichero {} se han encontrado {} espacios en blanco.".format(sys.argv[1],cont))
            fo.close()
        except:
            print("ERROR: No se ha podido crear el fichero de salida")
            sys.exit(3)