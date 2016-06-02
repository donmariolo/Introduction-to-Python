# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 11:34:24 2016

@author: marioromero
"""

"""
Cree una clase llamada Cliente. Contendrá los datos de una Persona (ejercicio 3) y de una cuenta de ahorro (ejercicio 7) como atributos (herede Cliente de Persona y Cuenta_ahorro). Tendrá un nuevo atributo llamado credit que, por defecto, será de 1000 euros. 
Tendrá un método nuevo que será mostrar_datos, que imprimirá por pantalla los datos de la persona y su saldo y credito actuales. 
Cree una persona con estos datos:
   Nombre: Mariano Fuentes
   DNI: 45365968L
   Direccion: C/ de las Alpujarras 2, bajo
   Telefono: 958776566
   Saldo: 2500
   Credito: 1500
   email: mfuentes@iaa.es
y muestre estos datos.
"""

from tema13_123456 import Persona
from tema13_7 import CuentaAhorro

class Cliente(Persona,CuentaAhorro):
    def __init__(self,nombre,DNI,direccion,telefono,email=None,saldo=0,credito=1000):
        Persona.__init__(self,nombre,DNI,direccion,telefono,email)
        CuentaAhorro.__init__(self,saldo)
        self.credito = credito
    
    def mostrar_datos(self):
        Persona.mostrar(self)
        CuentaAhorro.mostrar(self,3210)
        print("Credito: {:.2f}".format(self.credito))

if __name__ == "__main__":
    cliente = Cliente("Mariano Fuentes","45365968L","C/ de las Alpujarras 2, bajo","958776566","mfuentes@iaa.es",2500,1500)
    cliente.mostrar_datos()