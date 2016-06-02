# -*- coding: utf-8 -*-
"""
Created on Mon May 30 19:23:01 2016

@author: marioromero
"""

import operaciones_basicas
import sys

#==============================================================================
# if __name__ == '__main__':
#     print ("{} + {} = {}".format(numero1,numero2,operaciones_basicas.sumar(sys.argv[1],sys.argv[2])))
#     print ("{} - {} = {}".format(numero1,numero2,operaciones_basicas.restar(sys.argv[1],sys.argv[2])))
#     print ("{} * {} = {}".format(numero1,numero2,operaciones_basicas.multiplicar(sys.argv[1],sys.argv[2])))
#     print ("{} / {} = {}".format(numero1,numero2,operaciones_basicas.dividir(sys.argv[1],sys.argv[2])))
#==============================================================================

if __name__ == '__main__':
    print ('Numero de parametros =', len(sys.argv))
    if len(sys.argv) <= 2:
        print("ERROR. Necesito mas de un parametro")
    elif len(sys.argv) == 3:
        num1 = sys.argv[1]
        num2 = sys.argv[2]
        print ("{} + {} = {}".format(num1,num2 ,operaciones_basicas.sumar(num1,num2)))
    else:
        num = [] #lista de numeros
        for p in sys.argv [1:]: 
            num.append(float(p)) 
        suma = 0
        for n in num [0:]:
            suma =  operaciones_basicas.sumar (suma, n)
        print("{} # ({})".format(suma,num.insert(" + ")))