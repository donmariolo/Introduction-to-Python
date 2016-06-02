# -*- coding: utf-8 -*-
"""
Created on Mon May 30 18:27:34 2016

@author: marioromero
"""

""" Modulo para el calculo de areas de formas basicas """
pi = 3.1416

def cuadrado ( lado ):
    """ Calcula el area del cuadrado a partir de su lado """
    return lado ** 2

def circulo ( radio ):
    """ Calcula el area del circulo dado el radio """
    return pi * radio ** 2

#==============================================================================
# if __name__ == '__main__':
#     print ('Numero de parametros =', len (sys.argv))
#     for s in sys.argv :
#         print (s, '->', type(s))
#==============================================================================
