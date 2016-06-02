# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 19:39:33 2016

@author: marioromero
"""

"""
Cree una nueva clase que herede de Cuenta del ejercicio 1. Se llamará Cuenta_ahorro.
Contendrá un nuevo método oculto __avisar que informará en el momento en el que se realice
una operación (retirar) que dé lugar a un saldo negativo. El mensaje a mostrar será
'NUMEROS ROJOS'.
Modifique el método retirar para que no deje sacar dinero si el saldo es negativo. En ese caso
mostrará el mensaje por pantalla 'NO TIENE CREDITO'.
Cree un programa que genere una cuenta en la que se ingresan 300 euros y se sacan, 290, 20 y
30 euros. En cada operación, muestre el saldo actual.
"""

from tema13_123456 import Cuenta

class CuentaAhorro(Cuenta):
    def __avisar(self):
        print("NUMEROS ROJOS")

    def retirar(self,cantidad):
        if(self._Cuenta__saldo < 0):
            print("NO TIENE CRÉDITO")
            self.__avisar()
        else:
            super(CuentaAhorro,self).retirar(cantidad)
   
if __name__ == "__main__":
    ca = CuentaAhorro()
    ca.mostrar(3210)
    print("\n--Ingresos--")
    ca.ingresar(300)
    ca.mostrar(3210)
    print("\n--Retiradas--")
    for i in [290, 20, 30]:
        ca.retirar(i)
        ca.mostrar(3210)