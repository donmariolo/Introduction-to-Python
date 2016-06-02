# -*- coding: utf-8 -*-
"""
Created on Thu May 26 18:02:25 2016

@author: marioromero
"""

def suma(numbers):
    """Funcion que recibe una lista de enteros y devuelve la suma de todos sus elementos"""
    result = 0
    for n in numbers:
        result += n
    return result

def potencia3(x,y,z):
    """Funcion que recibe tres parametros (x, y, z) y devuelve xyz"""
    return x**(y**z)

def parymayorde(numbers):
    """Funcion que recibe una lista de enteros y devuelve otra lista con aquellos que son pares y >= 113"""
    result = []
    for n in numbers:
        if n%2==0 and n>=113:
            result.append(n)
    return result

def media(numbers):
    """Funcion que recibe una lista de enteros y calcula su media aritmetica"""
    return suma(numbers)/len(numbers)

def factorial(num):
    """Funcion que calcula el factorial de un numero"""
    factorial = 1
    listafactorial = range(num,0,-1)
    for i in listafactorial:
        factorial *= i
    return factorial

def listadivisores(num):
    """Funcion que recibe un numero y devuelve una lista con todos sus divisores"""
    divisores = []
    for n in range(1, num+1):
        if(num%n==0):
            divisores.append(n)
    return divisores

def primo(num):
    """Funcion que determina si un numero es primo (si SOLO divisible entre 1 y él mismo) o no"""
    for i in range(2,num):
        if (num%i)==0:
            return False
    return True