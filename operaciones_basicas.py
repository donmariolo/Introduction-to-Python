# -*- coding: utf-8 -*-
"""
Created on Mon May 30 19:09:45 2016

@author: marioromero
"""

""" Modulo que implementa las operaciones básicas matematicas """

def sumar(a,b):
    """ Funcion que suma dos elementos """
    return a+b
     
def restar(a,b):
    """ Funcion que resta dos elementos """
    return a-b
    
def multiplicar(a,b):
    """ Funcion que multiplica dos elementos """
    return a*b
    
def dividir(a,b):
    """ Funcion que divide dos elementos y saca una excepcion si el divisor es igual a 0 """
    try:
        return a/b
    except ZeroDivisionError:
        return print("ERROR: No se puede dividir por cero")
        raise ZeroDivisionError
        
        
