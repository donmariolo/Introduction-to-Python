# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 20:00:42 2016

@author: marioromero
"""

"""
Cree una clase llamada Buscador. Sirve para buscar y reemplazar palabras dentro de un
fichero. Esa clase heredará de la clase Fichero del ejercicio 2.
Tendrá tres nuevos métodos:
• buscar, que tendrá como parámetro una cadena de caracteres que buscar en el fichero.
Devolverá el número de veces que se ha encontrado el texto buscado.
• reemplazar, que tendrá como parametros dos cadenas de caracteres: la cadena a
buscar y la cadena por la que reemplazar la cadena buscada.
• escribir, que guardará el fichero en la ruta que se pase como parámetro a este nuevo
método.
Ejecute un codigo Python que cree un objeto Buscador. Leerá el fichero ejercicio1.py y
devolverá el número de veces que aparezca la palabra self. Posteriomente, reemplazará la
palabra self por this, y guardará el texto resultante en el fichero ejercicio1_mod.py.
Compruebe que los cambios se han llevado a cabo en este último fichero.
"""

from tema13_123456 import Fichero
import os

class Buscador(Fichero): 
    def buscar(self,cadena):
        if self.texto is None:
            print("Tiene que leer el fichero primero")
        else:
            return self.texto.count(cadena)
    
    def reemplazar(self,cadena_buscar,cadena_reemplazar):
        if self.texto is None:
            print("Tiene que leer el fichero primero")
        else:
            return self.texto.replace(cadena_buscar,cadena_reemplazar)
    
    def escribir(self,ruta):
        if self.texto is None:
            print("Tiene que leer el fichero primero")
        else:
            try:
                fout = open(ruta,"w")
                fout.write(self.texto)
                fout.close()
            except OSError:
                print("Error en el fichero {}".format(ruta))
    
    def __lt__(self,other):
        return os.path.getsize(self.ruta)<os.path.getsize(other)
        
if __name__ == '__main__':
    fich1 = Fichero("files\\out.txt")
    fich2 = Fichero("files\\con_comentarios.txt")
    
    buscador = Buscador("files\\out.txt")
    buscador.leer_fichero()
    print("Numero de ocurrencias de 'en': {}".format(buscador.buscar("en")))
    buscador.reemplazar("en","ne")
    buscador.escribir("files\\out2.txt")    
    
    #print(fich1 < fich2)