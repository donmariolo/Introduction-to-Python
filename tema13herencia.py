# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 19:09:24 2016

@author: marioromero
"""

class Madre:
    def __init__(self,parametro1=0):
        self.parametro1 = parametro1
        
    def metodo1madre(self):
        print("Metodo 1 de la clase Madre. Argumento: {}".format(self.parametro1))
        
    def metodo2madre(self):
        print("Metodo 2 de la clase Madre")
        
class Hija(Madre):
    
    def __init__(self,parametro1,parametro2):
        super(Hija,self).__init__(parametro1) #Madre.__init__(self,parametro1)
        self.parametro2 = parametro2

    def metodo1hija(self):
        print("Metodo 1 de la clase Hija. Argumento: {}".format(self.parametro1))
        

#==============================================================================
# madre = Madre(23)
# print(madre.metodo1madre())
# print(madre.metodo2madre())
# 
# hija = Hija()
# print(hija.metodo1hija())
# print(hija.metodo2madre())
#==============================================================================
