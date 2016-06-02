# -*- coding: utf-8 -*-
"""
Created on Mon May 30 19:13:02 2016

@author: marioromero
"""

import operaciones_basicas
a, b = 13, 3
print ('Operandos =', a, b)
print ('sumar = ', operaciones_basicas.sumar (a, b))
print ('restar = ', operaciones_basicas.restar (a, b))
print ('multiplicar = ', operaciones_basicas.multiplicar (a, b))
print ('dividir = ', operaciones_basicas.dividir (a, b))

import operaciones_basicas as ob
#¿Cómo deberiá importar el módulo para que no hubiera errores al ejecutar?
a, b = 13, 3
print ('Operandos =', a, b)
print ('sumar = ', ob.sumar (a, b))
print ('restar = ', ob.restar (a, b))
print ('multiplicar = ', ob.multiplicar (a, b))
print ('dividir = ', ob.dividir (a, b))

from operaciones_basicas import *
#¿Y cómo importariá para que funcionara el siguiente código?
a, b = 13, 0
print ('Operandos =', a, b)
print ('sumar = ', sumar (a, b))
print ('restar = ', restar (a, b))
print ('multiplicar = ', multiplicar (a, b))
print ('dividir = ', dividir (a, b))