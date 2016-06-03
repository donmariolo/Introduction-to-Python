# -*- coding: utf-8 -*-
"""
Created on Tue May 31 20:04:10 2016

@author: marioromero
"""

import pickle

data = {"entero": 3, "float": 2.33, "complejo": 1+3j, "lista": range(100), "tupla": (1,2,3), "diccionario": {"nombre": "Sara", "edad": 20}}
   
#ESCRITURA PICKLE
fout = open("fichero.pick", "wb")
pickle.dump(data, fout)
fout.close()

#LECTURA PICKLE
fin = open("fichero.pick", "rb")
new_data = pickle.load(fin)
fin.close()