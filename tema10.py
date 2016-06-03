# -*- coding: utf-8 -*-
"""
Created on Fri May 27 19:57:11 2016

@author: marioromero
"""

#Funcion que recibe dos enteros, a y b, y divide el mayor
#por el menor mostrando un mensaje de error si es una
#division entre cero
def division(a,b):  
    try:
        if(a>b):
            return a / b
        else:
            return b/a
    except ZeroDivisionError:
        print("Error. No se puede dividir entre 0.")
#MAIN
print(division(2,4))
print(division(3,0))
     
        
#Programa que itere sobre una lista de cadenas de texto que
#contienen nombres de fichero hasta encontrar el primero
#que existe (IOError) Pista: crear nuestra propia funcion,
#existe fichero(ruta), que devuelve True o False
def existe_fichero(path):
    try:
        fd = open("path","r")
        fd.close()
        return True
    except IOError:
        return False
#MAIN
path = "E:\\zone\\workspace\\python\\files\\"
lista_ficheros = [path+"ejercicio1.py", path+"ejercicio2.py", path+"ejercicio3.py", path+"tema10.py"]
for i in lista_ficheros:
    if existe_fichero:
        print("El fichero '{}' existe".format(i))
    else:
        print("El fichero '{}' NO existe".format(i))
    
        
#Funcion que recibe una lista y el elemento a buscar,
#devolviendo su posicion si existe, y -1 en caso de que no
#(ValueError) Pista: podemos usar la funcion
#list.index(value)
def buscar(elemento,lista):
    try:
        return lista.index(elemento)
    except ValueError:
        return -1       
#MAIN
print(buscar("aaaaa",lista_ficheros))
print(buscar(path+"ejercicio3.py" ,lista_ficheros))


#Funcion que recibe una lista y calcula la suma de todos los
#elementos, devolviendo None en caso de que alguno de los
#elementos no pueda sumarse (TypeError) Pista: <la
#funcion sum() esta a nuestra disposicion!
def suma(lista):
    try:
        return sum(lista)
    except TypeError:
        return None      
#MAIN
lista_numeros = list(range(1,21))
lista_numeros.append("error")
print(suma(lista_numeros))


#Funcion que recibe una lista y un indice, y devuelve el
#elemento que ocupa dicha posicion o None si el indice
#esta fuera de los limites de la lista 
def elementByIndex(i,lista):
    try:
        return lista[i]
    except IndexError:
        return None
   #MAIN
print(elementByIndex(10,lista_numeros)) 
print(elementByIndex(30,lista_numeros)) 
