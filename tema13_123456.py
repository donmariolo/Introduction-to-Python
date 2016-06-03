# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 16:46:08 2016

@author: marioromero
"""

"""
Cree una clase llamada Cuenta. Como atributo tendrá un número float llamado saldo, con una
cantidad inicial de 0 euros.
Tendrá dos métodos:
• ingresar, con un parámetro que indica la cantidad a sumar al saldo.
• retirar, con un parámetro que será un número float de euros a restar del saldo.
Cree un programa para ingresar 125.23, 503.4 y 50 euros
"""
    
class Cuenta:
    def __init__(self, saldo=0):
        self.__saldo = saldo
        self.__PIN = 3210

    def ingresar(self,cantidad):
        self.__saldo += cantidad

    def retirar(self,cantidad):
        self.__saldo -= cantidad

    def mostrar(self,PIN):
        print("Saldo actual: {:.2f}".format(self.leer_saldo(PIN)))
        
    def leer_saldo (self,PIN):
        if PIN == self.__PIN:
            return self.__saldo
        
    def __repr__(self):
        return "Cuenta({})".format(self.__saldo)
        
    def __unicode__(self):
        return "Saldo: {} euros".format(self.__saldo)

if __name__ == "__main__":
    print("Clase Cuenta")
    #pin = int(input("Dame el numero PIN: "))
    pin = 3210
    cuenta = Cuenta()
    cuenta.mostrar(pin)
    for i in [125.23, 503.4, 50]:
        cuenta.ingresar(i)
        cuenta.mostrar(pin)
    cuenta.retirar (333.34)
    cuenta.mostrar(pin)



"""
Cree una clase llamada Fichero. Esa clase tendrá un atributo llamado ruta y otro llamado
texto.
Implemente dos métodos:
• leer_fichero, que leerá el fichero dado por el atributo ruta y guardará su contenido en
el atributo texto.
• mostrar_fichero, que imprimirá por pantalla el texto del fichero leído.
Use su nueva clase para leer el fichero que contiene al ejercicio 1.
"""
class Fichero:
    def __init__(self,ruta):
        self.ruta = ruta
        self.texto = None
    
    def leer_fichero(self):
        fin = open(self.ruta,"r")
        self.texto = fin.read()
        fin.close()
        
    def mostrar_fichero(self):
        print("El fichero contiene el siguiente texto: '{}'".format(self.texto))
  
if __name__ == "__main__":
    print("Clase Fichero")
    fichero = Fichero("files\\out.txt")
    fichero.leer_fichero()
    fichero.mostrar_fichero()


"""
Cree una clase llamada Persona. Contendrá el nombre, DNI, dirección, teléfono y e-mail (este
último opcional) de un individuo.
Por método tendrá mostrar que imprimirá por pantalla los datos de la persona.
Utilice esa clase para crear una lista de personas y mostrar cada una de ellas. Los datos de
cada persona están en el fichero personas.txt. El formato de este fichero es una linea con los
datos de cada persona. Están separados por ';'. Contiene información por este orden:
nombre;DNI;dirección;teléfono;e-mail;saldo
"""
class Persona:
    def __init__(self,nombre,DNI,direccion,telefono,email=None):
        self.nombre = nombre
        self.DNI = DNI
        self.direccion = direccion
        self.telefono = telefono
        self.email = email

    def mostrar(self):
        print("{};{};{};{};{}".format(self.nombre,self.DNI,self.direccion,self.telefono,self.email))

if __name__ == "__main__":
    print("Clase Persona")
    lista_personas = []        
    fin = open("files\\personas.txt","r")
    for i in fin.readlines():
        if not i == "\n": #if line.strip():
            p = i.split(";")
            #lista_personas.append(Persona(p[0],p[1],p[2],p[3],p[4]))  
            lista_personas.append(Persona(*p[:-1]))
    for j in lista_personas:
        Persona.mostrar(j)
    

"""
Cree una clase llamada Punto. Tendrá como atributos las coordenadas x0 e y0 del origen (0, 0)
por defecto, y las coordenadas x e y del punto en cuestión.
Los métodos serán: distancia y muestra_punto. El primero devolverá la distancia del punto a
su origen. El segundo imprimirá por pantalla el mensaje de texto: (x,y), donde x e y son las
coordenadas del punto.
Ejecute un programa que cree dos puntos con origen en (0,0) y muestre por pantalla el que
tenga una distancia menor al centro:
distancia = math.sqrt ((x-x0)**2 + (y-y0)**2)
"""
import math

class Punto:
    def __init__(self,x,y,x0=0,y0=0):
        self.x = x
        self.y = y
        self.x0 = x0
        self.y0 = y0
    
    def distancia(self):
        return math.sqrt((self.x-self.x0)**2+(self.y-self.y0)**2)
        
    def muestra_punto(self):
        print("Punto dado por el usuario: ({},{})".format(self.x,self.y))

if __name__ == "__main__":
    ("Clase Punto")
    punto1 = Punto(10,5)
    punto2 = Punto(33,4)
    if(punto1.distancia()>punto2.distancia()):
        punto1.muestra_punto()
        print("La distancia del punto ({},{}) al punto ({},{}) es: {}".format(punto1.x,punto1.y,punto1.x0,punto1.y0,punto1.distancia()))
    else: 
        punto2.muestra_punto()
        print("La distancia del punto ({},{}) al punto ({},{}) es: {}".format(punto2.x,punto2.y,punto2.x0,punto2.y0,punto2.distancia()))    
    

"""
5. Cree una clase llamada Segmento. Sus atributos serán dos objetos de la clase Punto. Esos
puntos tendrán el mismo origen de coordenadas.
Como método tendrá longitud, que devolverá la distancia entre los dos puntos que componen
el segmento.
Ejecute un programa que cree un segmento, muestre la longitud de ese segmento y el punto
más cercano al origen.
NOTA: Si se reutiliza código ya hecho, este ejercicio se realiza en 20 lineas de código
"""
class Segmento:
    def __init__ (self, x1, y1, x2, y2, x0=0, y0=0):
        self.punto1 = Punto (x1, y1)
        self.punto2 = Punto (x2, y2)
    
    def longitud(self):
        return math.sqrt((self.punto1.x - self.punto2.x)**2+(self.punto1.y - self.punto2.y)**2)

if __name__ == '__main__':
    seg = Segmento (2, 2, 0, 3)
    if seg.punto1.distancia () > seg.punto2.distancia ():
        print ("Punto mas cercano al origen: {}".format(seg.punto2.muestra_punto ()))
    else:
        print ("Punto mas cercano al origen: {}".format(seg.punto1.muestra_punto ()))
    print ("Longitud del segmento: {}".format(seg.longitud ()))
        